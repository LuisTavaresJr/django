from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .forms import RegisterForm, EditAccountsForm

@login_required # verifica antes se o usuario esta logado pra dar permissao a acesar o painel(dashboard)
def dashboard(request):
    template_name = 'accounts/dashboard.html'
    return render(request, template_name)


def register(request):
    template_name = 'accounts/register.html'
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(
                username=user.username, password=form.cleaned_data['password1']
            )
            login(request, user) # essa view é responsavel por fazer o login do usuario
            return redirect('core:home')
    else:
        form = RegisterForm()
    context = {
        'form': form
    }
    return render(request, template_name, context)

@login_required
def edit(request):
    template_name = 'accounts/edit.html'
    context = {}
    if request.method == 'POST':
        form = EditAccountsForm(request.POST, instance=request.user) # a instacia q esta sendo alterada
        if form.is_valid():
            form.save()
            form = EditAccountsForm(instance=request.user) # formulario vazio
            context['success'] = True # apenas para fazer um if no html
    else:
        form = EditAccountsForm(instance=request.user)
    context['form'] = form
    return render(request, template_name, context)

@login_required
def edit_password(request):
    template_name = 'accounts/edit_password.html'
    context = {}
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user) # como nao sabe a ordem do palametros,ja foi passado de forma nomeada
        if form.is_valid():
            form.save()
            context['success'] = True
    else:
        form = PasswordChangeForm(user=request.user)
    context['form'] = form
    return render(request, template_name, context)