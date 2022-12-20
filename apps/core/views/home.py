from django.views.generic import TemplateView
from django.shortcuts import render, redirect

from apps.venda.models import Compra
from apps.atendimento.models import Consulta, Servico
from django.contrib.auth.mixins import LoginRequiredMixin



class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "home.html"
    login_url = 'apps:core:login'

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            if user.fucionario_type == 'atendente':
                return Compra.objects.filter(atendente=user).order_by('-data_compra')
            elif user.fucionario_type == 'tecnico':
                return Servico.objects.filter(tecnico=user)
            elif user.fucionario_type == 'veterinario':
                return Consulta.objects.filter(veterinario=user)
        else:
            return redirect('apps:core:login')


    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        query = self.get_queryset()
        context['title'] = 'Home'
        user = self.request.user
        context['user'] = user
        if user.is_authenticated:
            if user.fucionario_type == 'atendente':
                context['sidebar'] = 'venda'
                context['compras'] = query
                context['link_create'] = {
                    'url': 'http://' + self.request.get_host() + '/compra/create/',
                    'text': 'Nova Compra'
                }
            elif user.fucionario_type == 'tecnico':
                context['sidebar'] = 'atendimento'
                context['servicos'] = query
                context['link_create'] = {
                    'url': 'http://' + self.request.get_host() + '/servico/create/',
                    'text': 'Novo Serviço'
                }
            elif user.fucionario_type == 'veterinario':
                context['sidebar'] = 'Consulta'
                context['link_create'] = {
                    'url': 'http://' + self.request.get_host() + '/consulta/create/',
                    'text': 'Nova Consulta'
                }
                context['consultas'] = query
        else:
            return redirect('apps:core:login')
        
        return context

     

    