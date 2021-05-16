import tkinter
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


# Chamadas dos testes
# testeDificuldade()
# testeCriaSenha()
# testeTentativaJogador()
# testeCompara()
# desenhaTabuleiro()
# desenhaEscolhaNivel()

