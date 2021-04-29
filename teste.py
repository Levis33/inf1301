from model import game_rules


def testeDificuldade():
    game_rules.setDificuldade("facil")
    print(game_rules.dificuldade)
    print(game_rules.n_de_cores)



def testeCriaSenha():
    game_rules.setDificuldade("facil")
    game_rules.criaSenha()
    print(game_rules.senha)


def testeTentativaJogador():
    game_rules.setDificuldade("facil")
    game_rules.tentativaJogador()
    print(game_rules.tentativaSenha)


def testeCompara():
    game_rules.setDificuldade("facil")
    game_rules.criaSenha()
    game_rules.tentativaJogador()
    game_rules.compara()
    print(game_rules.respostaSenha)


testeDificuldade()
testeCriaSenha()
testeTentativaJogador()
testeCompara()


