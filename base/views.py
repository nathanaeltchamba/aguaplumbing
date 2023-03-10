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
    success_url = reverse_lazy('menu-list')
    form_class = MenuForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class MenuListView(ListView):
    template_name = 'menu-list.html'
    context_object_name = 'menulists'

    def get_queryset(self):
        return Menu.objects.all()

class DashboardView(TemplateView):
    template_name = 'dashboard.html'
    
