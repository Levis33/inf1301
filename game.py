import tkinter
from view import draw_canvas
from model import game_rules
from controller import event_handler

# Criação da janela principal
top = tkinter.Tk()

# Criação de um canvas na janela principal
game_rules.novoJogo()
cnv = tkinter.Canvas(top, bg="white", height=1200, width=700)
cnv.bind('<ButtonRelease-1>', event_handler.click)
draw_canvas.inicia()
draw_canvas.desenha(cnv)

cnv.pack()
top.mainloop()