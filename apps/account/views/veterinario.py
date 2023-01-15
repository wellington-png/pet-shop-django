from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from apps.account.forms import VeterinarioForm
from apps.account.models import Veterinario
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class VeterinarioCreateView(LoginRequiredMixin, CreateView):
    model = Veterinario
    form_class = VeterinarioForm
    template_name = 'veterinario/create.html'
    success_url = reverse_lazy('apps:account:veterinario_list')
    login_url = reverse_lazy('apps:core:home')
    success_message = "Veterinario criado com sucesso."
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Novo Veterinario'
        return context


class VeterinarioUpdateView(LoginRequiredMixin, UpdateView):
    model = Veterinario
    form_class = VeterinarioForm
    template_name = 'veterinario/update.html'
    success_url = reverse_lazy('apps:account:veterinario_list')
    login_url = reverse_lazy('apps:core:home')
    success_message = "Veterinario atualizado com sucesso."
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Atualizar Veterinario'
        return context
    

class VeterinarioDeleteView(LoginRequiredMixin, DeleteView):
    model = Veterinario
    template_name = 'veterinario/delete.html'
    success_url = reverse_lazy('apps:account:veterinario_list')
    login_url = reverse_lazy('apps:core:home')
    success_message = "Veterinario excluido com sucesso."
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Excluir Veterinario'
        return context


class VeterinarioListView(LoginRequiredMixin, ListView):
    model = Veterinario
    template_name ='veterinario/list.html'
    login_url = reverse_lazy('apps:core:home')
    context_object_name = 'veterinarios'
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listar Veterinarios'
        return context

