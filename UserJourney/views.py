from django.shortcuts import render

# Create your views here.



def login_view(request):
	template_name = 'userjourney/login.html'

	context = {}

	return render(request, template_name, context)



def register_view(request):
	template_name = 'userjourney/register.html'

	context = {}

	return render(request, template_name, context)

