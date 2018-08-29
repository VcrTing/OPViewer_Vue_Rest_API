from django.shortcuts import render
from django.views import View
from django.db.models import Q
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ( 
    ModelViewSet, GenericViewSet,
    ViewSetMixin
)
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer

from .serializers import UserInfoSerializer, UserTokenSerializer
from extrac.rest.four_func import VcrTTokenAuth
from extrac.rest.pagination import VcrTLOPager

from appis.user.models import UserInfo, UserToken
from appis.kuukann import models as kk_mds

from VcrT_REST.conf import (
    cache_key, cache_time,
    success_code, error_code, warning_code,
    kuukann_url
)
from extrac.utils.scurity import safe_md5
# Create your views here.

class LoginView(ViewSetMixin, APIView):
    """
        视图 - 登录
    """
    # renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    authentication_classes = []
    def check(self, request):
        ret = {
            'code': '',
            'msg': '',
            'user': None
        }
        user_name = request._request.GET.get('user_name', None)
        user_pwd = request._request.GET.get('user_pwd', None)
        try:
            user_info = UserInfo.objects.filter(Q(name = user_name) & Q(pwd = user_pwd))
            if len(user_info) == 1:
                user = user_info[0]
                ret['msg'] = 'The account is right ~'
                ret['code'] = success_code
                ret['user'] = {
                    'lucy': user.id,
                    'user_name': user.name,
                    'user_type': user.type,
                    'user_status': user.status,
                    'user_face': str(user.face)
                }
            else:
                ret['code'] = warning_code
                ret['msg'] = 'The account is right, but has %d count !!!'% len(user_info)
        except Exception as e:
            print(e)
            ret['msg'] = 'No that account !!!'
            ret['code'] = error_code
        return JsonResponse(ret, safe=False)

    def login(self, request):
        ret = {
            'code': '',
            'msg': '',
            'token': None,
            'img_url': None,
        }
        try:
            lucy = request._request.POST.get('lucy', None)
            print('lucy = ', lucy)
            user_info = UserInfo.objects.filter(id = lucy).first()

            token = safe_md5(user_info.name + user_info.pwd)
            ret['token'] = token
            UserToken.objects.update_or_create(user_info=user_info, defaults={'token': token})

            ret['code'] = success_code
            ret['msg'] = 'Token get success !!!'

        except Exception as e:
            print(e)
            ret['code'] = error_code
            ret['msg'] = 'Server runtime error !!!'
        return JsonResponse(ret)
        
class UserInfoView(ModelViewSet):
    """
        视图 - 用户信息
    """
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
    pagination_class = VcrTLOPager

class UserTokenView(ModelViewSet):
    """
        视图 - 认证信息
    """
    queryset = UserToken.objects.all()
    serializer_class = UserTokenSerializer
    pagination_class = VcrTLOPager

class IndexView(View):
    authentication_classes = []
    def get(self, request):
        user = UserInfo.objects.all().first()
        print('index_user = ', user)
        return render(request, 'index.html', {
            'msg': 'We have no page for this server ~',
            'img': user.face
        })
