from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from apps.core.forms import PetForm
from apps.core.models import Pet


class PetCreateView(LoginRequiredMixin, CreateView):
    model = Pet
    form_class = PetForm
    template_name = "pets/pets_form.html"
    success_url = reverse_lazy('apps:core:pet_list')

    def get_context_data(self, **kwargs):
        context = super(PetCreateView, self).get_context_data(**kwargs)
        context["title"] = "Novo Pet"
        return context


class PetListView(LoginRequiredMixin, ListView):
    model = Pet
    template_name = "pets/pets_list.html"
    context_object_name = "pets"
    paginate_by = 10
    queryset = Pet.objects.all()
    ordering = ["-id"]
    
    def get_context_data(self, **kwargs):
        context = super(PetListView, self).get_context_data(**kwargs)
        context["title"] = "Pets"
        return context
    
    def get_queryset(self):
        return Pet.objects.all().order_by("-id")
    

class PetUpdateView(LoginRequiredMixin, UpdateView):
    model = Pet
    form_class = PetForm
    template_name = "pets/pets_form.html"
    success_url = reverse_lazy('apps:core:pet_list')


    def get_context_data(self, **kwargs):
        context = super(PetUpdateView, self).get_context_data(**kwargs)
        context["title"] = "Editar Pet"
        return context
    

class PetDeleteView(LoginRequiredMixin, DeleteView):
    model = Pet
    template_name = "pets/pets_delete.html"
    success_url = reverse_lazy('apps:core:pet_list')

    def get_context_data(self, **kwargs):
        context = super(PetDeleteView, self).get_context_data(**kwargs)
        context["title"] = "Excluir Pet"
        return context

