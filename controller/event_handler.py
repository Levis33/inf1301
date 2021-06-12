#Thiago Levis Alambert Rodrigues
#Pedro Leon Fontes Cardoso
#

from view import draw_canvas
from model import game_rules
#nas funcoes nivel1-3 e apenas setados as variaveis de acordo com o nivel clicado
def nivel1(*args):
    game_rules.nivel = "facil"
    draw_canvas.inicia()
    #caso voce queira saber a senha apenas tirar o comentario abaixo
    print(game_rules.senha)
def nivel2(*args):
    game_rules.nivel = "medio"
    draw_canvas.inicia()
    #caso voce queira saber a senha apenas tirar o comentario abaixo
    #print(game_rules.senha)    

def nivel3(*args):
    game_rules.nivel = "dificil"
    draw_canvas.inicia()
    #caso voce queira saber a senha apenas tirar o comentario abaixo
    #print(game_rules.senha)

def insereCor(event,cnv):
    #essa parte abaixo pega a posicao do mouse do click e verifica a posicao, vendo assim qual cor colocar dentro da tentativa do jogador
    if event.x < 50:
        game_rules.tentativaJogador("red")
        draw_canvas.redesenhaCirculos(cnv)
    elif event.x < 100:
        game_rules.tentativaJogador("green")
        draw_canvas.redesenhaCirculos(cnv)
    elif event.x < 150:
        game_rules.tentativaJogador("blue")
        draw_canvas.redesenhaCirculos(cnv)
    elif event.x < 200:
        game_rules.tentativaJogador("yellow")
        draw_canvas.redesenhaCirculos(cnv)
    elif event.x < 250:
        game_rules.tentativaJogador("pink")
        draw_canvas.redesenhaCirculos(cnv)
    elif event.x < 300:
        game_rules.tentativaJogador("cyan")
        draw_canvas.redesenhaCirculos(cnv)
    elif event.x < 350:
        game_rules.tentativaJogador("brown4")
        draw_canvas.redesenhaCirculos(cnv)
    else:
        game_rules.tentativaJogador("purple")
        draw_canvas.redesenhaCirculos(cnv)
    #Desenha o canvas cajo ocorra uma vitoria/derrota
    if(game_rules.vitoria):
        draw_canvas.desenhaVitoriaouDerrota(cnv,True)
    elif(game_rules.derrota):
        draw_canvas.desenhaVitoriaouDerrota(cnv,False)

def restartGame(*args):
    game_rules.restartGame()
