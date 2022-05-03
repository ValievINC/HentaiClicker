from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'password_confirm']

    username = forms.CharField(
        max_length=20,
        label='Имя пользователя',
        widget=forms.TextInput(attrs={'placeholder': 'Вводи'}),
    )
    password = forms.CharField(
        min_length=3,
        max_length=20,
        label='Пароль',
        widget=forms.PasswordInput(attrs={'placeholder': 'Вводи пароль'}),
    )
    password_confirm = forms.CharField(
        min_length=3,
        max_length=20,
        label='Подтверждение пароля',
        widget=forms.PasswordInput(attrs={'placeholder': 'Вводи пароль ещё'}),
    )

    def clean(self):
        cleaned_data = self.cleaned_data
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        if password != password_confirm:
            raise forms.ValidationError("Пароли разные!")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get("password"))
        if commit:
            user.save()
        return user