#desafio 70
p1000 = barato = produtoB = total = compras = 0

print('='*35)
print(f'{' LOJA ':^35}')
print('='*35)

while True:
    produto = str(input('Nome do produto: ')).strip().capitalize()
    preco = float(input('Preço: R$ '))
    compras += 1
    total += preco
    if compras == 1 or barato > preco:
        barato = preco
        produtoB = produto
    elif preco > 1000:
        p1000 += 1
    while True:
        prox = str(input('Quer continuar ? [S/N] ')).strip().upper()[0]
        if prox in 'SN':
            break
    if prox == 'N':
        break
print(f'{' FIM DO PROGAMA ':=^35}')
print(f'Foram comprados {compras} produtos resultando em {total:.2f}')
print(f'Tem {p1000} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi a {produtoB} custando {barato}')