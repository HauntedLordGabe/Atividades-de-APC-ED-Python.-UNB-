def troco(x):
    cinquenta = x // 50
    resto = x % 50
    vinte_e_cinco = resto // 25
    resto = resto % 25
    dez = resto // 10
    resto = resto % 10
    cinco = resto // 5
    um = resto % 5 
    print(f'{cinquenta} moedas de 50 centavos')
    print(f'{vinte_e_cinco} moedas de 25 centavos')
    print(f'{dez} moedas de 10 centavos')
    print(f'{cinco} moedas de 5 centavos')
    print(f'{um} moedas de 1 centavo')
