def func1():
     resp = input('O programa funciona?\n')
     if(resp == 'SIM'):
         func2()
     else:
         func3()

def func2():
    resp = input('Você entende o que fez?\n')
    if(resp == 'SIM'):
        print('Ótimo. Então não mexe!')
    else:
        func6()

def func3():
    resp = input('Você sabe onde está o erro?\n')
    if(resp == 'SIM'):
        func4()
    else:
        func6()
    
    
def func4():
    resp = input('Acha que pode solucionar sozinho?\n')
    if(resp == 'SIM'):
        print('Então mão na massa!')
    else:
        func5()


def func5():
    resp = input('Já pesquisou no Google?\n')
    if(resp == 'SIM'):
        func6()
    else:
        print('Corre lá então!')
    
def func6():
    resp = input('Já foi na tutoria?\n')
    if(resp == 'SIM'):
        print('Choremos!')
    else:
        print('Temos um time a disposição!')
        
func1()
