
from django.shortcuts import render

from CategoryAndSubcategory.models import *
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import *

from datetime import datetime



def list_medicine(request):
	template_name = 'medicines/medicine_list.html'
	context = {}

	medicinesObjs = Medicine.objects.all()
	context['medicinesObjs'] = medicinesObjs

	return render(request, template_name, context)






def add_medicies(request):
	template_name = 'medicines/medicine_add.html'
	context = {}

	categoryObjs = Category.objects.all()
	context['categoryObjs'] = categoryObjs


	subcategoryObjs = SubCategory.objects.all()
	context['subcategoryObjs'] = subcategoryObjs

	manufaturerObjs = Manufacturer.objects.all()
	context['manufaturerObjs'] = manufaturerObjs



	if request.method == 'POST':
		medicinename = request.POST.get('medicinename')
		categoryid = request.POST.get('categoryid')
		subcategoryid = request.POST.get('subcategoryid')
		manufacturerid = request.POST.get('manufacturerid')
		quantity = request.POST.get('quantity')
		decsription = request.POST.get('decsription')
		batchnumber = request.POST.get('batchnumber')
		expiraydate = request.POST.get('expiraydate')
		actualprice = request.POST.get('actualprice')
		discountedprice = request.POST.get('discountedprice')
		gsttax = request.POST.get('gsttax')
		racknumber = request.POST.get('racknumber')
		shelfnumber = request.POST.get('shelfnumber')
		remark = request.POST.get('remark')
		image = request.FILES.get('image')


		if not medicinename:
			context['error'] = "Please provide Medicine Name."
			return render(request, template_name, context)

		if expiraydate:

			datetimeobject = datetime.strptime(expiraydate,'%d/%m/%Y')
		

			newformat = datetimeobject.strftime('%Y-%m-%d')
		else:
			newformat = None


		if categoryid:
			categoryObj = Category.objects.get(pk = categoryid)

		if subcategoryid:
			subcategoryObj = SubCategory.objects.get(pk = subcategoryid)

		if manufacturerid:
			manufaturerObj = Manufacturer.objects.get(pk = manufacturerid)




		medicineObj = Medicine.objects.create(
			medicineName = medicinename,
			category = categoryObj,
			subCategory = subcategoryObj,
			manufaturerName = manufaturerObj,
			quantity = quantity,
			decsription = decsription,
			batchNumber = batchnumber,
			expiryDate = newformat,
			actualPrice = actualprice,
			discountedPrice = discountedprice,
			gstTax = gsttax,
			rackNumber = racknumber,
			selfNumber = shelfnumber,
			remarks = remark)


		
		if image:
			medicineimageObj =  MedicineImage.objects.create(
				image =  image)
			medicineObj.images.add(medicineimageObj)

			medicineObj.save()

		context['success'] = "Medicine is Added."

		return render(request, template_name, context)


	return render(request, template_name, context)



def add_manufacturer(request):
	template_name = 'medicines/add_manufacture.html'
	context = {}
	if request.method == 'POST':
		mName = request.POST.get('mName')

		
		if not mName:
			context['error'] = "Please provide Manufacturer Name."
			return render(request, template_name, context)

		if Manufacturer.objects.filter(manufaturerName = mName).exists():
			context['error'] = "Manufacturer with this name is already exists."
			return render(request, template_name, context)


		Manufacturer.objects.create(
		manufaturerName = mName)

		context['success'] = "Manufacturer is Added."

		return render(request, template_name, context)

	return render(request, template_name, context)
