from django.shortcuts import render



def dashboard_view(request):
	template_name = 'dashboard/index.html'

	context = {}

	return render(request, template_name, context)


