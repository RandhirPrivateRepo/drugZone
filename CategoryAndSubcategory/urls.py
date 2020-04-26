from django.urls import path
from . import views

app_name = "CategoryAndSubCategory"

urlpatterns = [
    path('list_category/', views.category_list, name='category_list'),
    path('add_category/', views.category_add, name='category_add'),
    path('update_category/<int:pk>/', views.category_update, name='category_update'),


    path('list_subcategory/', views.subcategory_list, name='subcategory_list'),
    path('add_subcategory/', views.subcategory_add, name='subcategory_add'),
    path('update_subcategory/<int:pk>/', views.subcategory_update, name='subcategory_update'),



   
  
]
