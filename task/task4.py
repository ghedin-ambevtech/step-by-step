from time import sleep
from uuid import uuid4
from datetime import date
from typing import NoReturn

customers = []


class Customer:
    def __init__(self, id: str, name: str, age: int, address: str):
        self.id = id
        self.name = name
        self.age = age
        self.address = address

    @classmethod
    def create_customer_from_birth(cls, _id, name, year, address):
        return cls(_id, name, date.today().year - year, address)

    @staticmethod
    def validate_customers() -> NoReturn:
        if len(customers) == 0:
            print("Nenhum cliente cadastrado!")

    @staticmethod
    def list_customers() -> NoReturn:
        list_of_customers = [customer.id for customer in customers]
        print(f"Lista de clientes: {list_of_customers}")

    @staticmethod
    def create_customer() -> NoReturn:
        """
         Função de cadastramento de clientes
        """
        id_customer = str(uuid4())[0:5]
        name = input("Nome do cliente: ").strip().title()
        age = int(input("Digite o ano de nascimento do cliente: "))
        address = input("Digite o endereço do cliente: ")
        customer = Customer.create_customer_from_birth(id_customer, name, age, address)
        customers.append(customer)
        print(f"Cliente {customer.name} cadastrado com sucesso!")

    @staticmethod
    def update_customer() -> NoReturn:
        """
         Função de alteração cadastral de clientes
        """
        print("Atualizar dados de um cliente")
        id_customer = input("Digite o id do cliente que deseja alterar: ").strip()
        updated = None
        for customer in customers:
            if id_customer == customer.id:
                name = input(f"Você quer alterar o nome de {customer.name} para qual nome ? ").strip()
                customer.name = name.title()
                print(f"Cliente {customer.id} alterado com sucesso!")
                updated = True
                break
        if not updated:
            Customer.not_found(id_customer)

    @staticmethod
    def destroy_customer() -> NoReturn:
        """
         Função de exclusão de clientes
        """
        print("Excluir um cliente")
        id_customer = input("Digite o id do cliente que deseja excluir: ").strip()
        excluded = None
        for customer in customers:
            if id_customer == customer.id:
                name = customer.name
                index = customers.index(customer)
                del customers[index]
                print(f"{name} de id: {customer.id} excluído com sucesso!")
                excluded = True
                break
        if not excluded:
            Customer.not_found(id_customer)

    @staticmethod
    def contagem_regressiva(n: int) -> NoReturn:
        while n > 0:
            print(f"Saindo do sistema em {n}...")
            n -= 1
            sleep(1)

    @staticmethod
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
        Customer.create_customer()
        return True
    elif menu == 2:
        Customer.validate_customers()
        Customer.list_customers()
        return True
    elif menu == 3:
        Customer.update_customer()
        return True
    elif menu == 4:
        Customer.destroy_customer()
        return True
    elif menu == 0:
        Customer.contagem_regressiva(3)
        return False
    else:
        print('Opção inválida!')
        return True


print("###########    Sistema de Cadastro de Clientes    ###########")
while True:
    if not is_running():
        break
