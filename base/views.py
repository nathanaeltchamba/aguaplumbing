from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, UpdateView, DeleteView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib import messages
from .forms import (CustomUserCreationForm, InquiryForm, MenuForm, EditMenuForm, 
                    ServiceForm, AboutForm, AboutUpdateForm, UpdateServiceForm, ContactCreationForm, ContactUpdateForm)
from .models import Menu, User, Service, About, Contact

# Create your views here.
class Home(TemplateView):
    template_name = 'home.html'

    def get(self, request):
        context = {}

        services_card_1 = Service.objects.filter(card_number=1)
        services_card_2 = Service.objects.filter(card_number=2)
        services_card_3 = Service.objects.filter(card_number=3)
        contact = Contact.objects.first()

        context['services_card_1'] = services_card_1
        context['services_card_2'] = services_card_2
        context['services_card_3'] = services_card_3
        context['contact'] = contact

        return render(request, 'home.html', context)
    
    

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

# MENU CRUD VIEWS --------------------------------
class MenuListView(LoginRequiredMixin, TemplateView):
    template_name = 'menu/menu-list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menulist'] = Menu.objects.all()
        context['aboutus'] = About.objects.first()
        context['services'] = Service.objects.all()
        context['contacts'] = Contact.objects.all()
        return context
    

    
class AddMenuView(LoginRequiredMixin, CreateView):
    model = Menu
    template_name = 'menu/menu-create.html'
    success_url = reverse_lazy('Home')
    form_class = MenuForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class MenuDetailView(DetailView):
    model = Menu
    template_name = 'menu/menu-detail.html'

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
    template_name = 'menu/menu-update.html'
    form_class = EditMenuForm

    def form_valid(self, form):
        custom_user, created = User.objects.get_or_create(username=self.request.user.username)
        form.instance.author = custom_user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('menu-list')
    
class MenuDelete(LoginRequiredMixin, DeleteView):
    model = Menu 
    template_name = 'menu/menu-delete.html'

    def get_success_url(self):
        return reverse('menu-list')
    
# SERVICE CRUD VIEWS -------------------------------
# later include individual service section update.

class AddServiceView(LoginRequiredMixin, CreateView):
    model = Service
    template_name = 'service/service-create.html'
    success_url = reverse_lazy('Home')
    form_class = ServiceForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        if self.model.objects.count() > 0:
            form.add_error(None, 'You already have a Service Page. Update or delete that page before creating a new one.')
            return self.form_invalid(form)
        return super().form_valid(form)
    
class ServiceList(LoginRequiredMixin, ListView):
    model = Service
    template_name = 'service/service-list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['aboutus'] = About.objects.first()
        context['services'] = Service.objects.all()
        context['contacts'] = Contact.objects.all()
        return context

class ServiceDetailView(TemplateView):
    model = Service
    template_name = 'service/service-detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
    
class ServiceUpdateView(UpdateView):
    model = Service
    template_name = 'service/service-update.html'
    form_class = UpdateServiceForm

    def form_valid(self, form):
        custom_user, created = User.objects.get_or_create(username=self.request.user.username)
        form.instance.author = custom_user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('menu-list')
    
class ServiceDeleteView(DeleteView):
    model = Service
    template_name = 'service/service-delete.html'

    def get_success_url(self):
        return reverse('Home')
    
# CONTACT CRUD VIEWS -------------------------------

class AddContactView(LoginRequiredMixin, CreateView):
    model = Contact
    template_name = 'contact/contact-create.html'
    success_url = reverse_lazy('Home')
    form_class = ContactCreationForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class ContactList(LoginRequiredMixin, ListView):
    model = Contact
    template_name = 'contact/contact-list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contacts'] = Contact.objects.all()
        return context
    
class ContactDetailView(TemplateView):
    model = Contact
    template_name = 'contact/contact-detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['contacts'] = Contact.objects.all()
        return context
    
class ContactUpdateView(UpdateView):
    model = Contact
    template_name = 'contact/contact-update.html'
    form_class = ContactUpdateForm

    def form_valid(self, form):
        custom_user, created = User.objects.get_or_create(username=self.request.user.username)
        form.instance.author = custom_user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('dashboard')
    
class ContactDeleteView(DeleteView):
    model = Contact
    template_name = 'contact/contact-delete.html'

    def get_success_url(self):
        return reverse('Home')
# ABOUT US CRUD VIEWS ------------------------------

class AddAboutUsView(LoginRequiredMixin, CreateView):
    model = About
    template_name = 'about/aboutus-create.html'
    success_url = reverse_lazy('dashboard')
    form_class = AboutForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class AboutList(LoginRequiredMixin, ListView):
    model = About
    template_name = 'about/about-list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['aboutus'] = About.objects.all()
        return context
    
class AboutDetailView(TemplateView):
    model = About
    template_name = 'about/about-detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['aboutus'] = About.objects.all()
        return context
    
class AboutUpdateView(LoginRequiredMixin, UpdateView):
    model = About
    template_name = 'about/about-update.html'
    form_class = AboutUpdateForm

    def form_valid(self, form):
        custom_user, created = User.objects.get_or_create(username=self.request.user.username)
        form.instance.author = custom_user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('dashboard')
    
class AboutDeleteView(LoginRequiredMixin, DeleteView):
    model = About
    template_name = 'about/about-delete.html'
    success_url = reverse_lazy('dashboard')

    
# MISC VIEWS -----------------------------------------
class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menulist'] = Menu.objects.all()
        context['aboutus'] = About.objects.first()
        context['services'] = Service.objects.all()
        context['contacts'] = Contact.objects.all()
        return context
    
class CreationView(LoginRequiredMixin, TemplateView):
    template_name = 'create-page.html'
    