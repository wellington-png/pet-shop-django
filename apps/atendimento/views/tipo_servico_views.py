from __future__ import absolute_import, unicode_literals
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from apps.atendimento.models import TipoServico
from apps.atendimento.forms import TipoForm
from django.http import JsonResponse



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
    

class TipoServicoUpdateView(LoginRequiredMixin, UpdateView):
    model = TipoServico
    template_name = 'tipo_servico_create_up.html'
    success_url = reverse_lazy('apps:atendimento:tipo_servico_list')
    form_class = TipoForm

    def get_context_data(self, **kwargs):
        context = super(TipoServicoUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Editar Tipo de Serviço'
        context['action'] = 'edit'
        context['url'] = reverse_lazy('apps:atendimento:tipo_servico_update', kwargs={'pk': self.object.pk})
        return context
    
    def get_queryset(self):
        return TipoServico.objects.all().order_by('descricao')


class TipoServicoDeleteView(LoginRequiredMixin, DeleteView):
    model = TipoServico
    template_name = 'tipo_servico_delete.html'
    success_url = reverse_lazy('apps:atendimento:tipo_servico_list')

    def get_context_data(self, **kwargs):
        context = super(TipoServicoDeleteView, self).get_context_data(**kwargs)
        context['title'] = 'Excluir Tipo de Serviço'
        context['action'] = 'delete'
        return context

    def get_queryset(self):
        return TipoServico.objects.all().order_by('descricao')


     
def get_servico_value(request, pk):
    servico = TipoServico.objects.get(pk=pk)
    return JsonResponse(
        {'preco': servico.preco, 'nome': servico.descricao},safe=False
    )