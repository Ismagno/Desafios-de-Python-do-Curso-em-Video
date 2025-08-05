#desafio 56
smidade = 0
idmaxm = 0
menorF = 0
nomeM = 'Nenhuma homem'

for c in range(1, 5):
    print('----- {}º pessoa ----- '.format(c))
    nome = str(input('Qual seu nome? ')).strip().title()
    idade = int(input('Qual sua idade? '))
    sexo = str(input('Qual seu sexo(M/F)? ')).strip().upper()
    smidade += idade
    if sexo == 'M':
        if idmaxm < idade:
            idmaxm = idade
            nomeM = nome
    elif sexo == 'F' and idade < 20:
       menorF += 1
print('A media de idade é igual a {}'.format(smidade/4))
print('O homem mais velho tem {} anos e se chama {}'.format(idmaxm,nomeM))
print('Ao todo são {} mulheres com menos de 20 anos'.format(menorF))