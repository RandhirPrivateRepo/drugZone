from django.shortcuts import render


# Create your views here.
from django.contrib.auth import authenticate, login
# from django.contrib.auth.models import User
from django.forms.utils import ErrorList
from django.contrib.auth import login as django_login, logout as django_logout, authenticate
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
import traceback
from rest_framework.authtoken.models import Token

from drugZoneUsers.models import *



def login_view(request):
	
	template_name = 'userjourney/login.html'

	if request.method == 'GET':
		if request.user.is_authenticated:
			return redirect('DashboardApp:dashboard__index_view')
		else:
			return render(request, template_name)

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
						return redirect('DashboardApp:dashboard__index_view')
					else:
						return render(request, template_name, {'error': 'User have no rights to login'})

				else:
					return render(request, template_name, {'error': 'incorrect username or password'})

			else:
				return render(request, template_name, {'error': 'incorrect username'})
		else:
			return render(request, template_name, {'error': 'User not exists.'})

def logout_view(request):
    if request.method == 'GET':
        request.session.token = ''
        django_logout(request)
        return redirect('UserJourney:login_view')




def list_view(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            users = CustomUser.objects.all()
            return render(request, 'employee/employee_list.html', {'users':users})
    else:
        return render(request, 'userjourney/login.html')


def add_view(request):

    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, 'employee/addemployee.html')
        else:
            return render(request, 'userjourney/login.html')
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        role = request.POST.get('role')
        uploadDocument = request.FILES.get('uploadDocument')
        print (role)
        # try:
        user = CustomUser.objects.filter(email=email)
        if user:
            return render(request, 'employee/addemployee.html', {"error": "User already exist with same email"})
        else:

            new_user = CustomUser.objects.create_user(
                email = email,
                password = password)

            userObj = CustomUser.objects.get(email=email)
            userObj.name = name
            userObj.role = role
            userObj.uploadDocument = uploadDocument
            userObj.phone = phone
            userObj.is_staff = True
            # user.role = 3
            userObj.save()

            return redirect('UserJourney:list_view')
            