
#desafio 58
from random import randint

jogador = 0
pc = randint(1,10)
cont = 0

while jogador != pc:
    jogador = int(input('Adivinhe o número de 1 a 10: '))
    if jogador > pc:
        print('Menos... Tente mais uma vez.')
    elif jogador < pc:
        print('Mais...  Tente mais uma vez.')
    cont += 1
print('{:-^20}'.format(' WIN '))
if cont == 1:
    print('Parabéns você ganhou de PRIMEIRA!!!')
else:
    print('Parabéns, você ganhou na {}ª tentativa'.format(cont))
print('O número era {}'.format(pc))