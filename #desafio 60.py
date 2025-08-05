#desafio 60

n = int(input('Digite um número: '))
c = 1 
r = 0
p = 0

'''# for
for c in range(1, n): 
    n *= c
print(n)'''

#while
if n == 1: 
    print('Fatorial de 1 é ele mesmo')
else:
    while c < n:
        if c == 1:
            r = n * c
            p = r
            c += 1
        else:
            p *= c
            c += 1
    print('Fatorial do número {} é {}'.format(n,p))