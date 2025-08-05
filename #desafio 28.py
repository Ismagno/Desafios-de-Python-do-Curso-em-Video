#desafio 28
from random import randint
print('===== Jogo da Adivinhação ===== ')
while True:
    n = int(input('Digite um número de 1 a 5: '))
    pc = randint(1,5)
    if pc == n:
        print('Você acertou! O número era {}'.format(pc))
    else:
        print('Você errou! O número era {}'.format(pc))
    sair = str(input('Para sair aperte Q, jogar novamente ENTER:')).strip().upper()
    print('='*32)
    if sair == 'Q':
        break
    
