from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.list, name='list'),
    path('view/<int:pk>/', views.view, name='view'),
    path('write/', views.write, name='write'),
    path('edit/<int:pk>/', views.edit, name='edit'),
]