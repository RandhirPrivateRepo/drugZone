from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login
# from django.contrib.auth.models import User
from django.forms.utils import ErrorList
from django.contrib.auth import login as django_login, logout as django_logout, authenticate
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import traceback
from rest_framework.authtoken.models import Token

from drugZoneUsers.models import *
# from .forms import LoginModelForm

def LoginFormView(request):
	if request.method == 'GET':
		if request.user.is_authenticated:
			return redirect('dashbord')
		else:
			return render(request, 'login.html')

	if request.method == 'POST':
		email = request.POST.get('email')
		password = request.POST.get('password')
		if CustomUser.objects.filter(email=email).exists():
			user = CustomUser.objects.get(email=email)
			print (user)
			if user:
				if user.check_password(password):
					if user.is_superuser:
						outh_user = authenticate(username=email, password=password)
						django_login(request, outh_user)
						print (outh_user)
						if Token.objects.filter(user=outh_user).exists():
							token = Token.objects.get(user=outh_user)
						else:
							Token.objects.create(user=outh_user)
							token = Token.objects.get(user=outh_user)

						request.session['token'] = token.key
						return render(request, 'index.html')
					else:
						return render(request, 'login.html', {'error': 'User have no rights to login'})

				else:
					return render(request, 'login.html', {'error': 'incorrect username or password'})

			else:
				return render(request, 'login.html', {'error': 'incorrect username'})
		else:
			return render(request, 'login.html', {'error': 'User not exists.'})




@login_required(login_url='/')
def LogOutView(request):
    if request.method == 'GET':
        request.session.token = ''
        django_logout(request)
        return redirect('login')

@login_required(login_url='/')
def dashbord(request):
    if request.user.is_authenticated:
        # t = datetime.now()
        # incident = Incident.objects.filter(job_date_time__day=t.day).count()
        # crew = UserProfile.objects.filter(role='crew').count()
        # vehicle = Vehicle.objects.all().count()
        # data = {
        #     'incident': incident,
        #     'crew': crew,
        #     'vehicle': vehicle
        # }
        return render(request, 'index.html')
    else:
        return render(request, "login.html")


@login_required(login_url='/login')
def employeeList(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            users = CustomUser.objects.all()
            return render(request, 'employees.html', {'users':users})
    else:
        return render(request, "login.html")


@login_required(login_url='/login')
def employeeAdd(request):

    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, 'add-employee.html')
        else:
            return render(request, "login.html")
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        role = request.POST.get('role')
       
        # try:
        user = CustomUser.objects.filter(email=email)
        if user:
            return render(request, "add-employee.html", {"error": "User already exist with same email"})
        else:

            new_user = CustomUser.objects.create_user(
                email = email,
                password = password)

            userObj = CustomUser.objects.get(email=email)
            userObj.name = name
            userObj.role = role
            userObj.phone = phone
            userObj.is_staff = True
            # user.role = 3
            userObj.save()

            return redirect('employee-list')
            # else:
            #     return render(request, "add-employee.html", {"message": "user not added"})

        # except Exception as e:
        #     print(traceback.print_exc())
        #     return render(request, "error-404.html", {"message": "internal server error"})