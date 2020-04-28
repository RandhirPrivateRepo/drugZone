from django.urls import path
from . import views

app_name = "Prescription"

urlpatterns = [
    
   
    path('prescription-list/', views.prescription_list_view, name='prescription_list_view'),

   

]
