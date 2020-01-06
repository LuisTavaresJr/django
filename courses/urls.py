from django.contrib import admin
from django.urls import path
from .views import index, details

urlpatterns = [
    path('', index, name='index'),
    #path('<int:pk>', details, name='details') #agrupamento de expreção regular
    path('<slug>/', details, name='details'),

]