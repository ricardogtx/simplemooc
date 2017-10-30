from django.conf.urls import url
from django.contrib.auth.views import login
from .views import register

urlpatterns = [
    url(r'^entrar/$', login, {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^cadastre-se/$', register, name='register'),
]
