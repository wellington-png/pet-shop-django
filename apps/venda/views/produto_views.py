from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from apps.venda.models import Produto
from apps.venda.forms import ProdutoForm
from django.http import JsonResponse


class ProdutoCreateView(LoginRequiredMixin, CreateView):
    model = Produto
    form_class = ProdutoForm
    success_url = reverse_lazy('apps:venda:produto_list')
    template_name = "produto_create.html"

    def get_context_data(self, **kwargs):
        context = super(ProdutoCreateView, self).get_context_data(**kwargs)
        context['title_complete'] = "Produto"
        return context


class ProdutoListView(LoginRequiredMixin, ListView):
    model = Produto
    template_name = "produto_list.html"
    context_object_name = "produtos"
    paginate_by = 10
    
    
    def get_context_data(self, **kwargs):
        context = super(ProdutoListView, self).get_context_data(**kwargs)
        context['title'] = "Lista de Produtos"
        return context
     
    def get_queryset(self):
        return Produto.objects.all()

class ProdutoUpdateView(LoginRequiredMixin, UpdateView):
    model = Produto
    form_class = ProdutoForm
    success_url = reverse_lazy('apps:venda:produto_list')
    template_name = "produto_update.html"

    def get_context_data(self, **kwargs):
        context = super(ProdutoUpdateView, self).get_context_data(**kwargs)
        context['title_complete'] = "Produto"
        return context

class ProdutoDeleteView(LoginRequiredMixin, DeleteView):
    model = Produto
    success_url = reverse_lazy('apps:venda:produto_list')
    template_name = "produto_delete.html"

    def get_context_data(self, **kwargs):
        context = super(ProdutoDeleteView, self).get_context_data(**kwargs)
        context['title_complete'] = "Produto"
        return context


def get_produto_value(request, pk):
    produto = Produto.objects.get(pk=pk)
    return JsonResponse(
        {'preco': produto.preco, 'nome': produto.nome},safe=False
    )

    