from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from django import forms
from django.utils.translation import ugettext_lazy as _
from .utils import Analizator


class TaskForm(forms.Form):
    answer = forms.CharField(max_length=5)
    flag = False

    def clean_answer(self):
        data = self.cleaned_data['answer']

        if not data.isdigit():
            raise ValidationError(_('Invalid data not int digit given!!!'))

        return data


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(), min_length=3, max_length=10)

    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(), min_length=8, max_length=20)
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(), min_length=8, max_length=20)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

