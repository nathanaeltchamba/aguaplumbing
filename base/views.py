from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, UpdateView, DeleteView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib import messages
from .forms import CustomUserCreationForm, MenuForm, EditMenuForm
from .models import Menu, User

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
    
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

    def form_valid(self, form):
        # Get the username of the logged in user
        username = form.cleaned_data.get('username')

        # Add a success message with the username
        messages.success(self.request, "Logged in successfully")

        return super().form_valid(form)

    
class AddMenuView(LoginRequiredMixin, CreateView):
    model = Menu
    template_name = 'menu-create.html'
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
    

class MenuDetailView(DeleteView):
    model = Menu
    template_name = 'menu-detail.html'

    def get_object(self, querset=None):
        return get_object_or_404(Menu, slug=self.kwargs.get('slug'))
    
    def get(self, request, *args, **kwargs):
        menu = self.get_object()
        Menu.objects.filter(slug=menu.slug)
        return super().get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

class MenuUpdateView(LoginRequiredMixin, UpdateView):
    model = Menu
    template_name = 'menu-update.html'
    form_class = EditMenuForm

    def form_valid(self, form):
        custom_user, created = User.objects.get_or_create(username=self.request.user.username)
        form.instance.author = custom_user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('menu-detail', kwargs={'slug': self.object.slug})
    
class MenuDelete(LoginRequiredMixin, DeleteView):
    model = Menu 
    template_name = 'menu-delete.html'

    def get_success_url(self):
        return reverse('menu-list')

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'
    
# need to fix the imaage that appears on the on the menu list ( youtube video on snippets )