from django.urls import path, include
from .views import *

urlpatterns = [
    path('', HomePage.as_view(), name='index'),

    path('register/client/', ClientCreate.as_view(), name="register-client"),
    path('register/operator/', OperatorCreate.as_view(), name="register-operator"),
    path('register/service/', ServiceCreate.as_view(), name="register-service"),

    path('update/client/<int:pk>/', ClientUpdate.as_view(), name="update-client"),
    path('update/operator<int:pk>/', OperatorUpdate.as_view(), name="update-operator"),
    path('update/service/<int:pk>/', ServiceUpdate.as_view(), name="update-service"),

    path('delete/client/<int:pk>/', ClientDelete.as_view(), name="delete-client"),
    path('delete/operator/<int:pk>/', OperatorDelete.as_view(), name="delete-operator"),
    path('delete/service/<int:pk>/', ServiceDelete.as_view(), name="delete-service"),

    path('list/client/', ClientList.as_view(), name="list-client"),
]

