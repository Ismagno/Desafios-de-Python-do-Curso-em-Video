#desafio 46
from time import sleep

print('{:=^40}'.format(' CONTAGEM REGRESSIVA '))
i = int(input('Começo: '))
f = int(input('Final: '))
n = int(input('Pulando quantas casas? '))
for c in range(i, f-1, -n):
    print(c)
    sleep(1)
print('FIM')
print('='*40)