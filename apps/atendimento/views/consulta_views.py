from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from apps.atendimento.forms import ConsultaForm, ItemConsultaForm
from django.shortcuts import redirect
from django.urls import reverse_lazy
from apps.atendimento.models import Consulta, ItemConsulta
from django.forms import inlineformset_factory
from django.contrib.auth.mixins import LoginRequiredMixin


class ConsultaCreateView(LoginRequiredMixin, CreateView):
    model = ItemConsulta
    template_name = "consulta_create.html"
    success_url = reverse_lazy("apps:atendimento:consulta_list")
    form_class = ConsultaForm

    item_order_formset = inlineformset_factory(
        Consulta, ItemConsulta, form=ItemConsultaForm, extra=1, can_delete=True
    )

    def form_valid(self, form):
        self.object = form.save()
        formset = self.item_order_formset(self.request.POST, instance=self.object)
        if formset.is_valid():
            formset.save()
            return redirect(self.success_url)
        else:
            return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        context = super(ConsultaCreateView, self).get_context_data(**kwargs)
        context["formitem"] = self.item_order_formset(instance=self.object)
        context["title"] = "Cadastrar Serviço"
        context["action"] = "add"
        return context


class ConsultaListView(LoginRequiredMixin, ListView):
    model = Consulta
    template_name = "consulta_list.html"
    context_object_name = "consultas"
    paginate_by = 10


class ConsultaUpdateView(LoginRequiredMixin, UpdateView):
    model = Consulta
    template_name = "consulta_create_up.html"
    success_url = reverse_lazy("apps:atendimento:consulta_list")
    form_class = ConsultaForm

    item_order_formset = inlineformset_factory(
        Consulta, ItemConsulta, form=ItemConsultaForm, extra=1, can_delete=True
    )

    def form_valid(self, form):
        self.object = form.save()
        formset = self.item_order_formset(self.request.POST, instance=self.object)
        if formset.is_valid():
            formset.save()
            return redirect(self.success_url)
        else:
            return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        context = super(ConsultaUpdateView, self).get_context_data(**kwargs)
        context["formitem"] = self.item_order_formset(instance=self.object)
        context["title"] = "Editar Serviço"
        context["action"] = "edit"
        return context


class ConsultaDeleteView(LoginRequiredMixin, DeleteView):
    model = Consulta
    template_name = "consulta_delete.html"
    success_url = reverse_lazy("apps:atendimento:consulta_list")

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super(ConsultaDeleteView, self).get_context_data(**kwargs)
        context["title"] = "Remover Serviço"
        context["action"] = "delete"
        return context
