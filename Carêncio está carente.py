import math

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

D = math.sqrt((x2-x1)**2 + (y2-y1)**2)

if D <= 100:
    print('É o amor da minha vida!')
elif D >= 201:
    print('Não vale a pena investir')
else:
    print('Talvez dê certo')
