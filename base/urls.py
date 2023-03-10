from django.urls import path

from .views import Home, AddMenuView

urlpatterns = [
    path('', Home.as_view(), name='Home'),
    path('menu/', AddMenuView.as_view(), name='menu')
]