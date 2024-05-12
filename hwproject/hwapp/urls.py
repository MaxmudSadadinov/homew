from django.urls import path
from . import views

urlpatterns = [
path('about/', views.about_me, name='about'),
path('main/', views.main, name='main')
]