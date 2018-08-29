import time

from django.shortcuts import render
from django.db.models import Q
from django.views import View
from django.http import JsonResponse, HttpResponse
from django.utils import timezone

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ViewSetMixin, GenericViewSet

from .serializers import ImgSerializer
from .models import Img
from appis.user.models import UserInfo
from extrac.rest.pagination import VcrTLOPager, VcrTCPPager

from VcrT_REST.conf import (
    success_code, error_code, warning_code,
    kuukann_url
)
from extrac.rest.four_func import DefaultThrottle
# Create your views here.

class ImgView(ModelViewSet):
    """
        视图 - 图片
    """
    queryset = Img.objects.all()
    serializer_class = ImgSerializer
    pagination_class = VcrTCPPager

class LogicImgView(APIView):
    """
        逻辑视图 - 图片
    """
    def get(self, request):
        lucy = request._request.GET.get('lucy', None)

        img_queryset = Img.objects.filter(Q(user_info_id = lucy) & Q(status = True))
        pager = VcrTCPPager()
        pager_img_queryset = pager.paginate_queryset(queryset= img_queryset, request= request, view= self)
        img_ser = ImgSerializer(pager_img_queryset, many= True)
       
        return pager.get_paginated_response(img_ser.data)

    def post(self, request):
        ret = {
            'code': error_code,
            'msg': 'Plus img failed !!!'
        }
        new_img = request._request.FILES.get('new_img', None)
        # lucy = request._request.POST.get('lucy', None)

        user_info = request.user
        img = Img()
        img.created_time = timezone.now()
        img.status = True
        img.user_info = user_info

        img.img = new_img
        img.tiny_img = new_img

        img.save()
        ret['code'] = success_code
        ret['msg'] = 'Plus img success ~'
        ret['new_img_url'] = kuukann_url + 'img/' + str(img.id)

        return JsonResponse(ret)
    
class OptImgView(APIView):
    """
        操作视图 - 图片
    """
    throttle_classes = [ DefaultThrottle ]
    def get(self, request, *args, **kwargs):
        lucy = kwargs['lucy']
        img_one = Img.objects.first()
        return JsonResponse({
            'url': str(img_one.img)
        })

    def delete(self, request, *args, **kwargs):
        ret = {
            'code': error_code,
            'msg': 'Delete success !!!'
        }
        try:
            lucy = kwargs['lucy']
            img_one = Img.objects.get(id = lucy)
            img_one.status = False
            img_one.save()

            ret['code'] = success_code
            ret['img'] = {
                'lucy': img_one.id,
                'path': str(img_one.tiny_img),
                'del_time': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            }
        except Exception as e:
            print(e)
            ret['code'] = error_code
            ret['msg'] = 'Delete failed !!!'
        return JsonResponse(ret)

class ImgUtilView(View):
    """
        工具视图 - 图片
    """
    def get(self, request, *args, **kwargs):
        lucy = kwargs['lucy']
        flag = request.GET.get('flag', None)
        print('flag = ', flag)
        if flag == 'plus':
            return render(request, 'img_plus.html', {
                'lucy': lucy
            })
        elif flag == 'show':
            img_url = request.GET.get('original_img', None)
            print("img_url =", img_url)
            return render(request, 'img_show.html', {
                'img_url': img_url
            })