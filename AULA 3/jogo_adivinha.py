
import random




print("jogo da advinhação - advinhe um numero")
print('***' * 9)
print()

numero_aleatorio = random.randint(1,10)

escolha_do_usuario = int(input('digite um numero entre 1 e 10: '))


resultado = numero_aleatorio == escolha_do_usuario and ('acertou') or ('error')


print('resultado: ' , resultado)
print('o numero era : ', numero_aleatorio)

                                                                       