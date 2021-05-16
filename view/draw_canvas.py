from model import game_rules

SIZE = 50
Y = 20

xCentro = 600
yCentro = 350

def inicia(nivel):
    game_rules.setDificuldade(nivel)
    game_rules.criaSenha()
    print(game_rules.senha)
 
    
def desenha(cnv):
    listaCoresDisponiveis = game_rules.cores[0:game_rules.n_de_cores]
    nPedras = game_rules.nPedras
    limiteJogadas = game_rules.limiteJogadas
    
    for j in range(len(listaCoresDisponiveis)):
       cnv.create_oval(j * SIZE, (Y + 1) * SIZE - 400, (j + 1) * SIZE, (Y + 2) * SIZE - 400, fill = listaCoresDisponiveis[j], width = 5)

    for column in range(nPedras):
            for row in range(limiteJogadas):
                x1 = column * SIZE
                y1 = row * SIZE
                x2 = x1 + SIZE
                y2 = y1 + SIZE
                cnv.create_oval(x1,y1,x2,y2, fill="gray")


def escolheNivel(cnv):
    global xCentro, yCentro
    cnv.create_text((xCentro,50), fill="darkblue" ,text="escolha um nivel e clique em 'iniciar'", font = "arial 20")
    cnv.create_rectangle(xCentro - 100,100,xCentro + 100,200,fill = "red")
    cnv.create_rectangle(xCentro - 100,300,xCentro + 100,400,fill = "red")
    cnv.create_rectangle(xCentro - 100,500,xCentro + 100,600,fill = "red")
    cnv.create_text((xCentro,150), text="nivel 1", font = "arial 20")
    cnv.create_text((xCentro,350), text="nivel 2", font = "arial 20")
    cnv.create_text((xCentro,550), text="nivel 3", font = "arial 20")
   