from django.shortcuts import render

# Create your views here.
from .models import *
from django.shortcuts import redirect

            
def prescription_list_view(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            objs = UploadPrescription.objects.all()
            return render(request, 'prescription/prescription_list.html', {'objs':objs})
    else:
        return render(request, 'userjourney/login.html')