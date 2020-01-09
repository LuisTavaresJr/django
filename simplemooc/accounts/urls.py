from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import register, dashboard, edit, edit_password, password_reset

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('entrar/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('sair/', LogoutView.as_view(next_page='core:home'), name='logout'),
    path('cadastre-se/', register, name='register'),
    path('nova-senha/', password_reset, name='password_reset'),
    path('editar/', edit, name='edit'),
    path('editar-senha', edit_password, name='edit_password')
]