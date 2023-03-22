from django.urls import path

from .views import (Home, CustomLoginView, DashboardView, CreationView, AddMenuView, MenuListView, 
                    MenuDetailView, MenuUpdateView, MenuDelete, 
                    AddServiceView, ServiceDetailView, ServiceUpdateView, ServiceDeleteView)


urlpatterns = [
    path('', Home.as_view(), name='Home'),
    path('create-menu/', AddMenuView.as_view(), name='create-menu'),
    path('create-service/', AddServiceView.as_view(), name='create-service'),
    path('menu/<slug:slug>/', MenuDetailView.as_view(), name='menu-detail'),
    path('service/<slug:slug>/', ServiceDetailView.as_view(), name='service-detail'),
    path('menu/<slug:slug>/update/', MenuUpdateView.as_view(), name='menu-update'),
    path('service/<slug:slug>/update/', ServiceUpdateView.as_view(), name='service-update'),
    path('menu/<slug:slug>/delete/', MenuDelete.as_view(), name='menu-delete'),
    path('service/<slug:slug>/delete/', ServiceDeleteView.as_view(), name='service-delete'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('create/', CreationView.as_view(), name='create'),
    path('menulist/', MenuListView.as_view(), name='menu-list'),
    path('login/', CustomLoginView.as_view(), name='login')
]