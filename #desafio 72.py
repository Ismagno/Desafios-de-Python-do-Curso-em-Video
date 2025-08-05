#desafio 72

n_ex = ('zero', 'um', 'dois' ,'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezzeseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    while True:
        n = int(input('Digite um número de 0 a 20: '))
        if 0 <= n <= 20:
            break
        print('Tente novamente. ', end = '')
    print(f'Voce digitou o número {n_ex[n]}')
    while True:
        sair = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if sair in 'SN':
            break
    if sair == 'S':
        break
