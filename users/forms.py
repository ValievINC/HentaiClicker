from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from users.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Логин',
        widget=forms.TextInput(attrs={'placeholder': 'Вводи имя', 'class': 'formClass'}),
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'placeholder': 'Вводи пароль', 'class': 'formClass'}),
    )

    class Meta:
        model = User
        fields = ('username', 'password')


class RegistrationForm(UserCreationForm):
    username = forms.CharField(
        label='Логин',
        widget=forms.TextInput(attrs={'placeholder': 'Вводи имя', 'class': 'formClass'}),
    )
    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'placeholder': 'Вводи пароль', 'class': 'formClass'}),
    )
    password2 = forms.CharField(
        label='Подтвердите пароль',
        widget=forms.PasswordInput(attrs={'placeholder': 'Вводи пароль ещё', 'class': 'formClass'}),
    )

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=True)
        return user
