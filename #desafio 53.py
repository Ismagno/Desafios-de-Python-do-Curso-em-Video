#desafio 53

p = str(input('Digite uma frase: ')).strip()
pfor = p.upper().split()
pf = (''.join(pfor))
i = pf[::-1]
if pf == i:
    print('A frase " {} " é um POLÍNDROMO'.format(p,))
else: 
    print('A frase NÃO é um polídromo')