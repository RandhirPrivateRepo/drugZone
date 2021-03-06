"""drugzone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
	path('jet/', include('jet.urls', 'jet')),
	path('api/v1/user/', include('drugZoneUsers.urls')),    
    path('admin/', admin.site.urls),
    path('', include('UserJourney.urls')),
    path('dashboard/', include('DashBoard.urls')),
    path('labadmin/', include('LabAdmin.urls')),
    path('categorysubcategory/', include('CategoryAndSubcategory.urls')),
    path('medicines/', include('Medicines.urls')),
    path('consultation/', include('doctorConsultation.urls')),
    path('prescriptions/', include('prescription.urls')),


    # path('admin/internal/', admin.site.urls),prescription

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
