from django.urls import path
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
]
