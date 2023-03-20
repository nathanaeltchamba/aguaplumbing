from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Menu, Service, About
from ckeditor.widgets import CKEditorWidget

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

class MenuForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Menu
        fields  = ['title','content', 'snippet']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control w-75'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.TextInput(attrs={'class': 'form-control w-75'}),
        }
        
class EditMenuForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Menu
        fields  = ['title','content', 'snippet']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control w-75'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.TextInput(attrs={'class': 'form-control w-75'}),
        }
        

class AboutForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = About
        fields = ['title', 'content']
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control w-75'}),
            'content':forms.Textarea(attrs={'class':'form-control'}),
        }

class ServiceForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Service
        fields = ['title', 'content']
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control w-75'}),
            'content':forms.Textarea(attrs={'class':'form-control'}),
        }

class UpdateServiceForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Service
        fields = ['title', 'content']
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control w-75'}),
            'content':forms.Textarea(attrs={'class':'form-control'}),
        }