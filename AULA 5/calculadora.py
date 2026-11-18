def soma(n1):
  
    n2 =  int(input('nº: '))
    print('=', n1 + n2)
    
    
def subtracao(n1):

    n2 =  int(input('nº: '))
    print('=', n1 - n2)
    
    
def multiplicacao(n1):

    n2 =  int(input('nº: '))
    print('=', n1 * n2)
    
def divisao(n1):
   
    n2 =  int(input('nº: '))
    print('=', n1 / n2)
    
    
def calculadora():
    
    while True:
        n1 =  int(input('nº: '))
        op = input('qual operação voçe deseja >>').lower()
        if op == '+':
            soma(n1)
        elif op == '-':
            subtracao(n1)
        elif op == 'x':
            multiplicacao(n1)
        elif op == '/':
            divisao(n1)
        else:
            print('digite algo valido')
calculadora()