class Classe:
    pass


class PessoaFisica:
    pass


# class Pessoa:
#     def __init__(self, nome: str, sexo: str, cpf: str):
#         self.nome = nome
#         self.sexo = sexo
#         self.cpf = cpf
#
#
# cpf_original = "25678724-92"
# cpf_original = cpf_original.zfill(12)
#
# pessoa_1 = Pessoa("João", "M", cpf_original)
# print(pessoa_1.__dict__)


# class Pessoa:
#     def __init__(self, nome: str, sexo: str, cpf: str, ativo: bool = False):
#         self.nome = nome
#         self.sexo = sexo
#         self.cpf = cpf
#         self.ativo = ativo
#
#     def desativar(self):
#         self.ativo = False
#         print('A pessoa foi desativada com sucesso!!')
#


# if __name__ == "__main__":
#     cpf_original = "25678724-92"
#     cpf_original = cpf_original.zfill(12)
#     pessoa_1 = Pessoa("João", "M", cpf_original, True)
#     pessoa_1.desativar()
#
# print(pessoa_1.__dict__)


# Atributos protegidos
#
# Public: acessiveis de qualquer local do projeto
# Private: acessiveis para serem invocados, acessados e modificados somente por seu proprio objeto
# Protected: só podem ser invocados, acessados e modificados por classes que herdam de outra classe através
# do conceito de herança(classe filha/classe pai)
# pra acessar e modificar atributos protegidos, utilizamos getters and setters

#
# class Pessoa:
#     def __init__(self, nome: str, sexo: str, cpf: str, ativo: bool):
#         self.nome = nome
#         self.sexo = sexo
#         self.cpf = cpf
#         self.__ativo = ativo
#
#     def get_situacao(self, __ativo: bool):
#         return self.__ativo
#
#     def set_situacao(self, __ativo: bool):
#         self.__ativo = False
#
#
# if __name__ == "__main__":
#     cpf_original = "25678724-92"
#     cpf_original = cpf_original.zfill(12)
#     pessoa_1 = Pessoa("João", "M", cpf_original, True)
#     pessoa_1.set_situacao(False)
#     print(pessoa_1.__dict__)


# class Animal:
#     def __init__(self, nome: str, sexo: str):
#         self.__nome = nome
#         self.__sexo = sexo
#
#     def comer(self):
#         return f'O(A) {self.__nome} está comendo...'
#
#     def get_sexo(self):
#         return f'{self.__nome} é do sexo {self.__sexo}'
#
#     def set_sexo(self, sexo):
#         self.__sexo = sexo
#
#     def get_nome(self):
#         return f'O nome desse animal é {self.__nome}'
#
#     def set_nome(self, nome):
#         self.__nome = nome
#
#
# class Gato(Animal):
#     def __init__(self, nome: str, sexo: str):
#         super().__init__(nome, sexo)
#
#
# class Cachorro(Animal):
#     def __init__(self, nome: str, sexo: str):
#         super().__init__(nome, sexo)
#
#
# class Coelho(Animal):
#     def __init__(self, nome: str, sexo: str):
#         super().__init__(nome, sexo)
#
#
# if __name__ == "__main__":
#     gato = Gato("Snarf", "M")
#     cahorro = Cachorro("Lilith", "F")
#     coelho = Coelho("Pantufa", "F")
#     print(gato.get_sexo())
#     print(coelho.get_sexo())
#     print(cahorro.get_nome())
#     print(cahorro.comer())

# Polimorfismo:
# É a capacidade que uma subclasse tem de ter métodos com o mesmo nome de sua
# superclasse, e o programa saber qual método deve ser invocado, especificamente(da super ou da sub)

class Super:
    def teste(self):
        print('teste 1')

    def teste5(self):
        print('teste 1')

teste = Super()
teste.teste()


class Sub(Super):
    def teste2(self):
        print('teste2')

    def teste(self):
        print('teste 2')


sequencia = Sub()
sequencia.teste()


class SubSub(Sub):
    def teste2(self):
        print('teste 4')

    def teste(self):
        print('teste 3')

    @staticmethod                      # esse método é usado somente nessa classe que tem heranças
    def teste6():                      # sugar-syntax como @staticmethod e não ter parametros nem self
        print('teste 6')

    def teste5(self):
        print('teste 5')


final = SubSub()
final.teste()
final.teste2()
final.teste5()
final.teste6()


# from datetime import date
#
#
# class Person:
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age
#
#     @classmethod  # é um método geralmente usado pra criar construtores de classe.
#                       # Pra chamar não é necessário instanciar a classe
#     def from_birth_year(cls, name, year):
#         return cls(name, date.today().year - year)
#
#     @ staticmethod  # é um método que não modifica atributos da classe diretamente
#     def is_adult(age):
#         return age > 18
#
#
# person1 = Person('João', 21)
# person2 = Person.from_birth_year('Ana', 1986)
#
# print(person1.age)
# print(person2.age)
# print(person2.is_adult(person2.age))


from datetime import date


class Name:
    def __init__(self, name:str):
        self.name = name


class Person:  # aqui a classe person recebe um atributo que é um objeto de outra classe "Name".
    def __init__(self, name: Name, age: int):      # Pra criar Person é necessario person ter instanciado um objeto
        self.name = name                           # para aí entrar como atributo da classe person
        self.age = age


alison = Name('Alison')
person1 = Person(alison, 21)

print(person1.age)
print(person1.name.name)