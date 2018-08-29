from rest_framework import serializers

from .models import UserInfo, UserToken

class UserInfoSerializer(serializers.ModelSerializer):
    """
        序列化 - 用户信息
    """
    user_name = serializers.CharField(source='name')
    user_pwd = serializers.CharField(source='pwd')
    user_face = serializers.ImageField(source='face')

    user_type = serializers.CharField(source='get_type_display')
    user_status = serializers.NullBooleanField(source='status')

    class Meta:
        model = UserInfo
        fields = [ 'id', 'user_name', 'user_pwd', 'user_type', 'user_status', 'user_face']

class UserTokenSerializer(serializers.ModelSerializer):
    """
        序列化 - 用户Token
    """
    user_info = serializers.SerializerMethodField()

    class Meta:
        model = UserToken
        fields = [ 'id', 'token', 'update_time', 'user_info']

    def get_user_info(self, row):
        user = row.user_info.all()[0]
        return {
            'user_id': user.id,
            'user_name': user.name
        }
    