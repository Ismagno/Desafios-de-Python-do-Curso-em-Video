#desafio 68
from random import randint
from time import sleep

cont = 0
while True:
    print(f'{'IMPAR OU PAR':=^30}')
    n = int(input('Diga um valor: '))
    pc = randint(1, 10)
    while True:
        option = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
        if option in 'PI':
            break
    soma = n + pc
    print('='*30)
    print(f'Você jogou {n} e o computador {pc}.', end =' ')
    print("\nPensando...")
    sleep(2)
    if option == 'P':
        if soma % 2 == 0:
            print(f'Total de {soma} DEU PAR')
            print('='*30)
            print('Você VENCEU !!')
            print('Jogar novamente...')
            cont += 1
        else:
            print(f'Total de {soma} DEU IMPAR')
            print('='*30)
            print('Você PERDEU !!')
            break
    if option == 'I':
        if soma % 2 != 0:
            print(f'Total de {soma} DEU IMPAR')
            print('='*30)
            print('Você VENCEU !!')
            print('Jogar novamente...')
            cont += 1
        else:
            print(f'Total de {soma} DEU PAR')
            print('='*30)
            print('Você PERDEU !!')
            break
print('='*30)
if cont != 0:   
    print(f'Você ganhou {cont} antes de perder')
print(f'{' FIM DE JOGO ':=^30}')
    
