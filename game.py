import tkinter
from tkinter import *
from view import draw_canvas
from model import game_rules
from controller import event_handler

# Criação da janela principal
root = tkinter.Tk()

# Criação de um canvas na janela principal
cnv = tkinter.Canvas(root, bg="white", height=700, width=1200)
draw_canvas.escolheNivel(cnv)
#draw_canvas.inicia("facil")


#Bind de nivel
cnv.tag_bind("nivel1","<Button-1>",event_handler.nivel1)
cnv.tag_bind("nivel2","<Button-1>",event_handler.nivel2)
cnv.tag_bind("nivel3","<Button-1>",event_handler.nivel3)

#bind de circulos de cores
cnv.tag_bind("red","<Button-1>",lambda: event_handler.insereCor("red"))
cnv.tag_bind("green","<Button-1>",lambda: event_handler.insereCor("green"))
cnv.tag_bind("blue","<Button-1>",lambda: event_handler.insereCor("blue"))
cnv.tag_bind("yellow","<Button-1>",lambda: event_handler.insereCor("yellow"))
cnv.tag_bind("pink","<Button-1>",lambda: event_handler.insereCor("pink"))
cnv.tag_bind("cyan","<Button-1>",lambda: event_handler.insereCor("cyan"))
cnv.tag_bind("brown","<Button-1>",lambda: event_handler.insereCor("brown"))
cnv.tag_bind("purple","<Button-1>",lambda: event_handler.insereCor("purple"))


btn = Button(root,text="iniciar",width=12,bg="red",height=2,font ="arial 20",command=lambda: [draw_canvas.desenha(cnv),btn.destroy()])

btn.place(x=50,y=100)

cnv.pack()
root.mainloop()