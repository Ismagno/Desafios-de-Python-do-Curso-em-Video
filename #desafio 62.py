#desafio 62
print('='*30)
print('{:^30}'.format('10 TERMOS DE UMA PA'))
print('='*30)

#variaveis
p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
n = ''
c = 0
c2 = 0

#Repetição
while c < 10:
    print(f'{p}', end= ' → ' if c < 9 else '\n')
    p += r
    c += 1

#mais termos
while n != 0 :
    n = int(input('Mais termos (para sair 0): '))
    c += c2
    c2 = 0
    while c2 < n:
        print(f'{p}', end = ' → ' if c2 < n-1 else '\n')
        p += r
        c2 += 1
print('Progressão finalizada com {} termos'.format(c))        
print('FIM')


    




