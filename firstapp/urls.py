from django.contrib import admin
from django.urls import path

from .views import about, components, contact, index, project, services

urlpatterns = [
    path('about/',about,name='about'),
    path('components/',components,name='components'),
    path('contact/',contact,name='contact'),
    path('index/',index ,name='index'),
    path('project/',project,name='project'),
    path('',services,name='services'),

]
