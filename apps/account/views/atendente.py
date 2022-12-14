from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from apps.account.forms import AtendenteForm
from apps.account.models import Atendente
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class AtendenteListView(LoginRequiredMixin, ListView):
    model = Atendente
    template_name = 'atendente/list.html'
    login_url = reverse_lazy('account_atendente_login')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listar Atendentes'
        return context

class AtendenteCreateView(LoginRequiredMixin, CreateView):
     model = Atendente
     form_class = AtendenteForm
     template_name = 'atendente/create.html'
     login_url = reverse_lazy('account_atendente_login')
     success_url = reverse_lazy('apps:core:home')
     
     
     def get_context_data(self, **kwargs):
         context = super().get_context_data(**kwargs)
         context['title'] = 'Crear Atendente'
         return context
     

class AtendenteUpdateView(LoginRequiredMixin, UpdateView):
     model = Atendente
     form_class = AtendenteForm
     template_name = 'atendente/form.html'
     login_url = reverse_lazy('account_atendente_login')
     success_url = reverse_lazy('atendente:atendente_list')
     
     
     def get_context_data(self, **kwargs):
         context = super().get_context_data(**kwargs)
         context['title'] = 'Actualizar Atendente'
         return context


class AtendenteDeleteView(LoginRequiredMixin, DeleteView):
    model = Atendente
    template_name = 'atendente/delete.html'
    login_url = reverse_lazy('account_atendente_login')
    success_url = reverse_lazy('atendente:atendente_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Excluir Atendente'
        return context
