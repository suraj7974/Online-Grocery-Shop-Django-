from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('cart/', views.cart),
    path('thank_you/', views.thank_you),
]