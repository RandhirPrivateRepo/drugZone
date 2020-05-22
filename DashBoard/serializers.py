from rest_framework import serializers
from .models import * 



#-----------------------------------LABTEST---------------------------------------#

class LabTestSerializer(serializers.ModelSerializer):
	class Meta:
		model = LabTest
		fields = '__all__'
		depth = 1

