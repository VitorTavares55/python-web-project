from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html',extra_context={'titulo': 'Autenticação'}),name='login'),
    path("register", views.register_request, name="register"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),

]