from django.forms import ModelForm
from django import forms
from .models import Todo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import PasswordInput


class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'task_image', 'complete', 'user']
        widgets = {'user': forms.HiddenInput(),
                   'title': forms.fields.TextInput(attrs={'placeholder': 'Title...'}),
                   'description': forms.fields.TextInput(attrs={'placeholder': 'Description...'}),
                   'complete': forms.fields.CheckboxInput(attrs={'class': 'checkbox'})
                   }


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        widgets = {
            'username': forms.fields.TextInput(attrs={'placeholder': 'Username...'})
        }

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Password...'})
        self.fields['password2'].widget = PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Password confirmation...'})
