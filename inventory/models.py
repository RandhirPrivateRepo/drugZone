# from django.db import models

# # Create your models here.
# from CategoryAndSubcategory.models import *
# from Medicines.models import Medicine

# class Inventory(models.Model):
# 	category = models.ForeignKey('CategoryAndSubcategory.Category', on_delete = models.CASCADE ,null = True, blank = True)
# 	subCategory = models.ForeignKey('CategoryAndSubcategory.SubCategory', on_delete = models.CASCADE ,null = True, blank = True)
# 	itemName =   models.ForeignKey('Medicines.Medicine', on_delete = models.CASCADE ,null = True, blank = True)
# 	serialNumber =  models.CharField(max_length = 255, null = True, blank = True)
# 	batchNumber 
# 	shelfNumber 
# 	rackNumber 
# 	quantity 
# 	costToCompany
# 	remarks