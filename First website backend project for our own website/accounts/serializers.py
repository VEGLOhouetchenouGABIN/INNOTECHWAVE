from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from rest_framework import serializers
from .models import Profil


User = get_user_model()

class UserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['id','first_name','last_name',"email",'password','skills_description','is_active']
        extra_kwargs = {'password': {'write_only': True}, 'is_active': {'read_only': True}}
        #depth = 1

class ProfilSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profil
        fields=['id','user','image']

class ProfilSerializerList(serializers.ModelSerializer):
    class Meta:
        model=Profil
        fields=['id','user','image']
        depth=1


# class LogoutSerializer(serializers.Serializer):
#     refresh = serializers.CharField()

#     default_error_message = {
#         'bad_token': ('Token is expired or invalid')
#     }

#     def validate(self, attrs):
#         self.refresh_token = attrs['refresh']
#         return attrs

#     def save(self, **kwargs):

#         try:
#             RefreshToken(self.refresh_token).blacklist()
#         except TokenError:
#             self.fail('bad_token')