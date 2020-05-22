from django.db import models

# Create your models here.

from doctorConsultation.models import *
from drugZoneUsers.models import CustomUser

class UploadPrescription(models.Model):
	user = models.ForeignKey('drugZoneUsers.CustomUser',on_delete = models.CASCADE,null = True,blank =True)
	image = models.FileField(upload_to="media/uploads/", null = True, blank = True)
	symptom = models.ManyToManyField('doctorConsultation.Symptom')
	referDoctor = models.ForeignKey('doctorConsultation.DoctorList',on_delete = models.CASCADE,null = True,blank =True)
	medicinesDescription = models.CharField(max_length = 150, null = True, blank = True)
	createdAt = models.DateTimeField(auto_now_add = True)
	updatedAt = models.DateTimeField(auto_now = True)


	def __str__(self):
		return str(self.user)



	