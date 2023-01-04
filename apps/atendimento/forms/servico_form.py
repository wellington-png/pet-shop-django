from django.forms import ModelForm, DecimalField
from apps.atendimento.models import Servico, ItemServico, TipoServico
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
        
        self.fields['extra_field_valor'] = DecimalField(max_digits=10, decimal_places=2)
        self.fields['extra_field_valor'].widget.attrs['class'] = 'form-control valor'
        self.fields['extra_field_valor'].widget.attrs['readonly'] = True
        self.fields['extra_field_valor'].widget.attrs['id'] = 'valor'

        # onclick="calcularValor()"
        self.fields['extra_field_valor'].widget.attrs['onclick'] = "calcularValor()"
         
        self.fields['extra_field_valor_total'] = DecimalField(max_digits=10, decimal_places=2)
        self.fields['extra_field_valor_total'].widget.attrs['class'] = 'form-control valor_total'
        self.fields['extra_field_valor_total'].widget.attrs['readonly'] = True
        
        
        self.fields['servico'].queryset = Servico.objects.all()
        self.fields['tipo_servico'].queryset = TipoServico.objects.all()

        self.fields['servico'].widget.attrs['class'] = 'form-control'
        self.fields['tipo_servico'].widget.attrs['class'] = 'form-control servico'
        self.fields['quantidade'].widget.attrs['class'] = 'form-control quantidade'
        self.fields['tipo_servico'].widget.attrs['onclick'] = "calcularValor()"
        self.fields['quantidade'].widget.attrs['onclick'] = "calcularValor()"

    def save(self, commit=True):
        item_servico = super(ItemServicoForm, self).save(commit=False)
        item_servico.save()
        return item_servico