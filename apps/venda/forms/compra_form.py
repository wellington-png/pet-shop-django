from django.forms import ModelForm
from apps.venda.models import Compra, ItemCompra, Produto
from apps.account.models import  Atendente
from apps.core.models import Cliente

from django.utils.timezone import now

class CompraForm(ModelForm):
    class Meta:
        model = Compra

        fields = 'cliente', 'atendente', 'data_compra', 'valor_total'
    
    def __init__(self, *args, **kwargs):
        super(CompraForm, self).__init__(*args, **kwargs)
        self.fields['cliente'].queryset = Cliente.objects.all()
        self.fields['atendente'].queryset = Atendente.objects.all()
        self.fields['data_compra'].initial = now()
        self.fields['valor_total'].initial = 0.00
        self.fields['cliente'].widget.attrs['class'] = 'form-control js-example-basic-single w-100 select2-hidden-accessible'
        self.fields['atendente'].widget.attrs['class'] = 'form-control js-example-basic-single w-100 select2-hidden-accessible'
        self.fields['data_compra'].widget.attrs['class'] = 'form-control'
        self.fields['valor_total'].widget.attrs['class'] = 'form-control'
        self.fields['data_compra'].widget.attrs['placeholder'] = 'dd/mm/aaaa'
        self.fields['data_compra'].widget.attrs['type'] = 'date'
        
    def save(self, commit=True):
        print(self.cleaned_data)
        compra = super(CompraForm, self).save(commit=False)
        compra.save()
        return compra


class ItemCompraForm(ModelForm):
    class Meta:
        model = ItemCompra
        fields = 'compra', 'produto', 'quantidade'

    def __init__(self, *args, **kwargs):
        super(ItemCompraForm, self).__init__(*args, **kwargs)
        self.fields['compra'].queryset = Compra.objects.all()
        self.fields['produto'].queryset = Produto.objects.all()

        self.fields['compra'].widget.attrs['class'] = 'form-control'
        self.fields['produto'].widget.attrs['class'] = 'form-control'
        self.fields['quantidade'].widget.attrs['class'] = 'form-control'

    def save(self, commit=True):
        print(self.cleaned_data)
        item_compra = super(ItemCompraForm, self).save(commit=False)
        item_compra.save()
        return item_compra


    