from django.contrib import admin
from django.urls import path
from .views import index, details, enrollment, announcements

urlpatterns = [
    path('', index, name='index'),
    #path('<int:pk>', details, name='details') #agrupamento de expreção regular
    path('<slug>/', details, name='details'),
    path('<slug>/inscricao/', enrollment, name='enrollment'),
    path('<slug>/anuncios/', announcements, name='announcements'),
]