from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import MainUser


class SignUpForm(UserCreationForm):
    # username = forms.CharField(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    # first_name = forms.CharField(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
    #                              max_length=32, help_text='First name')
    # last_name = forms.CharField(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
    #                             max_length=32, help_text='Last name')
    # email = forms.EmailField(forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}), max_length=64,
    #                          help_text='Enter a valid email address')
    # password1 = forms.CharField(forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    # password2 = forms.CharField(forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Again'}))
    user_tg_id = forms.IntegerField(label= 'Telegram id', help_text='This is not required', required=False)

    class Meta(UserCreationForm.Meta):
        model = MainUser
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email', 'user_tg_id')


class SelfUserChangeForm(UserChangeForm):
    user_tg_id = forms.IntegerField(label= 'Telegram id', help_text='This is not required', required=False)

    class Meta(UserChangeForm.Meta):
        model = MainUser
        fields = ('first_name', 'last_name', 'email', 'user_tg_id')

