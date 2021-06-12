#Thiago Levis Alambert Rodrigues
#Pedro Leon Fontes Cardoso
#

__all__ = ['setDificuldade', 'criaSenha', 'compara', 'tentativaJogador']
import random
import sys
import os

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
cores = ['red','green','blue','yellow','pink','cyan','brown4','purple']
senha = []
tentativaSenha = []
respostaSenha = []
diculdade = 0
n_de_cores = 0
tentativas = limiteJogadas
qtdTentativas = 0
vitoria = False
derrota = False
nivel = "facil"

#Coloca as variaveis de acordo com a dificuldade 
def setDificuldade():
  global senha,nPedras,dificuldade,n_de_cores,limiteJogadas,tentativas,nivel

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
  senha = []
  for i in range(0,nPedras):
    senha.append(cores[random.randrange(0,n_de_cores)])

#gera uma tentativa para o jogador
def tentativaJogador(cor):
  global tentativaSenha,respostaSenha,qtdTentativas
  respostaSenha = []
  tentativaSenha.append(cor)
  if (len(tentativaSenha)==nPedras):
        qtdTentativas +=1
        compara()
        

#compara a tentativa do jogador com a senha
def compara():
  global tentativaSenha,senha,nPedras, respostaSenha,tentativas,vitoria,derrota
  print(qtdTentativas,limiteJogadas)
  for i in range(nPedras):
    if tentativaSenha[i] == senha[i]:
      respostaSenha.append('black')

    elif tentativaSenha[i] in senha and tentativaSenha[i] != senha[i]:
      respostaSenha.append('white')

    else:
      respostaSenha.append('grey')

  if tentativaSenha == senha:
    vitoria = True
  elif qtdTentativas >= limiteJogadas:
    derrota = True

def restartGame():
  python = sys.executable
  os.execl(python, python, * sys.argv)

def guardaInfosRegras():
  global senha,nivel
  arq = open("rejogar.txt","w")
  senhaGuarda = ""
  for el in senha:
        senhaGuarda += str(el)+ ' '
  arq.write("%s\n%s\n" %(senhaGuarda,nivel))
  arq.close()

def guardaJogadas():
  global tentativaSenha,respostaSenha
  arq = open("rejogar.txt","a")
  print(tentativaSenha,respostaSenha)
  tentativaGuarda = ""
  respostaGuarda = ""
  for i in range(0,len(tentativaSenha)):
    tentativaGuarda += str(tentativaSenha[i])+ ' '
    respostaGuarda += str(respostaSenha[i]) + ' '
  arq.writelines("%s%s\n" %(tentativaGuarda,respostaGuarda))
  arq.close()

def inicializaJogoGuardado():
  global senha,nivel
  arq = open("rejogar.txt","r")
  senha = arq.readline().strip().split(' ') #coloca a senha do arquivo txt na senha global
  nivel = arq.readline().strip() #coloca o nivel
  setDificuldade()
  arq.close()

