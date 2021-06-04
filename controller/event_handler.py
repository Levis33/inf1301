from view import draw_canvas

def nivel1(*args):
    draw_canvas.inicia("facil")

def nivel2(*args):
    draw_canvas.inicia("medio")

def nivel3(*args):
    draw_canvas.inicia("dificil")

def insereCor(event):
    if event.x < 50:
        print("red")
    elif event.x < 100:
        print("green")
    elif event.x < 150:
        print("blue")
    elif event.x < 200:
        print("yellow")
    elif event.x < 250:
        print("pink")
    elif event.x < 300:
        print("cyan")
    elif event.x < 350:
        print("brown")
    else:
        print("purple")

