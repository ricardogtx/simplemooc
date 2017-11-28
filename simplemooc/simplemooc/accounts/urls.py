from django.conf.urls import url
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from .views import register,dashboard, edit

urlpatterns = [
    url(r'^/$', dashboard, name='dashboard'),
    url(r'^entrar/$', login, {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^sair/$', logout, {'next_page': 'core:home'}, name='logout'),
    url(r'^cadastre-se/$', register, name='register'),
    url(r'^editar/$', edit, name='edit')
]
