from django.db import models
from CategoryAndSubcategory.models import *
# Create your models here.


class Manufacturer(models.Model):
	manufaturerName = models.CharField(max_length = 255, null = True, blank = True, verbose_name = 'Manufacturer Name')

	def __str__(self):
		return str(self.manufaturerName)



class MedicineImage(models.Model):
    image = models.ImageField(upload_to="media/uploads/")


class Medicine(models.Model):
	medicineName = models.CharField(max_length = 255, null = True, blank = True, verbose_name = 'Medicine Name')
	category = models.ForeignKey(Category, on_delete = models.CASCADE ,null = True, blank = True, verbose_name ='Category')
	subCategory = models.ForeignKey(SubCategory, on_delete = models.CASCADE ,null = True, blank = True, verbose_name = 'Sub Category')
	manufaturerName = models.ForeignKey(Manufacturer, on_delete = models.CASCADE ,null = True, blank = True, verbose_name = 'Manufacturer')
	quantity = models.IntegerField(default=0, verbose_name = 'Quantity')
	decsription = models.TextField(null = True, blank = True , verbose_name = 'Medicine Description')
	batchNumber = models.CharField(max_length = 255, null = True, blank = True , verbose_name = 'Batch No.')
	expiryDate = models.DateField(null = True, blank = True, verbose_name = 'Expiry-Date' )
	actualPrice = models.FloatField(default = 0.0, verbose_name = 'Actual Price (MRP)')
	discountedPrice = models.FloatField(default = 0.0,verbose_name = 'Price After Discount')
	gstTax = models.IntegerField(default = 0, verbose_name = 'GST/Other Tax')
	rackNumber = models.CharField(max_length = 255, null = True, blank = True, verbose_name = 'Rack-Number')
	selfNumber = models.CharField(max_length = 255, null = True, blank = True, verbose_name = 'Self-Number')
	remarks = models.TextField(null = True, blank = True, verbose_name = 'Remarks')
	images = models.ManyToManyField(MedicineImage)

	def __str__(self):
		return str(self.medicineName)