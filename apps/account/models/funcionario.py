from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db.models import CharField, EmailField, BooleanField, DecimalField

from apps.core.models import BaseModel

class UserManager(BaseUserManager):
    def create_user(self, username, name, email, cpf, logradouro, cidade, uf, cep, contato, salario, password=None):
        if not username:
            raise ValueError('O usuário precisa de um email')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            name=name
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

 
    def teste(self):
        print('teste')
    
    def create(self, **kwargs):
        print('create')
        return self.create_user(**kwargs)
       

    def create_superuser(self, username, name, email, password):
        user = self.create_user(
            username,
            name=name,
            email=self.normalize_email(email),
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user



class Funcionario(AbstractBaseUser, PermissionsMixin, BaseModel):
    name = CharField(verbose_name="nome completo", max_length=255)
    email = EmailField("endereço de e-mail", unique=True)
    username = CharField("Username", unique=True, max_length=255)
    is_staff = BooleanField("status de admin", default=False)
    is_active = BooleanField("ativo", default=True)
    cpf = CharField("CPF", max_length=255)
    logradouro = CharField("logradouro", max_length=255)
    cidade = CharField("cidade", max_length=255)
    uf = CharField("UF", max_length=255)
    cep = CharField("CEP", max_length=255)
    contato = CharField("contato", max_length=255)
    salario = DecimalField("salário", max_digits=10, decimal_places=2, default=0.00)
    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["name", "email"]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "usuário"
        verbose_name_plural = "usuários"
        ordering = ["name", "created_at"]
     
    def __str__(self):
        return self.username

