from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager


class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField('Nome de Usuário', max_length=30, unique=True)
    email = models.EmailField('E-mail', unique=True) # agora temos um email unico
    name = models.CharField('Nome', max_length=100, blank=True)
    is_active = models.BooleanField('Está ativo?', blank=True, default=True)# um boleando pra saber se o usario esta ativo, e se pode ou nao logar
    is_staff = models.BooleanField('É da equipe?', blank=True, default=False)# é para o django saber se ele pode acessar a area adm
    date_joined = models.DateTimeField('Data de Entrada', auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.name or self.username

    def get_short_name(self): # pra um melhor fucionamento do django
        return self.username

    def get_full_name(self):
        return str(self)

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'