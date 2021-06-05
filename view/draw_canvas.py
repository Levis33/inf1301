from model import game_rules

SIZE = 50
Y = 20

global columnR,rowR
columnR = 0
rowR = 0

xCentro = 600
yCentro = 350

def inicia(nivel):
    game_rules.setDificuldade(nivel)
    game_rules.criaSenha()
 
    
def desenha(cnv):
    cnv.delete("all")
    listaCoresDisponiveis = game_rules.cores[0:game_rules.n_de_cores]
    nPedras = game_rules.nPedras
    limiteJogadas = game_rules.limiteJogadas
    
    for j in range(len(listaCoresDisponiveis)):
       cnv.create_oval(j * SIZE, (Y + 1) * SIZE - 400, (j + 1) * SIZE, (Y + 2) * SIZE - 400, fill = listaCoresDisponiveis[j], width = 5,tags='cores')

    for column in range(nPedras):
            for row in range(limiteJogadas):
                x1 = column * SIZE
                y1 = row * SIZE
                x2 = x1 + SIZE
                y2 = y1 + SIZE
                cnv.create_oval(x1,y1,x2,y2, fill="gray")



def escolheNivel(cnv):
    cnv.delete("all")
    global xCentro, yCentro
    cnv.create_text((xCentro,50), fill="darkblue" ,text="escolha um nivel e clique em 'iniciar'", font = "arial 20")
    nivel1 = cnv.create_rectangle(xCentro - 100,100,xCentro + 100,200,fill = "red",tags="nivel1")
    nivel2 = cnv.create_rectangle(xCentro - 100,300,xCentro + 100,400,fill = "red",tags="nivel2")
    nivel3 = cnv.create_rectangle(xCentro - 100,500,xCentro + 100,600,fill = "red",tags="nivel3")
    nivel1text = cnv.create_text((xCentro,150), text="nivel 1", font = "arial 20",tags="nivel1")
    nivel2text = cnv.create_text((xCentro,350), text="nivel 2", font = "arial 20",tags="nivel2")
    nivel3text = cnv.create_text((xCentro,550), text="nivel 3", font = "arial 20",tags="nivel3")
    
def redesenhaCirculos(cnv):
    global sizeR,yR,columnR,rowR

    listaCoresDisponiveis = game_rules.cores[0:game_rules.n_de_cores]
    nPedras = game_rules.nPedras
    limiteJogadas = game_rules.limiteJogadas

    if columnR <  limiteJogadas:
        if rowR < nPedras:
            x1 = rowR * SIZE
            y1 = columnR * SIZE
            x2 = x1 + SIZE
            y2 = y1 + SIZE
            cnv.create_oval(x1,y1,x2,y2, fill=game_rules.tentativaSenha[rowR])
            #desenha as marcas da tentativa de senha
            if(len(game_rules.respostaSenha) == game_rules.nPedras):
                for i in range(nPedras):
                    x1 = (rowR+i+1) * SIZE +10
                    y1 = columnR * SIZE 
                    x2 = x1 + SIZE 
                    y2 = y1 + SIZE
                    #if(game_rules.respostaSenha[i] != 'vazia'):#se o espaco for preto ou branco desenha a cor ao lado
                    cnv.create_oval(x1,y1,x2,y2, fill=game_rules.respostaSenha[i])
            rowR+=1
            if rowR == nPedras:
                rowR = 0
                columnR +=1
                game_rules.tentativaSenha = []

