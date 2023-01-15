from django.forms import ModelForm, DecimalField
from apps.atendimento.models import Consulta, ItemConsulta, TipoServico
from apps.account.models import Veterinario
from apps.core.models import Pet


class ConsultaForm(ModelForm):
    class Meta:
        model = Consulta

        fields = (
            "pet",
            "veterinario",
            "sintomas",
            "diagnostico",
            "tratamento",
            "data_consulta",
            "valor_total",
        )

    def __init__(self, *args, **kwargs):
        super(ConsultaForm, self).__init__(*args, **kwargs)
        self.fields["pet"].queryset = Pet.objects.all()
        self.fields["pet"].widget.attrs[
            "class"
        ] = "form-control js-example-basic-single w-100 select2-hidden-accessible"
        self.fields["veterinario"].widget.attrs[
            "class"
        ] = "form-control js-example-basic-single w-100 select2-hidden-accessible"
        self.fields["sintomas"].widget.attrs["class"] = "form-control"
        self.fields["diagnostico"].widget.attrs["class"] = "form-control"
        self.fields["tratamento"].widget.attrs["class"] = "form-control"
        self.fields["data_consulta"].widget.attrs["class"] = "form-control"
        self.fields["valor_total"].widget.attrs["class"] = "form-control"

        self.fields["data_consulta"].widget.attrs["placeholder"] = "dd/mm/aaaa"
        self.fields["data_consulta"].widget.attrs["type"] = "date"

    def save(self, commit=True):
        consulta = super(ConsultaForm, self).save(commit=False)
        consulta.save()
        return consulta


class ItemConsultaForm(ModelForm):
    class Meta:
        model = ItemConsulta
        fields = "consulta", "tipo_servico", "quantidade"

    def __init__(self, *args, **kwargs):
        super(ItemConsultaForm, self).__init__(*args, **kwargs)

        self.fields["extra_field_valor"] = DecimalField(max_digits=10, decimal_places=2)
        self.fields["extra_field_valor"].widget.attrs["class"] = "form-control valor"
        self.fields["extra_field_valor"].widget.attrs["readonly"] = True
        self.fields["extra_field_valor"].widget.attrs["id"] = "valor"
        self.fields["extra_field_valor"].widget.attrs["required"] = False

        self.fields["extra_field_valor"].widget.attrs["onclick"] = "calcularValor()"

        self.fields["extra_field_valor_total"] = DecimalField(
            max_digits=10, decimal_places=2
        )
        self.fields["extra_field_valor_total"].widget.attrs[
            "class"
        ] = "form-control valor_total"
        self.fields["extra_field_valor_total"].widget.attrs["readonly"] = True
        self.fields["extra_field_valor"].widget.attrs["required"] = False

        self.fields["consulta"].queryset = Consulta.objects.all()
        self.fields["tipo_servico"].queryset = TipoServico.objects.all()
        self.fields["tipo_servico"].widget.attrs["onclick"] = "calcularValor()"
        self.fields["quantidade"].widget.attrs["onclick"] = "calcularValor()"

        self.fields["consulta"].widget.attrs["class"] = "form-control"
        self.fields["tipo_servico"].widget.attrs["class"] = "form-control servico"
        self.fields["quantidade"].widget.attrs["class"] = "form-control quantidade"

    def save(self, commit=True):
        item_consulta = super(ItemConsultaForm, self).save(commit=False)
        item_consulta.save()
        return item_consulta
