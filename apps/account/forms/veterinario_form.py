from django.contrib.auth.forms import  UsernameField, UserCreationForm

from apps.account.models import  Veterinario


class VeterinarioForm(UserCreationForm):
    class Meta:
        model = Veterinario
        fields = ('username', 'name', 'email', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser', 'crmv')
        field_classes = {'username': UsernameField}

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})
        self.fields['username'].label = 'Usuário'
        self.fields['name'].label = 'Nome'
        self.fields['email'].label = 'E-mail'
        self.fields['password1'].label = 'Senha'
        self.fields['password2'].label = 'Confirmação de senha'
        self.fields['is_active'].label = 'Ativo'
        self.fields['is_staff'].label = 'Administrador'
        self.fields['is_superuser'].label = 'Super usuário'
        self.fields['crmv'].label = 'Crmv'

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user