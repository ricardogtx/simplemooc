from django import forms
#from django.core.mail import send_email
from django.conf import settings


class ContactCourse(forms.Form):
    name = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail')
    message = forms.CharField(
        label='Mensagem/Dúvida', widget=forms.Textarea
    )

    def send_email(self, course):
        subject = '[%S] Contato' % course
        message = 'Nome: %(name)s;E-mail: %(email)s;%(message)s'
        message = message % {
            'name': self.cleaned_data['name'],
            'email': self.cleaned_data['email'],
            'message': self.cleaned_data['message'],
        }
        message = message % context
        send_email(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.CONTACT_EMAIL])
