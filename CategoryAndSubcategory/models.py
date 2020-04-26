from django.db import models

# Create your models here.

class Category(models.Model):
	categoryName = models.CharField(max_length = 100, null = True, blank = True, verbose_name = 'Category Name')
	description = models.TextField(null = True, blank = True)
	status = models.BooleanField(default = True)

	createdAt = models.DateTimeField(auto_now_add = True,null = True, blank = True)
	updatedAt = models.DateTimeField(auto_now = True, null = True, blank = True)
	

	
	def __str__(self):
		return str(self.categoryName)


class SubCategory(models.Model):
	category = models.ForeignKey(Category, on_delete = models.CASCADE)
	subCategoryName = models.CharField(max_length = 100, null = True, blank = True, verbose_name = 'Sub Category Name')
	description = models.TextField(null = True, blank = True)

	createdAt = models.DateTimeField(auto_now_add = True,null = True, blank = True)
	updatedAt = models.DateTimeField(auto_now = True, null = True, blank = True)
	
	
	def __str__(self):
		return str(self.subCategoryName)