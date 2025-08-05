#desafio 67

print(f'{' TABUADA ':=^25}')

while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c:>2} = {n*c}')
    print('='*25)
print(F'{'ENCERRADO':=^25}')