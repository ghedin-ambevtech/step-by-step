# # EXERCÍCIOS Regex:
# 1 - Com Regex, conseguir mostrar o CPF 012.345.678-90 desta forma: 01234567890
# 2 - Faça um validador de Passwords aonde o usuario digite o seu password e o seu programa deve validar se é um password válido ou não, para isso use as regras:
# a - Deve conter mais de 8 caracteres
# b - Deve conter ao menos uma Letra Maiúscula
# c - Deve conter ao menos 2 numeros
# d - Deve conter pelo menos 1 caractere especial
# e - deve conter pelo menos 2 letras minusculas
# 3 - Na frase 'avistamos estáticos o elastico e o plastico' quero retornar os caracteres "a" ou "e" ou "i" que estejam seguidos de "st". Monte esta expressão utilizando Regex

import re

CPF = '012.345.678-90'
# regex = '.,'

# 1 - Com Regex, conseguir mostrar o CPF 012.345.678-90 desta forma: 01234567890
cpf_numerico = re.sub(r'[^\w\s]', '', CPF)

# or
cpf_clean = ''.join(re.findall('\d', CPF))


print(f"{'*' * 40} Inicio {'*' * 40}")
print(f'CPF sem pontuação: {cpf_numerico}')
print(f'CPF sem clean: {cpf_clean}')
print('*'*80)
# 2 - Faça um validador de Passwords aonde o usuario digite o seu password e
# o seu programa deve validar se é um password válido ou não, para isso use as regras:
# a - Deve conter mais de 8 caracteres
# b - Deve conter ao menos uma Letra Maiúscula
# c - Deve conter ao menos 2 numeros
# d - Deve conter pelo menos 1 caractere especial
# e - deve conter pelo menos 2 letras minusculas

password = input("Digite uma senha: ")
# (?=.*?[A-Z])+ : pelo menos uma maiuscula(não usar {1,}, utilizar o + depois do parenteses)
# (?=.*?[0-9]{2,}): pelo menos dois numeros
# (?=.*[@#$&|~^%!*])+: pelo menos um caractere especial
# (?=.*?[a-z]{2,}): pelo menos duas letras minusculas
# [\w\d@#$&|~^%!*]{8,}: o conjunto de letras, números e caracteres especiais tem que ter pelo menos 8 caracteres
if not re.match(r"^(?=.*?[A-Z])+(?=.*?[0-9]{2,})(?=.*[\W])+(?=.*?[a-z]{2,})[\w\d\W]{8,}$", password):
    print("Senha inválida")

# 3 - Na frase 'avistamos estáticos o elastico e o plastico' quero retornar
# os caracteres "a" ou "e" ou "i" que estejam seguidos de "st". Monte esta expressão utilizando Regex

frase = 'avistamos estáticos o elastico e o plastico'
print('*'*80)
print(f'Frase: {frase}')
padrao = '[aei]st'
resultado = re.findall(padrao, frase)
# ou resultado = re.findall('(a|e|i)st', frase)
print(f'Lista de caracteres aei seguidos de st: {resultado}')

print(f"{'*' * 40} Fim {'*' * 40}")
