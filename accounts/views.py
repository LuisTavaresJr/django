from django.shortcuts import render, redirect
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
    form = EditAccountsForm()
    context = {}
    context['form'] = form
    return render(request, template_name, context)