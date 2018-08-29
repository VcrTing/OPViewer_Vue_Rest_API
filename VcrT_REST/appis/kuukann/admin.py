from django.contrib import admin
from .models import Img

from VcrT_REST.conf import admin_title, admin_header

admin.site.site_title = admin_title
admin.site.site_header = admin_header
# Register your models here.

class ImgAdmin(admin.ModelAdmin):
    list_display = ('tiny_img', )

admin.site.register(Img, ImgAdmin)