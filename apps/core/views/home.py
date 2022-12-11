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
                return Compra.objects.filter(atendente=user)
            elif user.fucionario_type == 'tecnico':
                return Servico.objects.filter(tecnico=user)
            elif user.fucionario_type == 'veterinario':
                return Consulta.objects.filter(veterinario=user)
        else:
            return redirect('apps:core:login')


    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        query = self.get_queryset()[:10]
        context['title'] = 'Home'
        user = self.request.user
        context['user'] = user
        if user.is_authenticated:
            if user.fucionario_type == 'atendente':
                context['compras'] = query
            elif user.fucionario_type == 'tecnico':
                context['servicos'] = query
            elif user.fucionario_type == 'veterinario':
                context['consultas'] = query
        else:
            return redirect('apps:core:login')
        
        return context

     

    