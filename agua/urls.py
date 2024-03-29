"""agua URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import handler404, handler500
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static
from base.views import SignupView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('base.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('login/', LoginView.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(), name = 'logout'),
    path('signup/', SignupView.as_view(), name = 'signup'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'base.views.error_404'
handler500 = 'base.views.error_500'
handler403 = 'base.views.error_403'
handler400 = 'base.views.error_400'