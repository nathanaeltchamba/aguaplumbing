from django.urls import path

from .views import Home, AddMenuView, DashboardView, MenuListView

urlpatterns = [
    path('', Home.as_view(), name='Home'),
    path('create-menu/', AddMenuView.as_view(), name='create-menu'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('menulist/', MenuListView.as_view(), name='menu-list'),
]