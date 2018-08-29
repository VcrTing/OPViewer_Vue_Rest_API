from rest_framework import serializers

from .models import Img

class ImgSerializer(serializers.ModelSerializer):
    """
        序列化 - 图片
    """
    original_img = serializers.ImageField(source='img')
    comped_img = serializers.ImageField(source='tiny_img')

    data_status = serializers.NullBooleanField(source='status')
    user_info = serializers.SerializerMethodField()

    class Meta:
        model = Img
        fields = [ 'id', 'data_status', 'comped_img', 'original_img', 'created_time', 'user_info']

    def get_user_info(self, row):
        try:
            user = row.user_info
            return {
                'lucy': user.id,
                'name': user.name
            }
        except:
            return None
