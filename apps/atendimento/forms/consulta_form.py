from django.forms import ModelForm, DateField
from apps.atendimento.models import Consulta, ItemConsulta, TipoServico
from apps.account.models import  Veterinario
from apps.core.models import Pet


class ConsultaForm(ModelForm):
    class Meta:
        model = Consulta

    
        fields = 'pet', 'veterinario', 'sintomas', 'diagnostico', 'tratamento', 'data_consulta', 'valor_total'

    def __init__(self, *args, **kwargs):
        super(ConsultaForm, self).__init__(*args, **kwargs)
        self.fields['pet'].queryset = Pet.objects.all()
        self.fields['veterinario'].queryset = Veterinario.objects.filter(fucionario_type='veterinario')

        self.fields['pet'].widget.attrs['class'] = 'form-control js-example-basic-single w-100 select2-hidden-accessible'
        self.fields['veterinario'].widget.attrs['class'] = 'form-control js-example-basic-single w-100 select2-hidden-accessible'
        self.fields['sintomas'].widget.attrs['class'] = 'form-control'
        self.fields['diagnostico'].widget.attrs['class'] = 'form-control'
        self.fields['diagnostico'].widget.attrs['class'] = 'form-control'
        self.fields['tratamento'].widget.attrs['class'] = 'form-control'
        self.fields['data_consulta'].widget.attrs['class'] = 'form-control'
        self.fields['valor_total'].widget.attrs['class'] = 'form-control'

        self.fields['data_consulta'].widget.attrs['placeholder'] = 'dd/mm/aaaa'
        self.fields['data_consulta'].widget.attrs['type'] = 'date'
         
    def save(self, commit=True):
        print(self.cleaned_data)
        consulta = super(ConsultaForm, self).save(commit=False)
        consulta.save()
        return consulta


class ItemConsultaForm(ModelForm):
    class Meta:
        model = ItemConsulta
        fields = 'consulta', 'tipo_servico', 'quantidade'

    def __init__(self, *args, **kwargs):
        super(ItemConsultaForm, self).__init__(*args, **kwargs)
        self.fields['consulta'].queryset = Consulta.objects.all()
        self.fields['tipo_servico'].queryset = TipoServico.objects.all()

        self.fields['consulta'].widget.attrs['class'] = 'form-control'
        self.fields['tipo_servico'].widget.attrs['class'] = 'form-control'
        self.fields['quantidade'].widget.attrs['class'] = 'form-control'

    def save(self, commit=True):
        print(self.cleaned_data)
        item_consulta = super(ItemConsultaForm, self).save(commit=False)
        item_consulta.save()
        return item_consulta
