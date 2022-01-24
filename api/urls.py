from django import views
from django.contrib import admin
from django.urls import include, path
from . import views 


urlpatterns = [
    path('login/',views.Login.as_view()),
    path('create/',views.Register.as_view()),
    path('propietario_create/',views.OwnerCreate.as_view()),
    path('propietario_list/',views.OwnerList.as_view()),
    path('propiedades_create/',views.PropertiesCreate.as_view()),
    path('propiedades_list/',views.PropertiesList.as_view()),
    
    
]