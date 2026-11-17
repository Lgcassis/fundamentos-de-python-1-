import random
score_user = 0
score_maquina = 0
while True:

    lista_maquina = ['pedra ','papel ','tesoura ']
    escolha_maquina = random.choice(lista_maquina)
    escolha_user = input('escolha entre: pedra,papel ou tesoura: ')


    if escolha_maquina == escolha_user:
        print('empate')
        print('maquina jogou: ' , escolha_maquina)
        print('pontos maquina', score_maquina)
        print('usuario jogou: ', escolha_user)
        print('pontos usuario' , score_user)
        
        
    elif escolha_maquina == 'pedra' and escolha_user == 'tesoura':
        print('a maquina ganhou *.*')
        score_maquina = score_user + 1
        print('maquina jogou: ' , escolha_maquina)
        print('pontos maquina', score_maquina)
        print('usuario jogou: ', escolha_user)
        print('pontos usuario' , score_user)
        
    elif escolha_maquina == 'tesoura' and escolha_user == 'papel':
        print('a maquina ganhou *.*')
        score_maquina = score_user + 1
        print('maquina jogou: ' , escolha_maquina)
        print('pontos maquina', score_maquina)
        print('usuario jogou: ', escolha_user)
        print('pontos usuario' , score_user)
        
    elif escolha_maquina == 'papel' and  escolha_usuario == 'pedra':    
        print('A maquina ganhou *.*')
        score_maqui =  score_maqui + 1 
        print('maquina jogou: ', escolha_maquina)
        print('pontos da maquina: ', score_maquina)
        print('usuario jogou: ', escolha_usuario)
        print('pontos usuario ', score_user)
        
    else:
        print('a maquina ganhou *.*')
        score_user = score_user + 1
        print('maquina jogou: ' , escolha_maquina)
        print('pontos maquina', score_maquina)
        print('usuario jogou: ', escolha_user)
        print('pontos usuario' , score_user)
        

        
