from django.urls import path

from users.views import UserLogin, UserRegistration, logout_user

app_name = 'users'

urlpatterns = [
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', UserRegistration.as_view(), name='register'),
]
