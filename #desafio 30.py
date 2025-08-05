#desafio 30

print('='*30)
n = int(input('Digite um número: '))
resto = n%2
if resto == 0:
    print('O número {} é par'.format(n))
else:
    print('O número {} é impar'.format(n))
