#Thiago Levis Alambert Rodrigues
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
    #desenha os circulos de opcoes disponiveis no canto inferior esquerdo
    for j in range(len(listaCoresDisponiveis)):
       cnv.create_oval(j * SIZE, (Y + 1) * SIZE - 400, (j + 1) * SIZE, (Y + 2) * SIZE - 400, fill = listaCoresDisponiveis[j], width = 5,tags='cores')
    #desenha os circulos cinzas via coluna/linha de acordo com as variaveis do nivel
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
    #utilizando tags podemos referenciar o retangulo passando a variavel "nivelX" utilizando uma funcao tag_binds do canvas (utilizada na game.py)
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
    # o codigo abaixo desenha os circulos de dicas (branco,preto e cinza) ao lado dos circulos ja existentes do proprio jogo
    #verifica se ainda esta dentro do limite da dificuldade
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
                    cnv.create_oval(x1,y1,x2,y2, fill=game_rules.respostaSenha[i])
            rowR+=1
            if rowR == nPedras:
                rowR = 0
                columnR +=1
                game_rules.tentativaSenha = []


def desenhaVitoriaouDerrota(cnv,vitoriaOuDerrota):
    cnv.delete("all")

    if(vitoriaOuDerrota):
        texto = cnv.create_text((xCentro,150), text="Voce Ganhou! a senha era", font = "arial 20")
    else:
        texto = cnv.create_text((xCentro,150), text="Voce Perdeu! a senha era", font = "arial 20")
    #o codigo abaixo desenha a resposta(circulos da senha) na tela no final do jogo
    for j in range(len(game_rules.senha)):
           cnv.create_oval(j * SIZE +500, (Y + 1) * SIZE - 850, (j + 1) * SIZE +500, (Y + 2) * SIZE - 850, fill = game_rules.senha[j], width = 5)

    textoSaida = cnv.create_text((xCentro,300), text="Para jogar novamente reinicie o jogo", font = "arial 20")
    
