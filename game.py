#Thiago Levis Alambert Rodrigues
#Pedro Leon Fontes Cardoso
#

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


#Bind de nivel, "nivelX" esta referente ao que foi passado em "tags" na game_rules.py,
cnv.tag_bind("nivel1","<Button-1>",event_handler.nivel1)
cnv.tag_bind("nivel2","<Button-1>",event_handler.nivel2)
cnv.tag_bind("nivel3","<Button-1>",event_handler.nivel3)

#bind de circulos de cores
cnv.tag_bind("cores","<Button-1>", lambda event: event_handler.insereCor(event,cnv))
#foi utilizado o lambda para não ser desenhado até o botao seja clicado
btn = Button(root,text="iniciar",width=12,bg="red",height=2,font ="arial 20",command=lambda: [draw_canvas.desenha(cnv),btn.destroy()])

cnv.tag_bind("restartButton","<Button-1>", event_handler.restartGame)

btn.place(x=50,y=100)


cnv.pack()
root.mainloop()