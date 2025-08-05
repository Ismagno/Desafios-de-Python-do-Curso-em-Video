#desafio 88

from random import sample
from time import sleep

jogos = []

bilhete = int(input('Quantos jogos vc quer fazer ? '))
for v in range(0, bilhete):
    jogos.append(sorted(sample(range(1,61), k = 6)))

print(f'====== Sorteado {bilhete} jogos ======')
sleep(1)

for i, v in enumerate(jogos):
    print(f'Jogo {i+1}: ', v)
    sleep(1)
print('='*30)



