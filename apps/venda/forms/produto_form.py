from django.forms import ModelForm
from apps.venda.models import Produto



class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = 'nome', 'preco', 'descricao', 'imagem'

    def __init__(self, *args, **kwargs):
        super(ProdutoForm, self).__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs['class'] = 'form-control'
        self.fields['preco'].widget.attrs['class'] = 'form-control'
        self.fields['descricao'].widget.attrs['class'] = 'form-control'
        self.fields['imagem'].widget.attrs['class'] = 'form-control mb-5'

    def save(self, commit=True):
        produto = super(ProdutoForm, self).save(commit=False)
        produto.save()
        return produto

