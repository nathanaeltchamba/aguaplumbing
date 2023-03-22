from django.contrib import admin
from .models import Menu, About, Service, Contact

# Register your models here.
admin.site.register(Menu)
admin.site.register(About)
admin.site.register(Service)
admin.site.register(Contact)