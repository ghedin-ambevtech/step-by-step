
def cumsum(*args):
    t = []
    soma = 0
    for item in args:
        soma += item
        t.append(soma)
    return t

print(cumsum(1, 5, 6, 15, 23, 2))
