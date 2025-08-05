#desafio 64
n = ''
c = 1
soma = 0

while n != 999:
    n = int(input('Digite {}º número: '.format(c)))
    if n != 999:
        soma += n
        c += 1
print('Foram digitados {} números\nA soma entre eles é {}'.format(c-1,soma))
