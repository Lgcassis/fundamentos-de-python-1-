def cadastro():
 nome = ['luis','lucas','maria']
 email = ['luis@', 'lucas@','maria@']
 while True:
     a = (input('digite seu nome: '))
     b = (input('digite seu email: '))
     c = (input('digite sua idade: '))
     
     if a in nome  and b in email:
       print('esse usuario ja existe tente outro')
     else:
        nome.append(a)
        email.append(b)
        print('cadastro feito com sucesso')
        break  
cadastro()

