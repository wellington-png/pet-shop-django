from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.forms import inlineformset_factory
from django.shortcuts import redirect
from django.urls import reverse_lazy
from apps.atendimento.models import Servico, ItemServico
from apps.atendimento.forms import ServicoForm, ItemServicoForm
from django.contrib.auth.mixins import LoginRequiredMixin


class ServicoCreateView(LoginRequiredMixin, CreateView):
    model = Servico
    form_class = ServicoForm
    template_name = "servico_create.html"
    success_url = reverse_lazy("apps:atendimento:servico_list")

    item_order_formset = inlineformset_factory(
        Servico, ItemServico, form=ItemServicoForm, extra=1, can_delete=True
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
        context = super(ServicoCreateView, self).get_context_data(**kwargs)
        context["title"] = "Cadastrar Serviço"
        context["action"] = "add"
        context["formitem"] = self.item_order_formset(instance=self.object)
        return context


class ServicoListView(LoginRequiredMixin, ListView):
    model = Servico
    template_name = "servico_list.html"
    context_object_name = "servicos"
    paginate_by = 10


class ServicoUpdateView(LoginRequiredMixin, UpdateView):
    model = Servico
    form_class = ServicoForm
    template_name = "servico_create_up.html"
    success_url = reverse_lazy("apps:atendimento:servico_list")

    item_order_formset = inlineformset_factory(
        Servico, ItemServico, form=ItemServicoForm, extra=1, can_delete=True
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
        context = super(ServicoUpdateView, self).get_context_data(**kwargs)
        context["title"] = "Alterar Serviço"
        context["action"] = "edit"
        context["formitem"] = self.item_order_formset(instance=self.object)
        return context


class ServicoDeleteView(LoginRequiredMixin, DeleteView):
    model = Servico
    template_name = "servico_delete.html"
    success_url = reverse_lazy("apps:atendimento:servico_list")

    def get_context_data(self, **kwargs):
        context = super(ServicoDeleteView, self).get_context_data(**kwargs)
        context["title"] = "Excluir Serviço"
        return context
