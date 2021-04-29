__all__ = ['novoJogo', 'dificuldade', 'criaSenha', 'compara', 'tentativaJogador']
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

limiteJogadas = 0 #
nPedras = 0 # numero de pedras de acordo com a 
cores = ['red','green','blue','yellow','pink','cyan','brown','purple']
senha = []
tentativaSenha = []
respostaSenha = []
diculdade = 0
n_de_cores = 0
tentativas = limiteJogadas


#Coloca as variaveis de acordo com a dificuldade 
def setDificuldade(nivel):
  global senha,nPedras,dificuldade,n_de_cores,limiteJogadas,tentativas

  if nivel == 'facil':
    dificuldade = 1
    n_de_cores = 6
    nPedras = 4
    limiteJogadas = 8

  elif nivel == 'medio':
    n_de_cores = 0 
    limiteJogadas = 10
    n_de_cores = 7
    nPedras = 5
    dificuldade = 2

  else:
    limiteJogadas = 12
    n_de_cores = 8
    nPedras = 6
    dificuldade = 3

#gera uma senha
def criaSenha():
  global cores,n_de_cores,senha,nPedras
  for i in range(0,nPedras):
    senha.append(cores[random.randrange(0,n_de_cores)])

#gera uma tentativa para o jogador
def tentativaJogador():
  global tentativaSenha
  
  for i in range(0,nPedras):
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

