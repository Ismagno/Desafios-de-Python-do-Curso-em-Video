#desafio 59
print('='*30)
n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))

option = 0
while option != 5:
    print('='*30)
    print('[ 1 ] SOMAR\n[ 2 ] MULTIPLICAR\n[ 3 ] MAIOR VALOR\n[ 4 ] NOVOS NÚMEROS\n[ 5 ] SAIR DO PROGRAMA')
    option = int(input('Qual opção: '))
    if option == 1:
        print('{} + {} = {}'.format(n1, n2, (n1 + n2)))
    elif option == 2:
        print('{} x {} = {}'.format(n1, n2, (n1 * n2)))
    elif option == 3:
        if n1 > n2:
            print('O maior valor é {}'.fomart(n1))
        elif n2 > n1:
            print('O maior valor é {}'.format(n2))
    elif option == 4:
        print('='*30)
        n1 = float(input('Primeiro valor: '))
        n2 = float(input('Segundo valor: '))
    elif option != 5:
        print('Opção invalida, tente novamente..')
print('{:=^30}'.format(' FINALIZADO '))
    
    