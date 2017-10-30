from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings

def register(request):
    template_name = 'accounts/register.html'
    if request.method == 'POST':
        print("Post")
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print("Válido")
            form.save()
            return redirect(settings.LOGIN_URL)
        else:
            print("Inválido")
    else:
        form = UserCreationForm()
    context = {
        'form': form
    }
    return render(request, template_name, context)
