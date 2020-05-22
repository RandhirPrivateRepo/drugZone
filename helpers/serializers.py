from rest_framework import serializers
from .models import * 



class BannerImagesSerializer(serializers.ModelSerializer):
	class Meta:
		model = BannerImages
		fields = '__all__'

