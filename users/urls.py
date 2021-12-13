from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('profile/', Profile.as_view(),name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html',extra_context={'titulo': 'Autenticação'}),name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
]
