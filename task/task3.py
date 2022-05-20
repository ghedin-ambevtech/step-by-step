"""
Crie um sistema de cadastro de customers que seja possível, criar, list, atualizar e deletar um customer.

Sistema em DOS, utilizando o que aprendemos até agora, armazene em memória em um lista!

"""
from time import sleep
from uuid import uuid4
from typing import NoReturn

customers = []


def validate_customers() -> NoReturn:
    if len(customers) == 0:
        print("Nenhum customer cadastrado!")


def list_customers() -> NoReturn:
    list_of_customers = [customer for customer in customers]
    print(f"Lista de clientes: {list_of_customers}")


def create_customer() -> NoReturn:
    """
     Função de cadastramento de clientes
    """
    customer = {}
    id_customer = str(uuid4())[0:5]
    customer["Id"] = id_customer
    name = input("Nome do cliente: ").strip()
    customer["Name"] = name.title()
    customers.append(customer)
    print(f"Cliente {customer['Name']} cadastrado com sucesso!")


def update_customer() -> NoReturn:
    """
     Função de alteração cadastral de clientes
    """
    print("Atualizar dados de um cliente")
    id_customer = input("Digite o id do cliente que deseja alterar: ").strip()
    updated = None
    for customer in customers:
        if id_customer == customer.get('Id'):
            name = input(f"Você quer alterar o name de {customer.get('Nome')} para qual nome ? ").strip()
            customer['Name'] = name.title()
            print(f"Cliente {id_customer} alterado com sucesso!")
            updated = True
            break
    if not updated:
        not_found(id_customer)


def destroy_customer() -> NoReturn:
    """
     Função de exclusão de clientes
    """
    print("Excluir um cliente")
    id_customer = input("Digite o id do cliente que deseja excluir: ").strip()
    excluded = None
    for customer in customers:
        if id_customer == customer.get('Id'):
            name = customer.get('Name')
            index = customers.index(customer)
            del customers[index]
            print(f"{name} de id: {id_customer} excluído com sucesso!")
            excluded = True
            break
    if not excluded:
        not_found(id_customer)


def contagem_regressiva(n: int) -> NoReturn:
    while n > 0:
        print(f"Saindo do sistema em {n}...")
        n -= 1
        sleep(1)


def not_found(_id: str) -> NoReturn:
    print(f'ID: {_id} não encontrado!')


def menu_opcoes() -> int:
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Atualizar")
    print("4 - Deletar")
    print("0 - Sair")
    return int(input("O que você deseja fazer ? ").strip())


def is_running() -> bool:
    menu = menu_opcoes()

    if menu == 1:
        create_customer()
        return True
    elif menu == 2:
        validate_customers()
        list_customers()
        return True
    elif menu == 3:
        update_customer()
        return True
    elif menu == 4:
        destroy_customer()
        return True
    elif menu == 0:
        contagem_regressiva(3)
        return False
    else:
        print('Opção inválida!')
        return True


print("###########    Sistema de Cadastro de Clientes    ###########")
while True:
    if not is_running():
        break
