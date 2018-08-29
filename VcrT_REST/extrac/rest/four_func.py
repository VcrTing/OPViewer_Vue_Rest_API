import time

from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from rest_framework.throttling import BaseThrottle, SimpleRateThrottle
from rest_framework.permissions import BasePermission
from rest_framework import views

from django.core.cache import cache

from appis.user.models import UserToken
from VcrT_REST.conf import cache_key, anonymous

"""
    认证
"""
class AnonymousAuth(BaseAuthentication):
    def authenticate(self, request):
        pass

    def authenticate_header(self, request):
        pass

class VcrTTokenAuth(BaseAuthentication):
    def authenticate(self, request):
        try:
            token = request._request.GET.get('token')
            token_data = UserToken.objects.filter(token = token).first()
            if not token_data:
                raise exceptions.AuthenticationFailed('User authenticate false !!!')
            return (token_data.user_info, token_data)
        except Exception as e:
            return None

    def authenticate_header(self, request):
        pass

"""
    权限
"""
class DefaultPermission(BasePermission):
    def has_permission(self, request, view):
        try:
            if request.user.type == 0:
                print('黑名单用户无法访问！！！')
                return False
        except:
            pass
        return True

"""
    节流
"""
class VcrTThrottle(SimpleRateThrottle):
    scope = 'VcrT'

    def get_cache_key(self, request, view):
        return self.get_ident(request)

class AnonymousThrottle(SimpleRateThrottle):
    scope = anonymous

    def get_cache_key(self, request, view):
        return self.get_ident(request)

class DefaultThrottle(SimpleRateThrottle):
    scope = anonymous

    def get_cache_key(self, request, view):
        return self.get_ident(request)

    def allow_request(self, request, view):
        if (request.user != anonymous):
            vt = VcrTThrottle()
        else:
            vt = AnonymousThrottle()
            self.history = None
        return vt.allow_request(request, view)
    
    def wait(self):
        return None