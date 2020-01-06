from django import forms
from django.core.mail import send_mail
from django.conf import settings

#from simplemooc.simplemooc.core.mail import send_mail_template

class ContactCourse(forms.Form):

    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='E-mail')
    message = forms.CharField(
        label='Mensagem/Dúvida', widget=forms.Textarea
    )# widget colocando o texto em area/ por padrao todos os campos sao obrigatorios.
    #para validar, caso nao queira, required=False


    def send_mail(self, course): # def de enviar email
        subject = f'{course} Contato'
        message = f'Nome: {self.cleaned_data["name"]};E-mail: {self.cleaned_data["email"]};' \
                f'Mensagem: {self.cleaned_data["message"]}'

        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.CONTACT_EMAIL])


    # def send_mail(self, course):
    #     subject = f'{course} Contato'
    #     context = {
    #         'name': self.cleaned_data['name'],
    #         'email': self.cleaned_data['email'],
    #         'message': self.cleaned_data['message'],
    #     }
    #     template_name = 'courses/contact_email.html'
    #     send_mail_template(subject, template_name, context,
    #                        [settings.CONTACT_EMAIL])
