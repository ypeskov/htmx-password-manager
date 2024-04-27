from django.urls import path

from users.views import UserLogin, UserRegistration

app_name = 'users'

urlpatterns = [
    path('login/', UserLogin.as_view(), name='login'),
    path('register/', UserRegistration.as_view(), name='register'),
]
