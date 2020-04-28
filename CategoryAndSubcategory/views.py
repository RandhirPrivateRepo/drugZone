from django.shortcuts import render

from CategoryAndSubcategory.models import *
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
# Create your views here.



@login_required(login_url='UserJourney:login_view')
def category_list(request):
   template_name = 'CategoryAndSubcategory/category_list.html'
   context = {}

   categoryObjs = Category.objects.all()
   context['categoryObjs'] = categoryObjs

   return render(request, template_name, context)


@login_required(login_url='UserJourney:login_view')
def category_add(request):
	template_name = 'CategoryAndSubcategory/category_add.html'
	context = {}

	if request.method == 'POST':
		category_name = request.POST.get('category_name')
		category_description = request.POST.get('category_description')
		category_status = request.POST.get('category_status')

		if category_status == "true":
			category_status = True
		else:
			category_status = False

		if not category_name:
			context['error'] = "Please provide Category Name."
			return render(request, template_name, context)

		if Category.objects.filter(categoryName = category_name).exists():
			context['error'] = "Category with this name is already exists."
			return render(request, template_name, context)


		Category.objects.create(
		categoryName = category_name,
		description = category_description,
		status = category_status)

		context['success'] = "Category is Added."

		return render(request, template_name, context)

	return render(request, template_name, context)



@login_required(login_url='UserJourney:login_view')
def category_update(request, pk):
	template_name = 'CategoryAndSubcategory/category_update.html'
	context = {}
	categoryObj = Category.objects.get(pk = pk)

	context['categoryObj'] = categoryObj
	if request.method == 'POST':
		category_name = request.POST.get('category_name')
		category_description = request.POST.get('category_description')
		category_status = request.POST.get('category_status')

		print(category_description)

		if category_status == "true":
			category_status = True
		else:
			category_status = False

		if not category_name:
			context['error'] = "Please provide Category Name."
			return render(request, template_name, context)

		

		categoryObj.categoryName = category_name
		categoryObj.description = category_description
		categoryObj.status = category_status

		categoryObj.save()


		return redirect('CategoryAndSubCategory:category_list')

	return render(request, template_name, context)





@login_required(login_url='UserJourney:login_view')
def subcategory_list(request):
   template_name = 'CategoryAndSubcategory/subCategory_list.html'
   context = {}

   subcategoryObjs = SubCategory.objects.all()
   context['subcategoryObjs'] = subcategoryObjs

   return render(request, template_name, context)
   

@login_required(login_url='UserJourney:login_view')
def subcategory_add(request):
	template_name = 'CategoryAndSubcategory/subCategory_add.html'
	context = {}

	categories = Category.objects.filter(status = True)
	context['categories'] = categories


	if request.method == "POST":
		subcategory_name = request.POST.get('subcategory_name')
		subcategory_description = request.POST.get('subcategory_description')
		subcategory_categoryid = request.POST.get('subcategory_categoryid')

		if not subcategory_name:
			context['error'] = "Please provide SubCategory Name."
			return render(request, template_name, context)

		if SubCategory.objects.filter(subCategoryName = subcategory_name).exists():
			context['error'] = "SubCategory with this name is already exists."
			return render(request, template_name, context)


		categoryObj = Category.objects.get(pk = subcategory_categoryid)

		SubCategory.objects.create(
		subCategoryName = subcategory_name,
		category = categoryObj,
		description = subcategory_description
		)

		context['success'] = "SubCategory is Added."

		return render(request, template_name, context)	

	return render(request, template_name, context)




@login_required(login_url='UserJourney:login_view')
def subcategory_update(request, pk):
	template_name = 'CategoryAndSubcategory/subCategory_update.html'
	context = {}
	subcategoryObj = SubCategory.objects.get(pk = pk)
	categories = Category.objects.filter(status = True)
	context['categories'] = categories

	context['subcategoryObj'] = subcategoryObj


	if request.method == "POST":
		subcategory_name = request.POST.get('subcategory_name')
		subcategory_description = request.POST.get('subcategory_description')
		subcategory_categoryid = request.POST.get('subcategory_categoryid')

		if not subcategory_name:
			context['error'] = "Please provide SubCategory Name."
			return render(request, template_name, context)

		categoryObj = Category.objects.get(pk = subcategory_categoryid)

		subcategoryObj.subCategoryName = subcategory_name
		subcategoryObj.category = categoryObj
		subcategoryObj.description = subcategory_description
		subcategoryObj.save()

		return redirect('CategoryAndSubCategory:subcategory_list')


	

	return render(request, template_name, context)


