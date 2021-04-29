__all__ = ['novoJogo']
import random

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
pink = (255,0,255)
cyan = (0,255,255)
brown = (153,76,0)
purple= (127,0,255)

limiteJogadas = 8 #
nPedras = 4 # numero de pedras de acordo com a 
cores = ['red','green','blue','yellow','pink','cyan','brown','purple']
senha = []
tentativaSenha = []
respostaSenha = []
diculdade = 0
n_de_cores = 0
tentativas = limiteJogadas


#Coloca as variaveis de acordo com a dificuldade 
def dificuldade(nivel):
  global senha,nPedras,dificuldade,n_de_cores,limiteJogadas,tentativas

  if nivel == 'facil':
    dificuldade = 1
    n_de_cores = 3

  elif nivel == 'medio':
    n_de_cores = 0 
    limiteJogadas += 2
    n_de_cores = 2
    nPedras += 1
    dificuldade = 2
    tentativas +=2

  else:
    limiteJogadas +=4
    n_de_cores = 1
    nPedras+=2
    tentativas +=4
    dificuldade = 3

#gera uma senha
def criaSenha():
  global cores,n_de_cores,senha,nPedras
  for i in range(0,nPedras):
    senha.append(cores[random.randrange(0,len(cores)-n_de_cores)])


def novoJogo():
    global limiteJogadas,nPedras,cores,senha,tentativas

    nivel = input('qual a dificuldade?')
    dificuldade(nivel)
    criaSenha()

    while tentativas != 0:
      if(dificuldade == 1):
          for i in range(0,nPedras):
              tentativaJogador()           

      elif(dificuldade == 2):
          for i in range(0,nPedras):
              tentativaJogador()

      else:
          for i in range(0,nPedras):
              tentativaJogador()
      
      ganhou = compara()
      if(ganhou):
        return
      print(respostaSenha)

      tentativas -= 1
      tentativaSenha.clear()
      respostaSenha.clear()
    print('perdeu')

#gera uma tentativa para o jogador
def tentativaJogador():
  global senha,tentativaSenha
  
  input_jogador = input('digite uma cor:')
  tentativaSenha.append(input_jogador)

#compara a tentativa do jogador com a senha
def compara():
  global tentativaSenha,senha,nPedras, respostaSenha,tentativas
  for i in range(nPedras):
    if tentativaSenha[i] == senha[i]:
      respostaSenha.append('black')

    elif tentativaSenha[i] in senha and tentativaSenha[i] != senha[i]:
      respostaSenha.append('white')

    else:
      respostaSenha.append('vazia')

  if tentativaSenha == senha:
    print('ganhou')
    return True


novoJogo()
