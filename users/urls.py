from django.urls import path

from users.apps import UsersConfig
from users.views import LoginView, LogoutView, RegisterView, ProfileView, generate_new_password, \
    UserConfirmationSentView, UserVerifyEmailView, UserConfirmedView

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/genpassword/', generate_new_password, name='generate_new_password'),
    path('email_confirm/', UserConfirmationSentView.as_view(), name='email_confirm'),
    path('verify_email/<str:uidb64>/<str:token>/', UserVerifyEmailView.as_view(), name='verify_email'),
    path('email_confirmed/', UserConfirmedView.as_view(), name='email_confirmed'),
]