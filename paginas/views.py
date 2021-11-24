from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Client, Operator, Service

class HomePage(TemplateView):
    template_name = 'pages/index.html'


# --------------------------------------------------------------------------------------------- 
#                                      CREATE VIEWS
# --------------------------------------------------------------------------------------------- 

class ClientCreate(CreateView):
	model = Client
	fields = ['name', 'identification', 'state', 'city']
	template_name = 'pages/form.html'
	success_url = reverse_lazy('index')

class OperatorCreate(CreateView):
	model = Operator
	fields = ['name', 'identification', 'area', 'department', 'rank', 'payment']
	template_name = 'pages/form.html'
	success_url = reverse_lazy('index')

class ServiceCreate(CreateView):
	model = Service
	fields = ['name', 'stage', 'level', 'price']
	template_name = 'pages/form.html'
	success_url = reverse_lazy('index')

# --------------------------------------------------------------------------------------------- 
#                                      UPDATE VIEWS
# --------------------------------------------------------------------------------------------- 

class ClientUpdate(UpdateView):
	model = Client
	fields = ['name', 'identification', 'state', 'city']
	template_name = 'pages/form.html'
	success_url = reverse_lazy('list-client')

class OperatorUpdate(UpdateView):
	model = Operator
	fields = ['name', 'identification', 'area', 'department', 'rank', 'payment']
	template_name = 'pages/form.html'
	success_url = reverse_lazy('index')

class ServiceUpdate(UpdateView):
	model = Service
	fields = ['name', 'stage', 'level', 'price']
	template_name = 'pages/form.html'
	success_url = reverse_lazy('index')

# --------------------------------------------------------------------------------------------- 
#                                      DELETE VIEWS
# --------------------------------------------------------------------------------------------- 

class ClientDelete(DeleteView):
	model = Client
	template_name = 'pages/form.html'
	success_url = reverse_lazy('list-client')

class OperatorDelete(DeleteView):
	model = Operator
	template_name = 'pages/form.html'
	success_url = reverse_lazy('index')

class ServiceDelete(DeleteView):
	model = Service
	template_name = 'pages/form.html'
	success_url = reverse_lazy('index')

# --------------------------------------------------------------------------------------------- 
#                                      LIST VIEWS
# --------------------------------------------------------------------------------------------- 

class ClientList(ListView):
	model = Client
	template_name = 'pages/list.html'
	success_url = reverse_lazy('index')
