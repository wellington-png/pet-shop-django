from django.db.models import CharField

from apps.core.models import BaseModel


class Cliente(BaseModel):
    UF_CHOICES = (
    ('AC', 'Acre'), 
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranão'),
    ('MG', 'Minas Gerais'),
    ('MS', 'Mato Grosso do Sul'),
    ('MT', 'Mato Grosso'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PE', 'Pernanbuco'),
    ('PI', 'Piauí'),
    ('PR', 'Paraná'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RO', 'Rondônia'),
    ('RR', 'Roraima'),
    ('RS', 'Rio Grande do Sul'),
    ('SC', 'Santa Catarina'),
    ('SE', 'Sergipe'),
    ('SP', 'São Paulo'),
    ('TO', 'Tocantins')
)
    
    cpf = CharField(max_length=255, verbose_name='CPF')
    nome = CharField(max_length=255, verbose_name='Nome')
    logradoro = CharField(max_length=255, verbose_name='Logradoro')
    cidade = CharField(max_length=255, verbose_name='Cidade', choices=UF_CHOICES)
    uf = CharField(max_length=255, verbose_name='UF')
    cep = CharField(max_length=255, verbose_name='CEP')
    contato = CharField(max_length=255, verbose_name='Contato')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['-id']