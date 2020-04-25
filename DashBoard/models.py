from django.db import models

# Create your models here.

class Test(models.Model):
	name = models.CharField(max_length = 255,null = True, blank = True)
	createdAt = models.DateTimeField(auto_now_add = True)
	updatedAt = models.DateTimeField(auto_now = True)
	
	def __str__(self):
		return str(self.name)

class sample(models.Model):
	name = models.CharField(max_length = 255,null = True, blank = True)
	createdAt = models.DateTimeField(auto_now_add = True)
	updatedAt = models.DateTimeField(auto_now = True)
	
	def __str__(self):
		return str(self.name)

class LabTest(models.Model):
	name = models.CharField(max_length = 255, verbose_name = 'Name')
	actualPrice = models.FloatField(default = 0.0, verbose_name = 'Actual Price (MRP)')
	discountedPrice = models.FloatField(default = 0.0,verbose_name = 'Price After Discount')
	image = models.FileField(upload_to="media/uploads/", null = True, blank = True)
	testDescription = models.CharField(max_length = 255, null = True, blank = True)
	testIncluded = models.ManyToManyField(Test, null = True, blank = True)
	testRequirements = models.ManyToManyField(sample, null = True, blank = True)
	createdAt = models.DateTimeField(auto_now_add = True)
	updatedAt = models.DateTimeField(auto_now = True)
	

	def __str__(self):
		return str(self.name)