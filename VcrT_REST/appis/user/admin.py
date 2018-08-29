from django.contrib import admin
from .models import UserInfo, UserToken

# Register your models here.

class UserInfoAdmin(admin.ModelAdmin):
    pass

class UserTokenAdmin(admin.ModelAdmin):
    list_display = ('user', 'token')

admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(UserToken, UserInfoAdmin)