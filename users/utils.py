from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.urls import reverse_lazy


def send_verification_email(user):
    token = default_token_generator.make_token(user)
    uid = user.pk
    verification_link = reverse_lazy('users:verify_email', kwargs={'uidb64': uid, 'token': token})
    site = settings.SITE_NAME
    subject = 'Поздравляем Вас с регистрацией!'
    message = f'Вы зарегистрировались на сайте' \
              f' Для активации аккаунта перейдите по ссылке: {site}{verification_link}'
    from_email = settings.EMAIL_BACKEND
    recipient_list = [user.email]
    send_mail(subject, message, from_email, recipient_list)

    user.is_active = True
    user.save()