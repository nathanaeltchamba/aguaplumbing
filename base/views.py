from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, DeleteView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CustomUserCreationForm, MenuForm
from .models import Menu

# Create your views here.
class Home(TemplateView):
    template_name = 'home.html'


class SignupView(CreateView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        return response
    
class AddMenuView(CreateView):
    model = Menu
    template_name = 'menus.html'
    success_url = reverse_lazy('stories')
    form_class = MenuForm

    def form_valid(self, form):
        title = form.cleaned_data.get('title')
        content = form.cleaned_data.get('content')
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)
    
