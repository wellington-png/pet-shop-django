from django.forms import ModelForm
from apps.atendimento.models import TipoServico


class TipoForm(ModelForm):
    class Meta:
        model = TipoServico
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(TipoForm, self).__init__(*args, **kwargs)
        self.fields['descricao'].widget.attrs['class'] = 'form-control'
        self.fields['descricao'].widget.attrs['placeholder'] = 'Descrição'
        self.fields['descricao'].label = ''
        self.fields['descricao'].help_text = ''
        self.fields['preco'].widget.attrs['class'] = 'form-control mt-2 mb-2'
        self.fields['preco'].widget.attrs['placeholder'] = 'Preço'
        self.fields['preco'].label = ''
        self.fields['preco'].help_text = ''