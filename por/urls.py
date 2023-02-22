from django.urls import path
from . import views

urlpatterns = [
    path('', views.team_name, name='team_name'),
    path('<str:team_name>/', views.data, name='data'),
    path('test/', views.test, name='test'),
]
