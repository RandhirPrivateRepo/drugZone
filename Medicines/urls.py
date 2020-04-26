from django.urls import path
from . import views

app_name = "Medicine"

urlpatterns = [
    path('list/', views.list_medicine, name='list_medicine'),
    path('add/', views.add_medicies, name='add_medicies'),
    path('add/manufacturer/', views.add_manufacturer, name='add_manufacturer'),

   


   
  
]
