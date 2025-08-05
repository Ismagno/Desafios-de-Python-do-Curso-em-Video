#desafio 32
print('===== ANO BISSEXTO =====')
ano = int(input('Qual o ano? '))
digitos = ano//1 % 100 #seprar os últimos dois dígitos
b = digitos % 4 #conferir se os últimos dois dígitos são múltiplo de 4
if b == 0:
    print('O ano de {} é bissexto'.format(ano))
else:
    print('O ano de {} não é bissexto'.format(ano))
