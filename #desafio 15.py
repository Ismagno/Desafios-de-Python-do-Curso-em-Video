#aluguel de carro
print('-'*20)
print('ALUGUEL DO CARRO: ')
dia = int(input('Quantos dias? '))
km = float(input('Quantos Kms? '))
#km = 0.15 dia = 60
valor = (km * 0.15) + (dia * 60)
print(f'O valor do aluguel é {valor:.2f}')
print('-'*20)
input('Aperte ENTER para sair do programa!')