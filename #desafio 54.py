#desafio 54
from datetime import date

ano = date.today().year
maior = 0
menor = 0
cont = 0

for c in range(0,7):
    nasc = int(input('Data de Nascimento: '))
    idade = ano - nasc
    cont += 1
    if idade < 21:
        menor += 1
    elif idade >= 21:
        maior += 1
print('No grupo de {} pessoas a {} maiores de idade e {} menores de idade'.format(cont,maior , menor))