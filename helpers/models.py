from django.db import models

# Create your models here.


BANNER_TYPE= (
		('HomePage', 'HomePage'),
        ('TestPage', 'TestPage'))


class PaymentDetails(models.Model):
	mrpTotal = models.FloatField(default = 0.0)
	aditionalDiscount = models.FloatField(default = 0.0)
	sampleCollectionCharges = models.FloatField(default = 0.0)
	deliveryCharges = models.FloatField(default = 0.0)
	totalAmount = models.FloatField(default = 0.0)
	totalSavings = models.FloatField(default = 0.0)
	minimunAmount = models.FloatField(default = 0.0)

	def __str__(self):
		return str(self.totalAmount)


class PromoCode(models.Model):
	code = models.CharField(max_length = 100, null = True, blank = True)
	description = models.CharField(max_length = 100, null = True, blank = True)
	maxUsagePerUser = models.IntegerField(default=0)

	def __str__(self):
		return str(self.code)


class BannerImages(models.Model):
	bannerImage = models.FileField(upload_to="media/uploads/", null = True, blank = True)
	bannerDescription = models.TextField(null=True,blank=True)
	bannerType = models.CharField(max_length = 10, choices = BANNER_TYPE, null = True, blank = True)
	createdAt = models.DateTimeField(auto_now_add = True)
	updatedAt = models.DateTimeField(auto_now = True)
	

	def __str__(self):
		return str(self.bannerType)