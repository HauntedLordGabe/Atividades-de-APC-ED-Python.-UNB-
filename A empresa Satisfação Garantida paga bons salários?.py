iterador = 0
conglomerado = 0

while True:
    a, b = input().split(',')
    b = float(b)

    if a == "Fim":
        break
    iterador += 1
    conglomerado += b

if iterador == 0:
    print('0.00')
else:
    b = conglomerado / iterador
    print(f'{b:.2f}')

