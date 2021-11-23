from django.urls import path, include
from .views import AboutPage

urlpatterns = [
    path('about', AboutPage.as_view(), name='index'),
]