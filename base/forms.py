from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Menu, Service, About, Contact
from ckeditor.widgets import CKEditorWidget

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

# MENU FORMS -----------------------------------------

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

# ABOUT FORMS -----------------------------------------        

class AboutForm(forms.ModelForm):
    title = forms.CharField(required=False, help_text='Optional')
    content = forms.Textarea()

    class Meta:
        model = About
        fields = ('title', 'content')

class AboutUpdateForm(forms.ModelForm):
    title = forms.CharField(required=False, help_text='Optional')
    content = forms.Textarea()

    class Meta:
        model = About
        fields = ('title', 'content')

# SERVICE FORMS --------------------------------------

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
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'content':forms.Textarea(attrs={'class':'form-control'}),
        }

# CONTACT FORMS -----------------------------------------
class ContactCreationForm(forms.ModelForm):
    title = forms.CharField(required=False, help_text='Optional')
    address = forms.CharField()
    email = forms.CharField()
    phone_number = forms.CharField()
    business_hours = forms.Textarea()
    service_area = forms.CharField()
    content = forms.Textarea()

    class Meta:
        model = Contact
        fields = ('title', 'address', 'email', 'phone_number','business_hours', 'service_area', 'content')

class ContactUpdateForm(forms.ModelForm):
    title = forms.CharField(required=False, help_text='Optional')
    address = forms.CharField()
    email = forms.CharField()
    phone_number = forms.CharField()
    business_hours = forms.Textarea()
    service_area = forms.CharField()
    content = forms.Textarea()

    class Meta:
        model = Contact
        fields = ('title', 'address', 'email', 'phone_number','business_hours', 'service_area', 'content')

class InquiryForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
