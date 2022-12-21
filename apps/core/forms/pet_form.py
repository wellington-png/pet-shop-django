from django.forms import ModelForm
from apps.core.models import Pet


class PetForm(ModelForm):
    class Meta:
        model = Pet
        fields = ("nome", "raca", "peso", "data_nascimento", "sexo", "especie", "porte", "pelagem", "cliente")
        
    def __init__(self, *args, **kwargs):
         super(PetForm, self).__init__(*args, **kwargs)
         self.fields["nome"].label = "Nome"
         self.fields["raca"].label = "Raca"
         self.fields["peso"].label = "Peso"
         self.fields["data_nascimento"].label = "Data Nascimento"
         self.fields["sexo"].label = "Sexo"
         self.fields["especie"].label = "Especie"
         self.fields["porte"].label = "Porte"
         self.fields["pelagem"].label = "Pelagem"
         self.fields["cliente"].label = "Cliente"
         
         self.fields["nome"].widget.attrs["class"] = "form-control"
         self.fields["raca"].widget.attrs["class"] = "form-control"
         self.fields["peso"].widget.attrs["class"] = "form-control"
         self.fields["data_nascimento"].widget.attrs["class"] = "form-control"
         self.fields["sexo"].widget.attrs["class"] = "form-control"
         self.fields["especie"].widget.attrs["class"] = "form-control"
         self.fields["porte"].widget.attrs["class"] = "form-control"
         self.fields["pelagem"].widget.attrs["class"] = "form-control"
         self.fields["cliente"].widget.attrs["class"] = "form-control"

    def save(self, commit=True):
        pet = super(PetForm, self).save(commit=False)
        pet.nome = self.cleaned_data["nome"]
        pet.raca = self.cleaned_data["raca"]
