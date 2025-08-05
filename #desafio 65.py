#desafio 65

option = ''
n = 0
soma_n = 0
quantidade_n = 0
nmax = nmin = 0

while option != 'N':
    n = int(input('Digite um número: '))
    option = str(input('Adicionar mais números [S/N]: ')).strip().upper()[0]
    quantidade_n +=1
    soma_n += n
    if quantidade_n == 1:
        nmax = n
        nmin = n
    elif nmax < n:
        nmax = n
    elif nmin > n:
        nmin = n

media = soma_n/quantidade_n
print('A média dos {} números é {} !'.format(quantidade_n,media))
print('O maior é {} !'.format(nmax))
print('O menor é {} !'.format(nmin))