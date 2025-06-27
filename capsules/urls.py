from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create-capsule/', views.create_capsule, name='create_capsule')
]
