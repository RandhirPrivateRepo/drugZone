from django.db import models

# Create your models here.
from drugZoneUsers.models import CustomUser


class Symptom(models.Model):
	name = models.CharField(max_length = 255,null = True, blank = True)
	createdAt = models.DateTimeField(auto_now_add = True)
	updatedAt = models.DateTimeField(auto_now = True)
	
	def __str__(self):
		return str(self.name)

class DoctorSpeciality(models.Model):
	name = models.CharField(max_length = 255,null = True, blank = True)
	createdAt = models.DateTimeField(auto_now_add = True)
	updatedAt = models.DateTimeField(auto_now = True)
	
	def __str__(self):
		return str(self.name)

class TimeSlots(models.Model):
	timeslots = models.CharField(max_length = 100)
	availability = models.BooleanField(default=True)
	createdAt = models.DateTimeField(auto_now_add = True)
	updatedAt = models.DateTimeField(auto_now = True)


class DoctorList(models.Model):
	name = models.CharField(max_length = 255,null = True, blank = True)
	speciality = models.ForeignKey('DoctorSpeciality',on_delete = models.CASCADE,null = True,blank =True)
	experience = models.CharField(max_length = 255,null = True, blank = True)
	timeSlots = models.ManyToManyField(TimeSlots,null = True,blank =True)
	consultationFee = models.FloatField(default = 0.0)
	phone = models.CharField(max_length = 255,null = True, blank = True)
	address = models.CharField(max_length = 255,null = True, blank = True)
	uploadDocument = models.FileField(upload_to="media/uploads/", null = True, blank = True)
	createdAt = models.DateTimeField(auto_now_add = True)
	updatedAt = models.DateTimeField(auto_now = True)
	
	def __str__(self):
		return str(self.name)


class DoctorConsultancy(models.Model):
	user = models.ForeignKey('drugZoneUsers.CustomUser',on_delete = models.CASCADE,null = True,blank =True)
	symptom = models.ManyToManyField(Symptom, null = True, blank = True)
	doctor = models.ForeignKey('DoctorList',on_delete = models.CASCADE,null = True,blank =True)
	onDate = models.DateField()
	slot = models.ForeignKey('TimeSlots',on_delete = models.CASCADE,null = True,blank =True)
	createdAt = models.DateTimeField(auto_now_add = True)
	updatedAt = models.DateTimeField(auto_now = True)
	

	def __str__(self):
		return str(self.user)