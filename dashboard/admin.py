from django.contrib import admin

# Register your models here.
from .models import *


admin.site.site_header = "DRUGZONE ADMIN" 
admin.site.site_title =  "DRUGZONE ADMIN" 
admin.site.site_url = False


class MedicineInline(admin.StackedInline):
    model = MedicineImage
    extra = 1

class ProductInline(admin.StackedInline):
    model = ProductImage
    extra = 1


class MedicineAdmin(admin.ModelAdmin):
	list_display = ('medicineName','category','subCategory','manufaturerName','actualPrice','quantity','rackNumber','selfNumber')
	inlines = [MedicineInline]

	def save_model(self, request, obj, form, change):
		obj.save()

		for afile in request.FILES.getlist('photos_multiple'):
			obj.photos.create(image=afile)

class ProductAdmin(admin.ModelAdmin):
	list_display = ('productName','category','subCategory','manufaturerName','actualPrice','quantity','rackNumber','selfNumber')	
    
	inlines = [ProductInline]

	def save_model(self, request, obj, form, change):
		obj.save()

		for afile in request.FILES.getlist('photos_multiple'):
			obj.photos.create(image=afile)

admin.site.register(Medicine, MedicineAdmin)
admin.site.register(Product, ProductAdmin)

admin.site.register(Categorie)
admin.site.register(SubCategorie)
admin.site.register(Manufacturer)