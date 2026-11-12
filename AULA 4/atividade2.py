lado1 = float(input('digite o tamanho do lado 1: '))
lado2 = float(input('digite o tamanho do lado 2: '))
lado3 = float(input('digite o tamanho do lado 3: '))
 
if lado1 == lado2 == lado3:
  print('triangulo equilatero')
elif lado1 == lado2 != lado3:
    print('triangulo isoceles')

elif lado1 != lado2 == lado3:
   print('triangulo isoceles ')
   
elif lado1 == lado3 != lado2:
     print('triangulo isoceles')
     
else:
  print('triangulo escaleno')

