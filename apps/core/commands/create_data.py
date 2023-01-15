from apps.core.models import Cliente, Pet
from apps.account.models import Atendente, Tecnico, Veterinario
from apps.venda.models import Compra, ItemCompra, Produto, Estoque
from apps.atendimento.models import (
    Servico,
    TipoServico,
    Consulta,
    ItemConsulta,
    ItemServico,
)
from datetime import datetime

from faker import Faker

fake = Faker("pt_BR")


def create_data():
    for i in range(10):
        Cliente.objects.create(
            cpf=fake.cpf(),
            nome=fake.name(),
            logradoro=fake.street_name(),
            cidade=fake.city(),
            uf=fake.state(),
            cep=fake.postcode(),
            contato=fake.phone_number(),
        )
    for i in range(10):
        Pet.objects.create(
            nome=fake.name(),
            raca=fake.word(),
            peso=fake.pydecimal(left_digits=2, right_digits=1, positive=True),
            data_nascimento=datetime.now(),
            sexo=fake.word(),
            especie=fake.word(),
            porte=fake.word(),
            pelagem=fake.word(),
            cliente=Cliente.objects.first(),
        )

    for i in range(10):
        Atendente.objects.create(
            name=fake.name(),
            email=fake.email(),
            username=fake.user_name(),
            cpf=fake.cpf(),
            logradouro=fake.street_name(),
            cidade=fake.city(),
            uf=fake.state(),
            cep=fake.postcode(),
            contato=fake.phone_number(),
            salario=fake.pydecimal(left_digits=5, right_digits=2, positive=True),
            cra=fake.pydecimal(left_digits=5, right_digits=2, positive=True),
        )
    # from apps.core.commands.create_data import create_data
    for i in range(10):
        Tecnico.objects.create(
            name=fake.name(),
            email=fake.email(),
            username=fake.user_name(),
            cpf=fake.cpf(),
            logradouro=fake.street_name(),
            cidade=fake.city(),
            uf=fake.state(),
            cep=fake.postcode(),
            contato=fake.phone_number(),
            salario=fake.pydecimal(left_digits=5, right_digits=2, positive=True),
            crta=fake.pydecimal(left_digits=5, right_digits=2, positive=True),
        )

    for i in range(10):
        Veterinario.objects.create(
            name=fake.name(),
            email=fake.email(),
            username=fake.user_name(),
            cpf=f"{fake.cpf()}",
            logradouro=fake.street_name(),
            cidade=fake.city(),
            uf=fake.state(),
            cep=fake.postcode(),
            contato=fake.phone_number(),
            salario=fake.pydecimal(left_digits=5, right_digits=2, positive=True),
            crmv=fake.pydecimal(left_digits=5, right_digits=2, positive=True),
        )

    for i in range(10):
        Produto.objects.create(
            nome=fake.name(),
            descricao=fake.name(),
            preco=52.0,
        )

    for i in range(10):
        Estoque.objects.create(
            produto=Produto.objects.first(),
            quantidade=fake.pyint(),
        )

    for i in range(10):
        TipoServico.objects.create(
            descricao=fake.text(),
            preco=50.10,
        )
    for i in range(10):
        Compra.objects.create(
            cliente_id=fake.pyint(1, 10),
            atendente=Atendente.objects.first(),
            data_compra=datetime.now().date(),
        )

    for i in range(10):
        ItemCompra.objects.create(
            compra_id=fake.pyint(1, 10),
            produto_id=fake.pyint(1, 10),
            quantidade=fake.pyint(),
        )

    for i in range(10):
        Servico.objects.create(
            pet_id=fake.pyint(1, 10),
            tecnico=Tecnico.objects.first(),
            data_servico=datetime.now().date(),
        )

    for i in range(10):
        Consulta.objects.create(
            pet_id=fake.pyint(1, 10),
            veterinario=Veterinario.objects.first(),
            sintomas=fake.text(),
            diagnostico=fake.text(),
            tratamento=fake.text(),
            data_consulta=datetime.now().date(),
        )

    for i in range(10):
        ItemConsulta.objects.create(
            consulta_id=fake.pyint(1, 10),
            tipo_servico_id=fake.pyint(1, 10),
            quantidade=fake.pyint(),
        )

    for i in range(10):
        ItemServico.objects.create(
            servico_id=fake.pyint(1, 10),
            tipo_servico_id=fake.pyint(1, 10),
            quantidade=fake.pyint(),
        )


if __name__ == "__main__":
    create_data()
