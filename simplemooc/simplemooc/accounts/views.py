from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.conf import settings

from .forms import RegisterForm, EditAccountForm

@login_required
def dashboard(request):
    template_name='accounts/dashboard.html'
    context = {}
    return render(request, template_name, context)

def register(request):
    template_name = 'accounts/register.html'
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(
                username = user.username,
                password = form.cleaned_data['password1']
            )
            login(request, user)

            return redirect('core:home')
    else:
        form = RegisterForm()
    context = {
        'form': form
    }
    return render(request, template_name, context)

@login_required
def edit(request):
    template_name='accounts/edit.html'
    form = EditAccountForm
    context = {}
    if request.method == 'POST':
        form = EditAccountForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            form = EditAccountForm(instance=request.user)
            context['success'] = True
    else:
        form = EditAccountForm(instance=request.user)
        
    context = {
        'form': form
    }
    return render(request, template_name, context)

@login_required
def edit_password(request):
    print('Entrou 1')
    template_name = 'accounts/edit_password.html'
    context = {}
    if request.method == 'POST':
        print('Entrou 2')
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            print('Entrou Salvou')
            context['success'] = True
    else:
        form = PasswordChangeForm(user=request.user)
        print('Entrou Não salvou')
    context['form'] = form

    return render(request, template_name, context)
