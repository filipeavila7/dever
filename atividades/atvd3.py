# pedir ao usuário que ele insira 5 notas
listnota = []
nt1 = int(input('insira a nota de mat:'))
listnota.append(nt1) 
nt2 = int(input('insira a nota de port:'))
listnota.append(nt2) 
nt3 = int(input('insira a nota de bio:'))
listnota.append(nt3) 
nt4 = int(input('insira a nota de fisi:'))
listnota.append(nt4) 
nt5 = int(input('insira a nota de hist:'))
listnota.append(nt5) 
# definir o total e a soma e calculo da media
total = len(listnota)
soma = sum(listnota)
media = soma / total
print(20*'=','BOLETIM ESCOLAR',20*'=')
# usar if else e elif para determinar a sua situação de acordo com as medias
print(f'a media é: {media}')
print()
if media >= 7:
    print(f'**aprovado com media:{media}**')
elif media >=5:
    print(f'**recuperação com media:{media}**')
else:
    print(f'**reprovado com media:{media}**')