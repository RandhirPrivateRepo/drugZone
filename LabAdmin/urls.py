from django.urls import path
from . import views

app_name = "LabAdmin"

urlpatterns = [
    path('list/', views.list_view, name='list_view'),
    path('add/', views.add_lab_admin, name='add_lab_admin'),
]