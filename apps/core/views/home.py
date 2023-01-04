from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.db.models import Sum
from apps.venda.models import Compra, ItemCompra
from apps.atendimento.models import Servico, Consulta
from django.contrib.auth.mixins import LoginRequiredMixin



class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "home.html"
    login_url = 'apps:core:login'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['title'] = 'Home'
        user = self.request.user
        context['user'] = user
        context['valor_compras'] = ItemCompra.objects.all().aggregate(Sum('valor_item'))['valor_item__sum'] or 0
        q = Compra.objects.all().count()
        context['quant_compra'] = q
        context['list_vendas']  = Compra.objects.all().order_by('-id')[:7]
        context['list_consultas']  = Servico.objects.all().order_by('-id')[:7]
        context['list_servicos']  = Servico.objects.all().order_by('-id')[:7]
        
        # context['valor_servicos'] = Servico.objects.all().aggregate(Sum('valor'))['valor__sum'] or 0
        # context['valor_consultas'] = Consulta.objects.all().aggregate(Sum('valor'))['valor__sum'] or 0
        # context['total'] = context['valor_compras'] + context['valor_servicos'] + context['valor_consultas']
        
        return context

     

    