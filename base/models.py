from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.core.validators import MaxValueValidator
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
    
class Menu(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextUploadingField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    snippet = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title
    
class About(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextUploadingField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, default='new-slug')

    def __str__(self):
        return self.title
    
class Service(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextUploadingField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    card_number = models.IntegerField(validators=[MaxValueValidator(3)], default=0)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title
    
class Contact(models.Model):
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=50)
    business_hours = models.TextField()
    service_area = models.CharField(max_length=150, default='Denver Metropolitan Area')
    content = models.TextField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title
    

def pre_save_menu_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)

pre_save.connect(pre_save_menu_receiver, sender=Menu)