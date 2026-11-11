
saldo = 500.20
senha = 1234

print('banco Z...')
print('seja bem vindo')

senha = int(input('digite sua senha '))

op = input('''
   escolher operação:
   
   1 - saque
   2 - deposito
   3 - extrato
   
   ''')

resultado = op == '1' and +float(input('voce escolheu saque R$:')) - saldo or op == '2' and float(input('voce escolheu desposito')) + saldo or ('extrato ' , saldo)
print(resultado)
