from django.urls import path
from . import views

urlpatterns = [
    path('', views.start),
    path('register/', views.register),
    path('register/register', views.register),
    path('login/', views.login),
    path('login/login', views.login),
    path('about-us/', views.about_us),
    path('logout/', views.logout),
]