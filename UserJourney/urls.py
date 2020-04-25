from django.urls import path
from . import views

app_name = "UserJourney"


urlpatterns = [
    path('', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),

    path('employee-add', views.add_view, name='add_view'),
    path('employee-list', views.list_view, name='list_view'),

]



