#criar uma lista com os dias da semana
semanas = ['terça','quarta','quinta','sexta']
print(semanas)
#pedir para o usuario por um dia da semana na lista
dia = input('insira um dia da semana:')
# usar if e else para determinar se o dia esta ou não na lista
if dia in semanas:
    print('esse dia esta na lista')
else:
    print('esse dia não está na lista')
