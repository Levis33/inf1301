from view import draw_canvas
from model import game_rules

def nivel1(*args):
    draw_canvas.inicia("facil")

def nivel2(*args):
    draw_canvas.inicia("medio")

def nivel3(*args):
    draw_canvas.inicia("dificil")

def insereCor(event):
    if event.x < 50:
        game_rules.tentativaJogador("red")
    elif event.x < 100:
        game_rules.tentativaJogador("green")
    elif event.x < 150:
        game_rules.tentativaJogador("blue")
    elif event.x < 200:
        game_rules.tentativaJogador("yellow")
    elif event.x < 250:
        game_rules.tentativaJogador("pink")
    elif event.x < 300:
        game_rules.tentativaJogador("cyan")
    elif event.x < 350:
        game_rules.tentativaJogador("brown")
    else:
        game_rules.tentativaJogador("purple")

    print(game_rules.respostaSenha)

