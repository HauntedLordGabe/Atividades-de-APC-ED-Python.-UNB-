x1, y1, z1 = input().split()

x2, y2, z2 = input().split()


calculox = float(x1)*float(x2)
calculoy = float(y1)*float(y2)
calculoz = float(z1)*float(z2)
soma = calculox + calculoy + calculoz
soma2 = float(x2)+float(y2)+float(z2)
calculo1 = soma / soma2


print(f'{calculo1:.6f}')
