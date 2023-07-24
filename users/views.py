import random

from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView as BaseLoginView, PasswordResetDoneView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.urls import reverse_lazy, reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views import View
from django.views.generic import CreateView, UpdateView, TemplateView

from users.forms import UserForm, UserProfileForm
from users.models import User
from users.utils import send_verification_email


class LoginView(BaseLoginView):
    template_name = 'users/login.html'


class LogoutView(BaseLogoutView):
    pass



class RegisterView(CreateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/register.html'

    def form_valid(self, form):
        new_user = form.save()
        send_verification_email(new_user)
        return redirect('users:email_confirm')

class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')


    def get_object(self, queryset=None):
        return self.request.user


def generate_new_password(request):
    new_pass = ''.join([str(random.randint(0, 9)) for _ in range(12)])
    send_mail(
        subject='Вы сменили пароль',
        message=f'Ваш новый пароль: {new_pass}',
        from_email=settings.EMAIL_BACKEND,
        recipient_list=[request.user.email]
    )
    request.user.set_password(new_pass)
    request.user.save()
    return redirect(reverse('user:profile'))


class UserConfirmationSentView(PasswordResetDoneView):
      template_name = 'users/email_confirm.html'



class UserVerifyEmailView(View):
    def get(self, request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64)
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            login(request, user)
            return redirect('users:email_confirmed')
        else:
            return redirect('users:email_confirmation_failed')

class UserConfirmedView(TemplateView):
    template_name = 'users/email_confirm.html'
