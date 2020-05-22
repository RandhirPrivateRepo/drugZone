from django.shortcuts import render

# Create your views here.
from .models import *
from django.shortcuts import redirect


def symptom_add_view(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, 'doctorConsultation/add_symptom.html')
        else:
            return render(request, 'userjourney/login.html')
    
    if request.method == 'POST':
        name = request.POST.get('name')

        testObj = Symptom.objects.filter(name=name)
        
        if testObj:
            return render(request, 'doctorConsultation/add_symptom.html', {"error": "Symptom already exist with same name"})
        else:

            new_test = Symptom.objects.create(
                name = name
            ) 
            return render(request, 'doctorConsultation/add_symptom.html', {"success": "Symptom created."})
            
def symptom_list_view(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            symtoms = Symptom.objects.all()
            return render(request, 'doctorConsultation/symptom_list.html', {'symtoms':symtoms})
    else:
        return render(request, 'userjourney/login.html')





def speciality_add_view(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, 'doctorConsultation/add_speciality.html')
        else:
            return render(request, 'userjourney/login.html')
    
    if request.method == 'POST':
        name = request.POST.get('name')
        # try:
        testObj = DoctorSpeciality.objects.filter(name=name)
        if testObj:
            return render(request, 'doctorConsultation/add_speciality.html', {"error": "Department already exist with same name"})
        else:

            new_test = DoctorSpeciality.objects.create(
                name = name
            ) 
            return render(request, 'doctorConsultation/add_speciality.html', {"success": "Department Created"})
            
def speciality_list_view(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            specObj = DoctorSpeciality.objects.all()
            return render(request, 'doctorConsultation/speciality_list.html', {'specObj':specObj})
    else:
        return render(request, 'userjourney/login.html')




def doctor_add_view(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            times = TimeSlots.objects.all()
            specObj = DoctorSpeciality.objects.all()
            return render(request, 'doctorConsultation/add_doctor.html' , {'times':times,'specObj':specObj})
        else:
            return render(request, 'userjourney/login.html')
    
    if request.method == 'POST':
        name = request.POST.get('name')
        speciality = request.POST.get('speciality')
        experience = request.POST.get('experience')
        timeSlots = request.POST.getlist('timeSlots')
        consultationFee = request.POST.get('consultationFee')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        uploadDocument = request.FILES.get('uploadDocument')

        docObj = DoctorList.objects.filter(name=name)
        if docObj:
            return render(request, 'doctorConsultation/add_doctor.html', {"error": "Doctor already exist with same name"})
        else:

            new_test = DoctorList.objects.create(
                name = name,
                experience = experience,
                consultationFee = consultationFee,
                phone = phone,
                address = address,
                uploadDocument = uploadDocument
            ) 

            docObj = DoctorList.objects.get(name = name)


            
            if DoctorSpeciality.objects.filter(id=speciality):
        	    obj1 = DoctorSpeciality.objects.get(id=speciality)
        	    docObj.speciality = obj1
        	    docObj.save()

            for obj in timeSlots:
                if TimeSlots.objects.filter(id=obj):
        	        obj1 = TimeSlots.objects.get(id=obj)
        	        docObj.timeSlots.add(obj1)
        	        docObj.save()


            return render(request, 'doctorConsultation/add_doctor.html', {"success": "Doctor Added Successfully"})
            
def doctor_list_view(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            doctors = DoctorList.objects.all()
            return render(request, 'doctorConsultation/doctor_list.html', {'doctors':doctors})
    else:
        return render(request, 'userjourney/login.html')