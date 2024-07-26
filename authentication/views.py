from django.shortcuts import render, redirect
from django.http import HttpResponse
from .views import *
from . forms import *
from django.contrib.auth import login, authenticate, logout, get_user_model
from django.conf import settings
from django.contrib.auth.views import *
from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse_lazy
from django.conf import settings
from django.views.generic.edit import CreateView
from django.core.mail import send_mail, EmailMultiAlternatives
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
# from django.contrib.auth.forms import PasswordResetForm
# from django.views.generic import View

class sign_up(CreateView):
    model = get_user_model
    form_class = SignUpForm
    template_name = 'authentication/sign_up_page.html'
    success_url = reverse_lazy('complete_verification')

    # Enregistrement de l'utilisateur 

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()

    # Configuration pour l'envoi de mail et génération du lien de vérification d'inscription

        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        url = self.request.build_absolute_uri(
            reverse_lazy('active_account', kwargs = {'uidb64': uid, 'token': token})
        )
        context = {'url': url, 'user': user}  
        message = render_to_string('authentication/active_account.html', context)
        subject = "Activer votre compte FotoBlog"
        from_email = "gbedagbehonorat@gmail.com"
        to_email = [user.email]

        # send_mail(

        #     subject,
        #     message,
        #     from_email,
        #     to_email,
        #     fail_silently=False,
        # )

        print(f"{subject}")
        print(f"{message}")
        print(f"{from_email}")
        print(f"{to_email}")

        try:
            email = EmailMultiAlternatives(
                subject=subject,
                body=message,
                from_email=from_email,
                to=to_email
            )
            email.attach_alternative(message, 'text/html')
            email.send(fail_silently=False)
            print('Email sent succesfull')
        except Exception as e:
            print('Email sent failed because the follow eception {e}')

#       Pour poursuivre l'éxécution du traitement standart du formulaire avec la classe parente
        return super().form_valid(form)
    
    
def complete_verification(request):
    return render(request, 'authentication/complete_verification.html')

def active_account(request, uidb64, token):
    Model = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = Model.objects.get(pk=uid)
    except (ValueError, TypeError, OverflowError, Model.DoesNotExist):
        user = None

    if user is not None:
        user.is_active = True
        user.save()
        return redirect(settings.LOGIN_REDIRECT_URL)
    else:
        return render(request, 'authentication/verification_failed.html')

class passwordresetview(PasswordResetView):
    template_name = 'authentication/password_reset_page.html'
    email_template_name = 'authentication/password_reset_email.html'
    subject_template_name = 'authentication/password_reset_subject.html'
    token_generator = default_token_generator
    success_url = reverse_lazy('password_reset_confirm')

class passwordchangedoneview(PasswordChangeDoneView):
    template_name = 'authentication/password_reset_confirm.html'

class passwordresetdoneview(PasswordResetConfirmView):
    template_name = 'authentication/password_reset_confirm_done.html'
    token_generator = default_token_generator
    success_url = reverse_lazy(settings.LOGIN_REDIRECT_URL)
    post_reset_login = False
