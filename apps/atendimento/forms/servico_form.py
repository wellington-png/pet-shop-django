from django.forms import ModelForm
from apps.atendimento.models import Servico, ItemServico, TipoServico
from apps.account.models import  Tecnico
from apps.core.models import Pet


class ServicoForm(ModelForm):
    class Meta:
        model = Servico

    
        fields = 'pet', 'tecnico', 'data_servico', 'valor_total'

    def __init__(self, *args, **kwargs):
        super(ServicoForm, self).__init__(*args, **kwargs)
        self.fields['pet'].queryset = Pet.objects.all()

        self.fields['pet'].widget.attrs['class'] = 'form-control js-example-basic-single w-100 select2-hidden-accessible'
        self.fields['tecnico'].widget.attrs['class'] = 'form-control js-example-basic-single w-100 select2-hidden-accessible'
        self.fields['data_servico'].widget.attrs['class'] = 'form-control'
        self.fields['valor_total'].widget.attrs['class'] = 'form-control'
        self.fields['data_servico'].widget.attrs['placeholder'] = 'dd/mm/aaaa'
        self.fields['data_servico'].widget.attrs['type'] = 'date'
         
    def save(self, commit=True):
        servico = super(ServicoForm, self).save(commit=False)
        servico.save()
        return servico


class ItemServicoForm(ModelForm):
    class Meta:
        model = ItemServico
        fields = 'servico', 'tipo_servico', 'quantidade'

    def __init__(self, *args, **kwargs):
        super(ItemServicoForm, self).__init__(*args, **kwargs)
        self.fields['servico'].queryset = Servico.objects.all()
        self.fields['tipo_servico'].queryset = TipoServico.objects.all()

        self.fields['servico'].widget.attrs['class'] = 'form-control'
        self.fields['tipo_servico'].widget.attrs['class'] = 'form-control'
        self.fields['quantidade'].widget.attrs['class'] = 'form-control'

    def save(self, commit=True):
        item_servico = super(ItemServicoForm, self).save(commit=False)
        item_servico.save()
        return item_servico