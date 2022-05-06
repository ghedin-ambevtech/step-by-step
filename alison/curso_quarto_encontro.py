# Listas, tuplas, set
lista = [1, 'a', [], True]

print(lista)

lista.append(3)

print(lista)

valor_removido = lista.pop()
print(f'Valor removido:{valor_removido}')
print(lista)

lista2 = [1, 9, 13, 8, 3, 17]

lista2.sort()
print(lista2)

lista2.sort(reverse=True)
print(lista2)


# Tuplas
tupla = (5, 9, 5, 6, 15, 3, 511)

# sorteada = tupla.sort()

# print(sorteada)

# Dictionary
payload = {
    "nome": "Alison",
    "Idade": 25,
    "Notas": [5, 6, 7]
}

print(payload['nome'])
print(sum(payload['Notas']) / len(payload["Notas"]))


# Set
meu_set = {1, 2, 3, 4, 3}

meu_set.add(9)

print(meu_set)

