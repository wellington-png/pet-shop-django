from django.forms import ModelForm
from apps.venda.models import Produto



class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = 'nome', 'preco', 'descricao'

    def __init__(self, *args, **kwargs):
        super(ProdutoForm, self).__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs['class'] = 'form-control'
        self.fields['preco'].widget.attrs['class'] = 'form-control'
        self.fields['descricao'].widget.attrs['class'] = 'form-control'

    def save(self, commit=True):
        print(self.cleaned_data)
        produto = super(ProdutoForm, self).save(commit=False)
        produto.save()
        return produto

