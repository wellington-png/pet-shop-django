from django.forms import ModelForm
from apps.core.models import Cliente


class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ("cpf", "nome", "logradoro", "cidade", "uf", "cep","contato")
        
    
    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
        self.fields['cpf'].widget.attrs['class'] = 'form-control'
        self.fields['cep'].widget.attrs['class'] = 'form-control'
        self.fields['cidade'].widget.attrs['class'] = 'form-control'
        self.fields['uf'].widget.attrs['class'] = 'form-control'
        self.fields['contato'].widget.attrs['class'] = 'form-control'
        self.fields['nome'].widget.attrs['class'] = 'form-control'
        self.fields['logradoro'].widget.attrs['class'] = 'form-control'
    
    def savar(self, commit=True):
        cliente = super(ClienteForm, self).save(commit=False)
        cliente.save()
        return cliente
