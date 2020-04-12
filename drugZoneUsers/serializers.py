from rest_framework import serializers
from .models import * 



class CustomUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = CustomUser
		fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = CustomUser
		fields = ('id','name','email','phone','profileImage','deviceToken','deviceType')


class UserProfileUpdateSerializer(serializers.ModelSerializer):
	class Meta:
		model = CustomUser
		fields = ('name','phone','profileImage')

