from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.forms import inlineformset_factory
from django.shortcuts import redirect

from apps.venda.models import Compra, ItemCompra
from apps.venda.forms import CompraForm, ItemCompraForm
from django.contrib.auth.mixins import LoginRequiredMixin


class CompraCreateView(LoginRequiredMixin, CreateView):
    model = Compra
    form_class = CompraForm
    template_name = 'compra_create.html'
    success_url = '/compra/listar'

    item_order_formset = inlineformset_factory(Compra, ItemCompra, form=ItemCompraForm, extra=1, can_delete=True)

    def form_valid(self, form):
        self.object = form.save()
        formset = self.item_order_formset(self.request.POST, instance=self.object)
        if formset.is_valid():
            formset.save()
            return redirect(self.success_url)
        else:
            return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        context = super(CompraCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Cadastrar Compras'
        context['action'] = 'add'
        context['formset'] = self.item_order_formset(instance=self.object)
        return context


class CompraListView(LoginRequiredMixin, ListView):
    model = Compra
    template_name = 'compra_list.html'
    context_object_name = 'compras'
    paginate_by = 10


class CompraUpdateView(LoginRequiredMixin, UpdateView):
    model = Compra
    form_class = CompraForm
    template_name = 'compra_create_up.html'
    success_url = '/compra/list'

    item_order_formset = inlineformset_factory(Compra, ItemCompra, form=ItemCompraForm, extra=1, can_delete=True)

    def form_valid(self, form):
        self.object = form.save()
        formset = self.item_order_formset(self.request.POST, instance=self.object)
        if formset.is_valid():
            formset.save()
            return redirect(self.success_url)
        else:
            return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        context = super(CompraUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Editar Compras'
        context['action'] = 'edit'
        context['formset'] = self.item_order_formset(instance=self.object)
        return context


class CompraDeleteView(LoginRequiredMixin, DeleteView):
    model = Compra
    template_name = 'compra_delete.html'
    success_url = '/compra/list'
    