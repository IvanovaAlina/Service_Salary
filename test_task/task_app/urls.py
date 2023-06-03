from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('salary_list/', views.salary_list, name='salary_list'),
    path('new_salary/', views.new_salary, name='new_salary'),
    path('delete_salary/<int:salary_id>/', views.delete_salary, name='delete_salary'),
    path('verify_email/', views.verify_email, name='verify_email'),
    path('send_mail_for_verify/', views.send_mail_for_verify, name='send_mail_for_verify'),
    path('verify_code/', views.verify_code, name='verify_code'),
]