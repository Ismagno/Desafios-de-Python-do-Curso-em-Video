#leitor de ângulo
import math


while True:
    print('='*20)
    print('Leitor de ângulo: ')
    a = float(input('Fonerça um ângulo(°): '))
    sen = math.sin(math.radians(a))
    cos = math.cos(math.radians(a))
    tan = math.tan(math.radians(a))
    print(f'De acordo com o ângulo {a:.2f}°:\nSeno: {sen:.2f}\nCosseno: {cos:.2f}\nTangente: {tan:.2f}')
    print('='*20)
    char = input('Para finalizar o progama aperte Q!')
    if char=="q" or char=="Q":
        break