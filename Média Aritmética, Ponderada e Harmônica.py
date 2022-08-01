def ponderada():
    calculox = float(x1)*float(x2)
    calculoy = float(y1)*float(y2)
    calculoz = float(z1)*float(z2)
    soma = calculox + calculoy + calculoz
    soma2 = float(x2)+float(y2)+float(z2)
    calculo1 = soma / soma2
    print('Ponderada')
    print(f'{calculo1:.2f}')

def harmonica():
    calculo1 = (1/int(x1)) + (1/int(y1)) + (1/int(z1))
    calculo2 = 3 / calculo1
    print('Harmonica')
    print(f'{calculo2:.2f}')

def aritmetica():
    calculo1 = (int(x1) + int(y1) + int(z1))/ 3
    print('Aritmetica')
    print((f'{calculo1:.2f}'))

x1, y1, z1 = input().split()
input1 = input()
if input1 == 'P':
    x2, y2, z2 = input().split()
    ponderada()
elif input1 == 'H':
    harmonica()
elif input1 == 'A':
    aritmetica()
else:
    print('Operacao inexistente')

