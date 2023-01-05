from apps.account.models import Atendente
from django.contrib.auth.forms import UserCreationForm, UsernameField


class AtendenteForm(UserCreationForm):
    class Meta:
        model = Atendente
        fields = (
            "name",
            "email",
            "username",
            "cpf",
            "logradouro",
            "cidade",
            "uf",
            "cep",
            "contato",
            "salario",
            "cra",
        )
        field_classes = {"username": UsernameField}

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({"class": "form-control"})
        self.fields["name"].widget.attrs.update({"class": "form-control"})
        self.fields["email"].widget.attrs.update({"class": "form-control"})
        self.fields["password1"].widget.attrs.update({"class": "form-control"})
        self.fields["password2"].widget.attrs.update({"class": "form-control"})
        self.fields["cpf"].widget.attrs.update({"class": "form-control"})
        self.fields["logradouro"].widget.attrs.update({"class": "form-control"})
        self.fields["cidade"].widget.attrs.update({"class": "form-control"})
        self.fields["uf"].widget.attrs.update({"class": "form-control"})
        self.fields["cep"].widget.attrs.update({"class": "form-control"})
        self.fields["contato"].widget.attrs.update({"class": "form-control"})
        self.fields["salario"].widget.attrs.update({"class": "form-control"})
        self.fields["cra"].widget.attrs.update({"class": "form-control"})
        self.fields["username"].label = "Usuário"
        self.fields["name"].label = "Nome"
        self.fields["email"].label = "E-mail"
        self.fields["password1"].label = "Senha"
        self.fields["password2"].label = "Confirmação de senha"
        self.fields["cra"].label = "CRA"

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
