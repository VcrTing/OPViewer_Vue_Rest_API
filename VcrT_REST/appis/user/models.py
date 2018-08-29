import os
from django.db import models
from django.utils import timezone
from VcrT_REST.conf import face_upload_path

# Create your models here.
def face_upload(user_info, filename):
    return os.path.join(face_upload_path, filename)

class UserInfo(models.Model):
    USER_TYPE = (
        (0, '黑名单用户'),
        (1, '普通用户'),
        (2, 'VIP用户')
    )
    name = models.CharField(max_length=120, verbose_name='用户名')
    pwd = models.CharField(max_length=220, verbose_name='密码')
    type = models.SmallIntegerField(choices=USER_TYPE, verbose_name='用户类型')
    status = models.NullBooleanField(default=True, verbose_name='账号状态')
    face = models.ImageField(upload_to=face_upload, verbose_name='头像', default='def_face.jpg')

    def __str__(self):
        return self.name

class UserToken(models.Model):
    user_info = models.OneToOneField(to='UserInfo', on_delete=models.SET_NULL, null=True, blank=True)
    token = models.CharField(max_length=220, verbose_name='token信息')
    update_time = models.DateTimeField(default=timezone.now(), verbose_name='更新时间')

    def __str__(self):
        return 'token'
