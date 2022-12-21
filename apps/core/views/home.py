from django.views.generic import TemplateView
from django.shortcuts import render, redirect

from apps.venda.models import Compra
from apps.atendimento.models import Consulta, Servico
from django.contrib.auth.mixins import LoginRequiredMixin



class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "home.html"
    login_url = 'apps:core:login'




    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['title'] = 'Home'
        user = self.request.user
        context['user'] = user
        
        return context

     

    