import os
from django.db import models
from django.utils import timezone
from appis.user.models import UserInfo

from VcrT_REST.conf import img_upload_path

# Create your models here.
def img_upload(img, file_name):
    return os.path.join(img_upload_path, str(img.user_info.id), 'original', file_name)

def tiny_img_upload(img, file_name):
    return os.path.join(img_upload_path, str(img.user_info.id), file_name)

class Img(models.Model):
    img = models.ImageField(upload_to=img_upload, verbose_name='图片')
    tiny_img = models.ImageField(upload_to=tiny_img_upload, verbose_name='缩略图')

    created_time = models.DateTimeField(default=timezone.now(), verbose_name='创建时间')
    status = models.NullBooleanField(default=True, verbose_name='状态')
    user_info = models.ForeignKey(UserInfo, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='所属用户')

    def __str__(self):
        try:
            return self.user_info.name + '的图片'
        except:
            return '图片'