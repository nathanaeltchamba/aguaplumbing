from django.urls import path

from .views import Home, AddMenuView, DashboardView, MenuListView, MenuDetailView, MenuUpdateView, MenuDelete, CustomLoginView

urlpatterns = [
    path('', Home.as_view(), name='Home'),
    path('create-menu/', AddMenuView.as_view(), name='create-menu'),
    path('menu/<slug:slug>/', MenuDetailView.as_view(), name='menu-detail'),
    path('menu/<slug:slug>/update/', MenuUpdateView.as_view(), name='menu-update'),
    path('menu/<slug:slug>/delete/', MenuDelete.as_view(), name='menu-delete'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('menulist/', MenuListView.as_view(), name='menu-list'),
    path('login/', CustomLoginView.as_view(), name='login')
]