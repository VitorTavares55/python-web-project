from django.views.generic import TemplateView
from django.urls import reverse_lazy

class Profile(TemplateView):
	template_name = 'users/profile.html'
