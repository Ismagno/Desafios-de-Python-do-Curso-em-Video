#desafio 55

pmax = 0
pmin = 0

for c in range(1, 6):
    p = float(input('PESO  DA PESSOA {}º: '.format(c)))
    if c == 1:
        pmax = p
        pmin = p
    else:
        if pmax < p:
            pmax = p
        elif pmin > p:
            pmin = p
print('O maior peso é {} kg e o menor peso é {} kg'.format(pmax, pmin))