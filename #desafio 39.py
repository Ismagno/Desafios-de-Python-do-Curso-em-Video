#desafio 39
from datetime import date

print('===== Alistamento Militar =====')
nome = str(input('Qual seu nome? ')).strip().title()
sexo = str(input('Qual seu sexo? ')).strip().upper()
if sexo == 'MASCULINO':
    ano = int(input('Qual o seu ano de nascimento? '))
    idade = ((date.today().year) - ano)
    if idade == 18:
        print('{}, você está na idade, {} anos, de fazer o alistamento militar obrigatório!'.format(nome.split()[0],idade))
    elif idade >= 18:
        p = idade - 18
        print('{}, você passou da idade de alistamento, por {} anos, apresente URGENTEMENTE!'.format(nome.split()[0],p))
        print('Seu alistamento era para ser em {}'.format((date.today().year) - p ))
    else:
        p = 18 - idade
        print('{}, você não tem idade para o alistamento militar! Faltam {} anos!'.format(nome.split()[0],p))
        print('Seu alistamento será no ano de {}'.format((date.today().year) + p ))
else:
    print('Você não precisa fazer o alistamento militar OBRIGATORIO!')
print('Tenha um Bom dia')
print('='*50)

