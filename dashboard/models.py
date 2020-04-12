from django.db import models

# Create your models here.

class Categorie(models.Model):
	categoryName = models.CharField(max_length = 100, null = True, blank = True, verbose_name = 'Category Name')
	
	def __str__(self):
		return str(self.categoryName)


class SubCategorie(models.Model):
	category = models.ForeignKey(Categorie, on_delete = models.CASCADE)
	subCategoryName = models.CharField(max_length = 100, null = True, blank = True, verbose_name = 'Sub Category Name')
	
	def __str__(self):
		return str(self.subCategoryName)


class Manufacturer(models.Model):
	manufaturerName = models.CharField(max_length = 255, null = True, blank = True, verbose_name = 'Manufacturer Name')

	def __str__(self):
		return str(self.manufaturerName)



class Medicine(models.Model):
	medicineName = models.CharField(max_length = 255, null = True, blank = True, verbose_name = 'Medicine Name')
	category = models.ForeignKey(Categorie, on_delete = models.CASCADE ,null = True, blank = True, verbose_name ='Category')
	subCategory = models.ForeignKey(SubCategorie, on_delete = models.CASCADE ,null = True, blank = True, verbose_name = 'Sub Category')
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

	def __str__(self):
		return str(self.medicineName)



class Product(models.Model):
	productName = models.CharField(max_length = 255, null = True, blank = True , verbose_name = 'Product Name')
	category = models.ForeignKey(Categorie, on_delete = models.CASCADE , null = True, blank = True,verbose_name ='Category')
	subCategory = models.ForeignKey(SubCategorie, on_delete = models.CASCADE ,null = True, blank = True, verbose_name = 'Sub Category')
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

	def __str__(self):
		return str(self.productName)

class MedicineImage(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete = models.CASCADE,related_name='medicieneImages')
    image = models.ImageField(upload_to="media/uploads/")

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE,related_name='productImages')
    image = models.ImageField(upload_to="media/uploads/")
