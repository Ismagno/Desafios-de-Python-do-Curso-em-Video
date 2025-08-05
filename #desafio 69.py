#desafio 69 

sexoM = sexoF = maiorI = pessoas =0

while True:
    print('='*35)
    print(f'{'CADASTRO DE PESSOA':^35}')
    print('='*35)
    idade = int(input('IDADE: '))
    if idade > 18:
        maiorI += 1
    while True:
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if sexo == 'M':
            sexoM += 1
            break
        elif sexo == 'F' and idade < 20:
            sexoF += 1
            break
        elif sexo == 'F': 
            break
    pessoas += 1
    print('-'*35)
    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if continuar in 'SN':
            break
    if continuar in 'N':
        break
print(f'{' FIM DE PROGAMA ':=^35}')
print(f'Foram cadastradas {pessoas} pessoas')
print(f'Total de pessoas com mais de 18 anos: {maiorI}')
print(f'Ao todo tem {sexoM} homens cadastrados')
print(f'E tem {sexoF} mulheres com menos de 20 anos')