from view import draw_canvas
from model import game_rules

def nivel1(*args):
    draw_canvas.inicia("facil")

def nivel2(*args):
    draw_canvas.inicia("medio")

def nivel3(*args):
    draw_canvas.inicia("dificil")

def insereCor(event,cnv):
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
        game_rules.tentativaJogador("brown")
        draw_canvas.redesenhaCirculos(cnv)
    else:
        game_rules.tentativaJogador("purple")
        draw_canvas.redesenhaCirculos(cnv)

