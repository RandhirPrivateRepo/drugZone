from django.shortcuts import render

from .models import *
from django.shortcuts import redirect




def dashboard_view(request):
    if request.user.is_authenticated:
    	template_name = 'dashboard/index.html'
    	context = {}
    	return render(request, template_name, context)
    else:
        template_name = 'userJourney/login.html'
        context = {}
        return render(request, template_name, context)


def test_add_view(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, 'Labtest/add_test.html')
        else:
            return render(request, 'userjourney/login.html')
    
    if request.method == 'POST':
        name = request.POST.get('name')
        # try:
        testObj = Test.objects.filter(name=name)
        if testObj:
            return render(request, 'Labtest/add_test.html', {"error": "Test already exist with same name"})
        else:

            new_test = Test.objects.create(
                name = name
            ) 
            return render(request, 'Labtest/add_test.html', {"success": "Test Created Successfully"})
            
def test_list_view(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            tests = Test.objects.all()
            return render(request, 'Labtest/test_list.html', {'tests':tests})
    else:
        return render(request, 'userjourney/login.html')



def sample_add_view(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, 'Labtest/add_sample.html')
        else:
            return render(request, 'userjourney/login.html')
    
    if request.method == 'POST':
        name = request.POST.get('name')
        # try:
        testObj = sample.objects.filter(name=name)
        if testObj:
            return render(request, 'Labtest/add_sample.html', {"error": "Sample already exist with same name"})
        else:

            new_test = sample.objects.create(
                name = name
            ) 
            return render(request, 'Labtest/add_sample.html', {"success": "Sample Created Successfully"})
            
def sample_list_view(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            samples = sample.objects.all()
            return render(request, 'Labtest/sample_list.html', {'samples':samples})
    else:
        return render(request, 'userjourney/login.html')



def labtest_add_view(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            samples = sample.objects.all()
            tests = Test.objects.all()
            return render(request, 'Labtest/add_labtest.html' , {'samples':samples,'tests':tests})
        else:
            return render(request, 'userjourney/login.html')
    
    if request.method == 'POST':
        name = request.POST.get('name')
        actualPrice = request.POST.get('actualPrice')
        discountedPrice =request.POST.get('discountedPrice')
        image = request.FILES.get('image')
        testDescription = request.POST.get('testDescription')
        testIncluded = request.POST.getlist('testIncluded') 
        testRequirements = request.POST.getlist('testRequirements')

        testObj = LabTest.objects.filter(name=name)
        if testObj:
            return render(request, 'Labtest/add_labtest.html', {"error": "LabTest already exist with same name"})
        else:

            new_test = LabTest.objects.create(
                name = name,
                actualPrice = actualPrice,
                discountedPrice = discountedPrice,
                image = image,
                testDescription = testDescription
                
            ) 

            labObj = LabTest.objects.get(name = name)


            for obj in testIncluded:
                if Test.objects.filter(id=obj):
            	    obj1 = Test.objects.get(id=obj)
            	    labObj.testIncluded.add(obj1)
            	    labObj.save()

            for obj in testRequirements:
                if sample.objects.filter(id=obj):
        	        obj1 = sample.objects.get(id=obj)
        	        labObj.testRequirements.add(obj1)
        	        labObj.save()


            return render(request, 'Labtest/add_labtest.html', {"success": "LabTest Created Successfully"})
            
def labtest_list_view(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            labtests = LabTest.objects.all()
            return render(request, 'Labtest/labtest_list.html', {'labtests':labtests})
    else:
        return render(request, 'userjourney/login.html')