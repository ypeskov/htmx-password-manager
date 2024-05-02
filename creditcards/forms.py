from django import forms

from .models import CreditCard


class CreditCardForm(forms.ModelForm):
    class Meta:
        model = CreditCard
        fields = ['title', 'holder_name', 'brand', 'number', 'expiration_month',
                  'expiration_year', 'cvv', 'pin', 'notes']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight'
                         + 'focus:outline-none focus:shadow-outline',
                'placeholder': 'Title'
            }),
            'holder_name': forms.TextInput(attrs={
                'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight'
                         + 'focus:outline-none focus:shadow-outline',
                'placeholder': 'Holder Name'
            }),
            'brand': forms.TextInput(attrs={
                'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight'
                         + 'focus:outline-none focus:shadow-outline',
                'placeholder': 'Brand'
            }),
            'number': forms.TextInput(attrs={
                'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight'
                         + 'focus:outline-none focus:shadow-outline',
                'placeholder': 'Card Number (16 digits)'
            }),
            'expiration_month': forms.TextInput(attrs={
                'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight'
                         + 'focus:outline-none focus:shadow-outline',
                'placeholder': 'Expiration Month (1-12)'
            }),
            'expiration_year': forms.TextInput(attrs={
                'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight'
                         + 'focus:outline-none focus:shadow-outline',
                'placeholder': 'Expiration Year (YYYY)'
            }),
            'cvv': forms.TextInput(attrs={
                'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight'
                         + 'focus:outline-none focus:shadow-outline',
                'placeholder': 'CVV (3 digits)'
            }),
            'pin': forms.TextInput(attrs={
                'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight'
                         + 'focus:outline-none focus:shadow-outline',
                'placeholder': 'PIN (4 digits)'
            }),
            'notes': forms.Textarea(attrs={
                'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight'
                         + 'focus:outline-none focus:shadow-outline',
                'rows': 3,
                'placeholder': 'Notes'
            }),
        }
