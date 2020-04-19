from django.urls import path
from . import views

app_name = "DashboardApp"

urlpatterns = [
    path('index/', views.dashboard_view, name='dashboard__index_view'),
]