lista = ['janeiro','fevereiro','março','julho','agosto','setembro','outubro','novembro']

if 'julho' in lista:
    print('julho esta na lista')
else:
    print('julho não esta na lista')
lista.insert('abril', 3)
print(lista)

lista.insert('dezembro', 6)
print(lista)

lista.remove('novembro')
print(lista)             