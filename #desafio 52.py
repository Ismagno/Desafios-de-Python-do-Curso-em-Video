#desafio 52
from math import floor
cont = 0
n = int(input('Digite um número inteiro: '))
for c in range(1, n + 1):
    if n % c == 0:
        cont += 1
if cont == 2:
    print('Esse número é PRIMO')
elif cont != 2:
    print('Esse número NÃO é primo')


