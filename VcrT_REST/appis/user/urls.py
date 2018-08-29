from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from .views import (
    UserInfoView, UserTokenView, 
    LoginView
)

app_name = 'user'

router = routers.DefaultRouter()
router.register(r'user_info', UserInfoView)
router.register(r'user_token', UserTokenView)

urlpatterns = [
    url(r'^', include(router.urls)),

    path('login', LoginView.as_view({
        'get': 'check',
        'post': 'login'
    }))
]