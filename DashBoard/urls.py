from django.urls import path
from .views import *
from . import views

app_name = "DashboardApp"

urlpatterns = [
    path('index/', views.dashboard_view, name='dashboard__index_view'),
   
    path('test-add/', views.test_add_view, name='dashboard__test_add_view'),
    path('test-list/', views.test_list_view, name='dashboard__test_list_view'),

    path('sample-add/', views.sample_add_view, name='dashboard__sample_add_view'),
    path('sample-list/', views.sample_list_view, name='dashboard__sample_list_view'),

    path('labtest-add/', views.labtest_add_view, name='dashboard__labtest_add_view'),
    path('labtest-list/', views.labtest_list_view, name='dashboard__labtest_list_view'),

    path('lab-add/', views.labs_add_view, name='dashboard__labs_add_view'),
    path('lab-list/', views.labs_list_view, name='dashboard__labs_list_view'),

    path('banner-add/', views.banner_add_view, name='dashboard__banner_add_view'),
    path('banner-list/', views.banner_list_view, name='dashboard__banner_list_view'),

    #---------------------------------REST URLS-----------------------------------__#

    path('labtests/', LabTestAPIView.as_view()),
    path('labtests/<int:testid>/', LabTestDetailAPIView.as_view()),
    path('bannerimages/', BannerImagesAPI.as_view()),

]
