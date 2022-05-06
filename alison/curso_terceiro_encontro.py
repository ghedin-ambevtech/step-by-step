import re
# String

frase = "hoje é dia 1 de Abril, o dia da mentira!     "

print(frase)
print(frase[:5])
print(frase[2:10])
print(frase[::-1])
print(frase[10:])

# operações com strings
print(frase.upper())
print(frase.strip())
print(frase.capitalize())
print(frase.title())
print(frase.split(','))

sep = frase.split(',')
print(sep)
print(','.join(sep))

resultado = re.findall('\w', frase)
print(resultado)

email = 'teste@gmail.com'
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

print(re.search(regex, email))

if re.search(regex, email):
    print('Email válido')
else:
    print('Email inválido')


print(len(re.findall('\d', frase)))
print(1 if email == 'test@gmail.com' else 'deu ruim')