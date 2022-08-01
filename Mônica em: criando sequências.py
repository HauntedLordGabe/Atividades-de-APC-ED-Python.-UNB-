a = int(input())
b = int(input())
c = int(input())
p1 = input()
p2 = input()

soma_ab = a + b 
soma_bc = b + c
soma_ac = a + c

soma1 = p1 * soma_ab
soma2 = p2 * soma_bc

concatenação = soma1 + soma2
multiplicação = concatenação * soma_ac


print(multiplicação)
