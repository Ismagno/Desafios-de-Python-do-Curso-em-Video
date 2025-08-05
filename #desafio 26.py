#desafio 26
print('='*40)
frase = str(input('Digite uma frase: ')).strip().upper()
frasec = frase.count('A')
print(f'A letra A aparece {frasec} vezes')
#print(f'A primeira letra A aparece {frase.find('A')}')
print('A primeira vez que a letra A aparece é : {}'.format(frase.find('A')+1))
print('A última vez que a letra A aparece é: {}'.format(frase.rfind('A')+1))
