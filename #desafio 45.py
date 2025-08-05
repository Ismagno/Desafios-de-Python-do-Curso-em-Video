#desafio 45
from random import choice
from time import sleep

print('===== JOKENPÔ =====')
while True:
    escolha = int(input('Escolha:\n1 - PEDRA\n2 - PAPEL\n3 - TESOURA\n'))
    lista = ['PEDRA', 'PAPEL', 'TESOURA']
    jokenpo = choice(lista)
    print('='*19)
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ!!!')
    sleep(1)
    if escolha == 1: #PEDRA
        if jokenpo == 'PEDRA':
            print('DEU EMPANTE\nJOGADOR: PEDRA\nPC: PEDRA')
        elif jokenpo == 'PAPEL':
            print('PC GANHADOR\nJOGADOR: PEDRA\nPC: PAPEL')
        elif jokenpo == 'TESOURA':
            print('JOGADOR GANHOU\nJOGADOR: PEDRA\nPC: TESOURA')
    elif escolha == 2: #PAPEL
        if jokenpo == 'PEDRA':
            print('JOGADOR GANHOU\nJOGADOR: PAPEL\nPC: PEDRA')
        elif jokenpo == 'PAPEL':
            print('DEU EMPANTE\nJOGADOR: PAPEL\nPC: PAPEL')
        elif jokenpo == 'TESOURA':
            print('PC GANHOU\nJOGADOR: PAPEL\nPC: TESOURA')
    elif escolha == 3: #TESOURA
        if jokenpo == 'PEDRA':
            print('PC GANHOU\nJOGADOR: TESOURA\nPC: PEDRA')
        elif jokenpo == 'PAPEL':
            print('JOGADOR GANHOU\nJOGADOR: TESOURA\nPC: PAPEL')
        elif jokenpo == 'TESOURA':
            print('DEU EMPATE\nJOGADOR: TESOURA\nPC: TESOURA')
    print('='*19)
    print('PC:FOI UM PRAZER JOGAR COM VC...')
    print('='*19)
    sair = str(input('Para jogar novamente aperte ENTER, caso contrario Q:').strip().upper())
    if sair == 'Q':
        break