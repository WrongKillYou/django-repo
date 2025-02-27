from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('', views.login, name='login'),
    path('student_dashboard/', views.student_dashboard, name='student_dashboard')
]