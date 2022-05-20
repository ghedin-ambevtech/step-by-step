"""
Crie um sistema de cadastro de clientes que seja possível, criar, listar, atualizar e deletar um cliente.

Sistema em DOS, utilizando o que aprendemos até agora, armazene em memória em um lista!

"""
from time import sleep, time
from uuid import uuid4


def incluir_cliente(nome:str):
    """
     Função de cadastramento de clientes
    """
    cliente = {}
    cliente["Nome"] = nome.title()
    id_cliente = str(uuid4())[0:5]
    cliente["Id"] = id_cliente
    clientes.append(cliente)
    print(f"Cliente {nome} cadastrado com sucesso!")


def alterar_cliente(nome: str):
    """
     Função de alteração cadastral de clientes
    """
    alterado = None
    for cliente in clientes:
        if id_cliente == cliente.get('Id'):
            nome = input(f"Você quer alterar o nome de {cliente.get('Nome')} para qual nome ? ").strip()
            cliente['Nome'] = nome
            print(f"Cliente {id_cliente} alterado com sucesso!")
            alterado = True
            break
    if not alterado:
        print(f"Id {id_cliente} não encontrado!")


def destroy_cliente(id: str):
    """
     Função de exclusão de clientes
    """
    deletado = None
    for cliente in clientes:
        if id_cliente == cliente.get('Id'):
            nome = cliente.get('Nome')
            index = clientes.index(cliente)
            del clientes[index]
            print(f"{nome} de id: {id_cliente} deletado com sucesso!")
            deletado = True
            break
    if not deletado:
        print(f"Id {id_cliente} não encontrado!")


def contagem_regressiva(n: int):
    while n > 0:
        print(f"Saindo do sistema em {n}...")
        n -= 1
        sleep(1)


# clientes = [{"Id": "1", "Nome": "Douglas"}]
clientes = []

print("###########    Sistema de Cadastro de Clientes    ###########")
while True:
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Atualizar")
    print("4 - Deletar")
    print("0 - Sair")
    menu = input("O que você deseja fazer ? ").strip()

    match menu:
        case "1":
            nome = input("Nome do cliente: ").strip()
            incluir_cliente(nome)
        case "2":
            if len(clientes) == 0:
                print("Nenhum cliente cadastrado!")
            [print(cliente) for cliente in clientes]
        case "3":
            print("Atualizar dados de um cliente")
            id_cliente = input("Digite o id do cliente que deseja alterar: ").strip()
            alterar_cliente(nome)
        case "4": # do original eu troquei o pop pelo del setei a flag de deletado quando excluiu e tirei o if de
                  # dentro do for.
            print("Deletar um cliente")
            id_cliente = input("Digite o id do cliente que deseja deletar: ").strip()
            destroy_cliente(id_cliente)
        case "0":
            contagem_regressiva(3)
            break
