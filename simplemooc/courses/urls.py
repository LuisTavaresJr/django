from django.contrib import admin
from django.urls import path
from .views import index, details, enrollment, announcements, undo_enrollment

urlpatterns = [
    path('', index, name='index'),
    #path('<int:pk>', details, name='details') #agrupamento de expreção regular
    path('<slug>/', details, name='details'),
    path('<slug>/inscricao/', enrollment, name='enrollment'),
    path('<slug>/anuncios/', announcements, name='announcements'),
    path('<slug>/cancelar-inscricao/', undo_enrollment, name='undo_enrollment'),
]