from django.forms import ModelForm, DecimalField
from apps.venda.models import Compra, ItemCompra, Produto
from apps.account.models import  Atendente
from apps.core.models import Cliente

from django.utils.timezone import now

class CompraForm(ModelForm):
    class Meta:
        model = Compra

        fields = 'cliente', 'atendente', 'data_compra', 
    
    def __init__(self, *args, **kwargs):
        super(CompraForm, self).__init__(*args, **kwargs)
        self.fields['cliente'].queryset = Cliente.objects.all()
        self.fields['atendente'].queryset = Atendente.objects.all()
        self.fields['cliente'].widget.attrs['class'] = 'form-control js-example-basic-single w-100 select2-hidden-accessible'
        self.fields['atendente'].widget.attrs['class'] = 'form-control js-example-basic-single w-100 select2-hidden-accessible'
        
    def save(self, commit=True):
        compra = super(CompraForm, self).save(commit=False)
        compra.save()
        return compra


class ItemCompraForm(ModelForm):
    class Meta:
        model = ItemCompra
        fields = 'compra', 'produto', 'quantidade'

    def __init__(self, *args, **kwargs):
        super(ItemCompraForm, self).__init__(*args, **kwargs)
        self.fields['extra_field_valor'] = DecimalField(max_digits=10, decimal_places=2)
        self.fields['extra_field_valor'].widget.attrs['class'] = 'form-control valor'
        self.fields['extra_field_valor'].widget.attrs['readonly'] = True
        self.fields['extra_field_valor'].widget.attrs['id'] = 'valor'
        self.fields['extra_field_valor'].widget.attrs['required'] = False


        self.fields['extra_field_valor'].widget.attrs['onclick'] = "calcularValor()"
         
        self.fields['extra_field_valor_total'] = DecimalField(max_digits=10, decimal_places=2)
        self.fields['extra_field_valor_total'].widget.attrs['class'] = 'form-control valor_total'
        self.fields['extra_field_valor_total'].widget.attrs['readonly'] = True
        self.fields['extra_field_valor_total'].widget.attrs['required'] = 'false'

        
         
        
        

        self.fields['produto'].queryset = Produto.objects.all()
        
        
        self.fields['produto'].widget.attrs['class'] = 'form-control produto'
        self.fields['quantidade'].widget.attrs['class'] = 'form-control quantidade'
        self.fields['produto'].widget.attrs['onclick'] = "calcularValor()"
        self.fields['quantidade'].widget.attrs['onclick'] = "calcularValor()"
        

    def save(self, commit=True):
        item_compra = super(ItemCompraForm, self).save(commit=False)
        item_compra.save()
        return item_compra


    