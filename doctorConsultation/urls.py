from django.urls import path
from . import views

app_name = "DoctorConsultation"

urlpatterns = [
    
   
    path('symptom-add/', views.symptom_add_view, name='symptom_add_view'),
    path('symptom-list/', views.symptom_list_view, name='symptom_list_view'),

    path('speciality-add/', views.speciality_add_view, name='speciality_add_view'),
    path('speciality-list/', views.speciality_list_view, name='speciality_list_view'),

    path('doctor-add/', views.doctor_add_view, name='doctor_add_view'),
    path('doctor-list/', views.doctor_list_view, name='doctor_list_view'),

]
