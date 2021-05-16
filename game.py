import tkinter
from view import draw_canvas
from model import game_rules
from controller import event_handler

# Criação da janela principal
root = tkinter.Tk()

# Criação de um canvas na janela principal
cnv = tkinter.Canvas(root, bg="white", height=700, width=1200)
# cnv.bind('<ButtonRelease-1>', event_handler.click)
draw_canvas.escolheNivel(cnv)
draw_canvas.inicia("facil")
draw_canvas.desenha(cnv)

cnv.pack()
root.mainloop()