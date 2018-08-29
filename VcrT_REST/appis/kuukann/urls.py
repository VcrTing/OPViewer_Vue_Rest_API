from django.conf.urls import url
from django.urls import path, include

from rest_framework import routers


from .views import (
    ImgView,
    LogicImgView, OptImgView, ImgUtilView
)
app_name = 'kuukann'

router = routers.DefaultRouter()
router.register(r'img', ImgView)

urlpatterns = [
    url(r'^', include(router.urls)),

    path('logic_img', LogicImgView.as_view()),
    path('opt_img/<int:lucy>', OptImgView.as_view()),
    path('util_img/<int:lucy>', ImgUtilView.as_view())
]