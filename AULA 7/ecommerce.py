
def cumprimentar():
    print('SEJA BEM VINDO(A)')

def e_commerce():
    cumprimentar()
    pergunta = input('Deseja acessar? s/n').lower()
    carrinho = []
    total   =  []
    while pergunta == 's':
        produtos = {
             'iphone 18':10000.20,
             'tv':2500.50,
             'ssd 512':350.60,
             'notebook dell':5000.50            
            }

        print('Produtos:', produtos)
        produto = input('Escolha o produto: ').lower()
        carrinho.append(produto)
        total.append(produtos[produto])
        print('Suas compras: ', carrinho)
        print('R$', sum(total))
        pergunta = input('Deseja continuar? s/n').lower()
    else:
       print('CARRINHO:', carrinho)
       total_ = sum(total)
       print('R$', total_)
       pag = ['', '1 Pix','2 CC', '3 CD','4 Paypal']
       forma = int(input(f'Escolha {pag}'))
       print('Forma de pagamento',pag[forma] )
       print('OBRIGADA VOLTE SEMPRE!')

e_commerce()       

        
    

