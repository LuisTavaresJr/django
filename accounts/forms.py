from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
import re

User = get_user_model() # chamando o User q o django reconhece como padrao (no caso o nosso criado)


class RegisterForm(forms.ModelForm):

    #email = forms.EmailField(label='E-mail') Esse campo email e desnecessario pois ja colocamos no fields
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmação de Senha', widget=forms.PasswordInput)

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('A confirmação não está correta')
        return password2

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.match('^[a-zA-Z0-9-@]*$', username):
            raise forms.ValidationError('O nome do usuário so pode conter letras, digitos ou os seguintes caracteres: @/./+/-/')
        return username

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

    class Meta: # no nosso formulario de registo so vamos usar o username e email
        model = User
        fields = ['username', 'email']


class EditAccountsForm(forms.ModelForm):

    # def clean_email(self):  # serve para validação do email (email único)
    #     email = self.cleaned_data['email']
    #     queryset = User.objects.filter(
    #         email=email).exclude(pk=self.instance.pk)
    #     if queryset.exists():
    #         raise forms.ValidationError('Já existe usuário com este E-mail.')
    #     return email
    # foi removido pq essa def era pra forçar nosso email ser unico, mas agora ele ja vem direto do model sendo unico
    class Meta:
        model = User
        fields = ['username', 'email', 'name']