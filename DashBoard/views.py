from django.shortcuts import render

from .models import *
from doctorConsultation.models import DoctorList
from django.shortcuts import redirect

from .serializers import * 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import traceback

from helpers.models import BannerImages

from helpers.serializers import BannerImagesSerializer





def dashboard_view(request):
    if request.user.is_authenticated:
        template_name = 'dashboard/index.html'
        doctors = DoctorList.objects.all()[:6]
        return render(request, template_name, {'doctors':doctors})
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


#---------------------------------------------------------------------- REST APIS FOR LABTEST ---------------------------------------------------------------------------------#

class BannerImagesAPI(APIView):

    def get(self,request):
        user = request.user
        try:
            if not self.request.query_params.get('type'):
                return Response({"Error":"please define type"},status=status.HTTP_400_BAD_REQUEST)

            if self.request.query_params.get('type') == 'HomePage':
                objs = BannerImages.objects.filter(bannerType = 'HomePage')
                serialized = BannerImagesSerializer(objs, many=True, context = {'request': request})
            elif self.request.query_params.get('type') == 'TestPage':
                objs = BannerImages.objects.filter(bannerType = 'TestPage')
                serialized = BannerImagesSerializer(objs, many=True, context = {'request': request})

            return Response(serialized.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"Error":str(e)},status=status.HTTP_400_BAD_REQUEST)

class LabTestAPIView(APIView):

    def get(self,request):
        user = request.user
        try:
            if self.request.query_params.get('popular') == 'True':
                objs = LabTest.objects.filter(popularTest=True)

            if self.request.query_params.get('package') == 'True':
                objs = LabTest.objects.filter(packageOrSingle='Package')

            if self.request.query_params.get('testtype') == 'pathology':
                objs = LabTest.objects.filter(testType='Pathology')

            if self.request.query_params.get('testtype') == 'radiology':
                objs = LabTest.objects.filter(testType='Radiology')
            
            if not self.request.query_params:
                objs = LabTest.objects.all()
            
            serialized = LabTestSerializer(objs, many=True, context = {'request': request})
            return Response(serialized.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"Error":str(e)},status=status.HTTP_400_BAD_REQUEST)



class LabTestDetailAPIView(APIView):

    def get(self,request,testid):
        user = request.user
        try:
            objs = LabTest.objects.get(id=testid)
            serialized = LabTestSerializer(objs, context = {'request': request})
            return Response(serialized.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"Error":str(e)},status=status.HTTP_400_BAD_REQUEST)

