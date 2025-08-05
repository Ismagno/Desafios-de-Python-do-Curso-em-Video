print('{:=^20}'.format(' TABUADA V2.0 '))
n = int(input('Escolha um número: '))
for c in range(1, 11):
    print(f'{n} x {c:>2} = {n*c:>2}')
print('{:=^20}'.format('FIM'))