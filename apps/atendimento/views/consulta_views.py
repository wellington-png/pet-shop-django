from django.views.generic import CreateView, UpdateView, ListView, DetailView, View
from apps.atendimento.forms import ConsultaForm, ItemConsultaForm
from django.shortcuts import redirect
from apps.atendimento.models import Consulta, ItemConsulta
from django.forms import inlineformset_factory
from django.contrib.auth.mixins import LoginRequiredMixin


class ConsultaCreateView(LoginRequiredMixin, CreateView):
    model = ItemConsulta
    template_name = 'consulta_create.html'
    success_url = '/consulta/list'
    form_class = ConsultaForm

    item_order_formset = inlineformset_factory(Consulta, ItemConsulta, form=ItemConsultaForm, extra=1, can_delete=True)

    def form_valid(self, form):
        self.object = form.save()
        formset = self.item_order_formset(self.request.POST, instance=self.object)
        print(formset.data)
        if formset.is_valid():
            formset.save()
            return redirect(self.success_url)
        else:
            return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        context = super(ConsultaCreateView, self).get_context_data(**kwargs)
        context['formset'] = self.item_order_formset(instance=self.object)
        context['title'] = 'Cadastrar Serviço'
        context['action'] = 'add'
        print(context['formset'], '4567890-++++++++++++++++++++++')
        return context
    
    

class ConsultaListView(LoginRequiredMixin, ListView):
    model = Consulta
    template_name = 'consulta_list.html'
    context_object_name = 'consultas'
    paginate_by = 10



    

# class ConsultaUpdateView(UpdateView):
#     model = Consulta
#     fields = '__all__'
#     template_name = 'consulta_form.html'
#     success_url = '/consulta/list'


# class ConsultaDetailView(DetailView):
#     model = Consulta
#     template_name = 'consulta_detail.html'
#     context_object_name = 'consulta'