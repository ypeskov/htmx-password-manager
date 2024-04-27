from django import forms


class RegistrationForm(forms.Form):
    password_error_messages = {
        'min_length': 'This password is too short. It must contain at least 3 characters.',
    }
    username = forms.CharField(label='Username',
                               max_length=100,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email',
                             max_length=100,
                             widget=forms.TextInput(attrs={'class': 'form-control'}), )
    password = forms.CharField(label='Password',
                               min_length=3,
                               max_length=100,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                               error_messages=password_error_messages)
    password2 = forms.CharField(label='Repeat password',
                                min_length=3,
                                max_length=100,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                                error_messages=password_error_messages)
