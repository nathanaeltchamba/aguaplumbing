from django.urls import path

from .views import (Home, CustomLoginView, DashboardView, 
                    AddMenuView, MenuListView, MenuDetailView, MenuUpdateView, MenuDelete, 
                    AddServiceView, ServiceDetailView, ServiceUpdateView, ServiceDeleteView, ServiceList,
                    AddContactView, ContactDetailView, ContactUpdateView, ContactDeleteView, ContactList,
                    AddAboutUsView, AboutDetailView, AboutUpdateView, AboutDeleteView, AboutList,
                    Inquiry,)


urlpatterns = [
    path('', Home.as_view(), name='Home'),
    # Create Paths
    path('create-menu/', AddMenuView.as_view(), name='create-menu'),
    path('create-service/', AddServiceView.as_view(), name='create-service'),
    path('create-contact/', AddContactView.as_view(), name='create-contact'),
    path('create-about/', AddAboutUsView.as_view(), name='create-about'),
    # List Paths
    path('menu-list/', MenuListView.as_view(), name='menu-list'),
    path('service-list/', ServiceList.as_view(), name='service-list'),
    path('contact-list/', ContactList.as_view(), name='contact-list'),
    path('about-list/', AboutList.as_view(), name='about-list'),
    # Detail Paths
    path('menu/<slug:slug>/', MenuDetailView.as_view(), name='menu-detail'),
    # Update Paths
    path('menu/<slug:slug>/update/', MenuUpdateView.as_view(), name='menu-update'),
    path('service/<slug:slug>/update/', ServiceUpdateView.as_view(), name='service-update'),
    path('contact/<slug:slug>/update/', ContactUpdateView.as_view(), name='contact-update'),
    path('about/<slug:slug>/update/', AboutUpdateView.as_view(), name='about-update'),
    # Delete Paths
    path('menu/<slug:slug>/delete/', MenuDelete.as_view(), name='menu-delete'),
    path('service/<slug:slug>/delete/', ServiceDeleteView.as_view(), name='service-delete'),
    path('contact/<slug:slug>/delete/', ContactDeleteView.as_view(), name='contact-delete'),
    path('about/<slug:slug>/delete/', AboutDeleteView.as_view(), name='about-delete'),
    # Misc Paths
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('login/', CustomLoginView.as_view(), name='login'),
    # path('contact/', ContactDetailView.as_view(), name='contact-detail'),
    path('services/', ServiceDetailView.as_view(), name='service-detail'),
    path('about/', AboutDetailView.as_view(), name='about-detail'),
    path('inquiry/', Inquiry.as_view(), name='inquiry'),
]