from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Client, Operator, Service
from django import forms
from django.shortcuts import get_object_or_404


class HomePage(TemplateView):
    template_name = 'pages/index.html'


class Operators(ListView):
	model = Operator
	template_name = 'pages/operators.html'


class Services(ListView):
	model = Service
	template_name = 'pages/services.html'


# ---------------------------------------------------------------------------------------------
#                                      CREATE VIEWS
# ---------------------------------------------------------------------------------------------

class ClientCreate(LoginRequiredMixin, CreateView):
	login_url = reverse_lazy('login')
	model = Client
	fields = ['name', 'identification', 'state', 'city']
	template_name = 'pages/form.html'
	success_url = reverse_lazy('index')


class OperatorCreate(LoginRequiredMixin, CreateView):
	login_url = reverse_lazy('login')
	model = Operator
	fields = ['name', 'identification', 'area', 'department', 'rank', 'payment']
	template_name = 'pages/form.html'
	success_url = reverse_lazy('index')
	def form_valid(self, form):

		# Define o usuário como usuário logado
		form.instance.user = self.request.user
			
		url = super().form_valid(form)

		# Salva o objeto novamente
		self.object.save()

		return url




class ServiceCreate(LoginRequiredMixin, CreateView):
	login_url = reverse_lazy('login')
	model = Service
	fields = ['name', 'stage', 'level', 'price']
	template_name = 'pages/form.html'
	success_url = reverse_lazy('index')
	def form_valid(self, form):

		# Define o usuário como usuário logado
		form.instance.user = self.request.user
			
		url = super().form_valid(form)

		# Salva o objeto novamente
		self.object.save()

		return url


# ---------------------------------------------------------------------------------------------
#                                      UPDATE VIEWS
# ---------------------------------------------------------------------------------------------

class ClientUpdate(LoginRequiredMixin, UpdateView):
	login_url = reverse_lazy('login')
	model = Client
	fields = ['name', 'identification', 'state', 'city']
	template_name = 'pages/form.html'
	success_url = reverse_lazy('list-client')


class OperatorUpdate(LoginRequiredMixin, UpdateView):
	login_url = reverse_lazy('login')
	model = Operator
	fields = ['name', 'identification', 'area', 'department', 'rank', 'payment']
	template_name = 'pages/form.html'
	success_url = reverse_lazy('index')

	def get_object(self, queryset=None):
		self.object = get_object_or_404(Operator, pk=self.kwargs['pk'], user=self.request.user)
		return self.object

class ServiceUpdate(LoginRequiredMixin, UpdateView):
	login_url = reverse_lazy('login')
	model = Service
	fields = ['name', 'stage', 'level', 'price']
	template_name = 'pages/form.html'
	success_url = reverse_lazy('index')
	def get_object(self, queryset=None):
		self.object = get_object_or_404(Service, pk=self.kwargs['pk'], user=self.request.user)
		return self.object

# --------------------------------------------------------------------------------------------- 
#                                      DELETE VIEWS
# --------------------------------------------------------------------------------------------- 

class ClientDelete(LoginRequiredMixin, DeleteView):
	login_url = reverse_lazy('login')
	model = Client
	template_name = 'pages/delete.html'
	success_url = reverse_lazy('list-client')

class OperatorDelete(LoginRequiredMixin, DeleteView):
	login_url = reverse_lazy('login')
	model = Operator
	template_name = 'pages/delete.html'
	success_url = reverse_lazy('index')
	def get_object(self, queryset=None):
		self.object = get_object_or_404(Operator, pk=self.kwargs['pk'], user=self.request.user)
		return self.object


class ServiceDelete(LoginRequiredMixin, DeleteView):
	login_url = reverse_lazy('login')
	model = Service
	template_name = 'pages/delete.html'
	success_url = reverse_lazy('index')
	def get_object(self, queryset=None):
		self.object = get_object_or_404(Service, pk=self.kwargs['pk'], user=self.request.user)
		return self.object

# --------------------------------------------------------------------------------------------- 
#                                      LIST VIEWS
# --------------------------------------------------------------------------------------------- 

class ClientList(LoginRequiredMixin, ListView):
	login_url = reverse_lazy('login')
	model = Client
	template_name = 'pages/client-list.html'
	success_url = reverse_lazy('index')

class OperatorList(LoginRequiredMixin, ListView):
	login_url = reverse_lazy('login')
	model = Operator
	template_name = 'pages/operator-list.html'
	success_url = reverse_lazy('index')

class ServiceList(LoginRequiredMixin, ListView):
	login_url = reverse_lazy('login')
	model = Service
	template_name = 'pages/service-list.html'
	success_url = reverse_lazy('index')
