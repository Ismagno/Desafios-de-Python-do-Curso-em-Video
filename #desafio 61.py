#desafio 61

print('='*30)
print('{:^30}'.format('10 TERMOS DE UMA PA'))
print('='*30)
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Razão: '))
seguinte = 0
c = 0
while c < 10:
    print('{}'.format(primeiro), end=' → ' if c < 9 else '\n')
    primeiro += razao
    c += 1
print('Acabou')
