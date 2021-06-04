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

#global columnR,rowR
#columnR = 0
#rowR = 0
#SIZE = 50

#Bind de nivel
cnv.tag_bind("nivel1","<Button-1>",event_handler.nivel1)
cnv.tag_bind("nivel2","<Button-1>",event_handler.nivel2)
cnv.tag_bind("nivel3","<Button-1>",event_handler.nivel3)

#bind de circulos de cores
cnv.tag_bind("cores","<Button-1>",event_handler.insereCor)

'''
def redesenhaCirculos(cnv):
    global sizeR,yR,columnR,rowR

    listaCoresDisponiveis = game_rules.cores[0:game_rules.n_de_cores]
    nPedras = game_rules.nPedras
    limiteJogadas = game_rules.limiteJogadas
    print(nPedras,limiteJogadas,columnR,rowR,"nPedras,limiteJogadas,columnR,rowR")

    if columnR <  limiteJogadas:
            if rowR < nPedras:
                x1 = rowR * SIZE
                y1 = columnR * SIZE
                x2 = x1 + SIZE
                y2 = y1 + SIZE
                cnv.create_oval(x1,y1,x2,y2, fill=game_rules.tentativaSenha[rowR])
                rowR+=1
                if rowR == nPedras-1:
                    rowR = 0
                    columnR +=1
                #print(column,row)

'''
btn = Button(root,text="iniciar",width=12,bg="red",height=2,font ="arial 20",command=lambda: [draw_canvas.desenha(cnv),btn.destroy()])
#btn2 = Button(root,text="iniciar",width=12,bg="red",height=2,font ="arial 20",command=lambda: redesenhaCirculos(cnv))

#btn2.place(x=200,y=200)
btn.place(x=50,y=100)

cnv.pack()
root.mainloop()