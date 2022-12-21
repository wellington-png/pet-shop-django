from __future__ import absolute_import, unicode_literals
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from apps.atendimento.models import TipoServico
from apps.atendimento.forms import TipoForm



class TipoServicoListView(LoginRequiredMixin, ListView):
    model = TipoServico
    template_name = 'tipo_servico_list.html'
    context_object_name = 'tipos'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(TipoServicoListView, self).get_context_data(**kwargs)
        context['title'] = 'Lista de Tipos de Serviço'
        return context
    
    def get_queryset(self):
        return TipoServico.objects.all().order_by('descricao')


class TipoServicoCreateView(LoginRequiredMixin, CreateView):
    model = TipoServico
    template_name = 'tipo_servico_create.html'
    success_url = reverse_lazy('apps:atendimento:tipo_servico_list')
    form_class = TipoForm

    def get_context_data(self, **kwargs):
        context = super(TipoServicoCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Cadastrar Tipo de Serviço'
        context['action'] = 'add'
        return context
