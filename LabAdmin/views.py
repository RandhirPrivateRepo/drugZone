from django.shortcuts import render

# Create your views here.
def list_view(request):
	template_name = 'labadmin/list.html'

	context = {}

	return render(request, template_name, context)


def add_lab_admin(request):
	template_name = 'labadmin/addlabadmin.html'

	context = {}

	return render(request, template_name, context)


