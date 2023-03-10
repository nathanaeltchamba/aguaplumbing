from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Menu

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields  = ['title','content']
        widgets = {
            'content': forms.Textarea(attrs={'cols': 100, 'rows': 30}),
        }