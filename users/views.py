from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from users.forms import RegistrationForm


def home(request):
    if request.user.is_authenticated:
        return render(request, 'users/home.html')

    return render(request, 'users/login.html')


class UserLogin(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True


class UserRegistration(View):
    def get(self, request):
        return render(request, 'users/registration.html', {'form': RegistrationForm()})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            is_valid = True
            if User.objects.filter(email=email).exists():
                messages.error(request, "Email is already used")
                is_valid = False
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username is already used")
                is_valid = False
            if not is_valid:
                return render(request, 'users/registration.html',
                              {'form': form,
                               'email': email,
                               'username': username})

            User.objects.create_user(
                username=form.cleaned_data.get('username'),
                email=form.cleaned_data.get('email'),
                password=form.cleaned_data.get('password')
            )

            return HttpResponseRedirect(reverse('home'))

        return render(request, 'users/registration.html', {'form': form})
