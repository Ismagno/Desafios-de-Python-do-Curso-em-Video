#desafio 83

expressao = (str(input('Digite uma expressão: ')))
pilha = list()

for carc in expressao:
    if carc in '(':
        pilha.append('(')
    elif carc in ')':
        if pilha:
            pilha.pop()
        else:
            print('Expressão invalida')
            break

else:
    if pilha:
        print('Sua expressão é INVÁLIDA !')
    else:
        print('Sua expressão é VÁLIDA')