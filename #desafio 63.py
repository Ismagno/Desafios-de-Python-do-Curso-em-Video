#desafio 63

print('{:=^40}'.format(' SEQUÊNCIA DE FIBONACCI '))

n = int(input('Quantos termos da sequência de Fibonacci: '))
n1 = 0
n2 = 1
n3 = 0

if n == 1:
    print(f'{n1}')
elif n > 1:
    print(f'{n1} → {n2}',end = ' → ' if n > 2 else '\n')
    c = 2
    while c < n:
        n3 = n1 + n2
        print(f'{n3}', end = ' → ' if c < n-1 else '\n')
        n1 = n2
        n2 = n3
        c += 1
print('FIM')

