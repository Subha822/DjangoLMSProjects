from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('customer', views.list_customers, name='list_customers'),
    path('create/', views.create_customer, name='create_customer'),
    path('update/<int:pk>/', views.update_customer, name='update_customer'),
    path('delete/<int:pk>/', views.delete_customer, name='delete_customer'),
]