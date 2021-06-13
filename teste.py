#Thiago Levis Alambert Rodrigues
#Pedro Leon Fontes Cardoso
#Raphael Ponce

import tkinter
import sys
import os
from model import game_rules
from view import draw_canvas


def testeDificuldade():
    game_rules.setDificuldade("facil")
    print(game_rules.dificuldade)
    print(game_rules.n_de_cores)



def testeCriaSenha():
    game_rules.setDificuldade("facil")
    game_rules.criaSenha()
    print(game_rules.senha)


def testeTentativaJogador():
    game_rules.setDificuldade("facil")
    game_rules.tentativaJogador()
    print(game_rules.tentativaSenha)


def testeCompara():
    game_rules.setDificuldade("facil")
    game_rules.criaSenha()
    game_rules.tentativaJogador()
    game_rules.compara()
    print(game_rules.respostaSenha)


def desenhaTabuleiro():
    root = tkinter.Tk()
    cnv = tkinter.Canvas(root, bg="white", height=700, width=1200)
    draw_canvas.inicia("facil")
    draw_canvas.desenha(cnv)
    cnv.pack()
    root.mainloop() 


def desenhaEscolhaNivel():
    root = tkinter.Tk()
    cnv = tkinter.Canvas(root, bg="white", height=700, width=1200)
    draw_canvas.escolheNivel(cnv)
    cnv.pack()
    root.mainloop()

def guardaJogadas():
    arq = open("teste.txt","a")
    print(game_rules.tentativaSenha, game_rules.respostaSenha)
    tentativaGuarda = ""
    respostaGuarda = ""
    for i in range(0,len(game_rules.tentativaSenha)):
        tentativaGuarda += str(game_rules.tentativaSenha[i])+ ' '
        respostaGuarda += str(game_rules.respostaSenha[i]) + ' '
    arq.writelines("%s%s\n" %(tentativaGuarda,respostaGuarda))
    print(arq)
    arq.close()


def inicializaJogoGuardado():
  arq = open("teste.txt","r")
  game_rules.senha = arq.readline().strip().split(' ') #coloca a senha do arquivo txt na senha global
  game_rules.nivel = arq.readline().strip() #coloca o nivel
  game_rules.setDificuldade()
  print(arq)
  arq.close()


def restartGame():
  python = sys.executable
  os.execl(python, python, * sys.argv)
  print("jogo foi restartado")  


# Chamadas dos testes
# testeDificuldade()
# testeCriaSenha()
# testeTentativaJogador()
# testeCompara()
# desenhaTabuleiro()
# desenhaEscolhaNivel()
# guardaJogadas()
# inicializaJogoGuardado()
# restartGame()

