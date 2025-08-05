#desafio 41
from datetime import date

print('===== CATEGORIA NA NATAÇÃO =====')
ano = int(input('Qual seu ano de nascimento? '))
idade = ((date.today().year) - ano)
if idade < 9:
    print('Sua categoria é a MIRIM')
elif idade < 14:
    print('Sua categoria é a INFANTIL')
elif idade < 19:
    print('Sua categoria é JÚNIOR')
elif idade < 20:
    print('Sua categoria é a SÊNIOR')
else:
    print('Sua categoria é a MASTER')
print('='*32)