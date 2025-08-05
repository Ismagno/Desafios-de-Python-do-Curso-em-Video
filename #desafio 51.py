#desafio 51
print('='*30)
print('{:^30}'.format(' 10 TERMOS DE UMA PA '))
print('='*30)
pt = int(input('Primeiro termo: '))
r = int(input('Razão: '))
a = pt + (10 - 1) * r
for c in range(pt, a + 1, r):
    print('{} ->'.format(c), end=' ')
print('ACABOU')
