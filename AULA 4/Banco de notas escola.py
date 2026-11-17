alunos = []
medias = []

pergunta = input('deseja acessar?').lower()
while pergunta == 'sim':
    
  for i in range(4):
      senha = input('SENHA: ')
      if senha == '123':
        print('SISTEMA DE NOTAS..')
        nome = input('aluno ')
        nota1 = float(input('nota matematica: '))
        nota2 = float(input('nota portugues: '))
        nota3 = float(input('nota ingles: '))
        media = (nota1+nota2+nota3) / 3
        print('media', media,'aluno(a)', nome)
        alunos.append(nome)
        medias.append(media)
        pergunta = input('deseja continuar?')
        if pergunta !='sim':
            print('lista de alunos')
            print(alunos)
            print('medias')
            print(media)
            print('MEDIA DA SALA: ', sum(medias)/len(medias))
            print('***' * 10)
            pergunta = input('deseja continuar?')

      else:
          print('senha incorreta')
  else:
      print('senha bloqueada')
      break   
else:
            print('ate logo')
 
 