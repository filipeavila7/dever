# a)
# primeiro adicionamos a lista
lista = [5,8,2,9,1]
print(lista)

# b)
# usamos o '.sort' para acrescentar a lista em ordem crescente
lista.sort()
print(lista)
# para ser decrescente, adicionamos o 'reverse=True'
lista.sort(reverse=True)
print(lista)

# c)
# criamos uma variavel para o valor '7', e usamos o '.append' para adicionar o numero
num = 7
lista.append(num)
print(lista)
# usamos o '.insert' para inserir o numero 3 na segunda posição da lista(indice 1)
lista.insert(1, 3)
print(lista)

# d)
# usamos o '.insert' para substituir o primeiro valor(indice 0) da lista por 10
lista.insert(0, 10)
print(lista)
# usamos o '.remove' para remover um valor desejado, no caso o numero 9 da lista
lista.remove(9)
print(lista)

# e)
# usamos o 'del' para deletar uma determinada posição de numeros na lista, no caso do 2 ate 4
del lista[2:4]
print(lista)



