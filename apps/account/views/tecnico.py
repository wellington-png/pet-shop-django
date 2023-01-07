from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from apps.account.forms import TecnicoForm
from django.shortcuts import redirect
from apps.account.models import Tecnico
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class TecnicoCreateView(LoginRequiredMixin, CreateView):
    model = Tecnico
    form_class = TecnicoForm
    template_name = 'tecnico/create.html'
    success_url = reverse_lazy('apps:core:home')
    login_url = reverse_lazy('account_tecnico_login')
    success_message = "Tecnico criado com sucesso."
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Novo Tecnico'
        return context

class TecnicoUpdateView(LoginRequiredMixin, UpdateView):
    model = Tecnico
    form_class = TecnicoForm
    template_name = 'tecnico/update.html'
    success_url = reverse_lazy('apps:account:list')
    login_url = reverse_lazy('account_tecnico_login')
    success_message = "Tecnico atualizado com sucesso."
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Atualizar Tecnico'
        return context

class TecnicoDeleteView(LoginRequiredMixin, DeleteView):
    model = Tecnico
    template_name = 'tecnico/delete.html'
    success_url = reverse_lazy('apps:account:list')
    login_url = reverse_lazy('account_tecnico_login')
    success_message = "Tecnico excluido com sucesso."
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Excluir Tecnico'
        return context
    

class TecnicoListView(LoginRequiredMixin, ListView):
    model = Tecnico
    template_name = 'tecnico/list.html'
    login_url = reverse_lazy('account_tecnico_login')
    context_object_name = 'tecnicos'
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listar Tecnicos'
        return context