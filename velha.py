tabuleiro = ['-', '-', '-',
             '-', '-', '-',
             '-', '-', '-']

x = False         # Variável que define se é ou não a vez do jogador X jogar.
cont = 0          # Variável que conta quantas jogadas já se passaram. 
terminado = False # Variável que indica se o jogo já acabou ou não.


# Função que checa se o jogador especificado pelo parâmetro "jog" completou alguma linha do tabuleiro.
def checar_linha(tab, jog):
    if (tab[0] == tab[1] and tab[0] == tab[2] and tab[0] != '-') or (tab[3] == tab[4] and tab[3] == tab[5] and tab[3] != '-') or (tab[6] == tab[7] and tab[6] == tab[8] and tab[6] != '-'):
        return True


# Função que checa se o jogador especificado pelo parâmetro "jog" completou alguma coluna do tabuleiro.
def checar_coluna(tab, jog):
    if (tab[0] == tab[3] and tab[0] == tab[6] and tab[0] != '-') or (tab[1] == tab[4] and tab[1] == tab[7] and tab[1] != '-') or (tab[2] == tab[5] and tab[2] == tab[8] and tab[2] != '-'):
        return True


# Função que checa se o jogador especificado pelo parâmetro "jog" completou alguma diagonal do tabuleiro.
def checar_diag(tab, jog):
    if (tab[0] == tab[4] and tab[0] == tab[8] and tab[0] != '-') or (tab[2] == tab[4] and tab[2] == tab[6] and tab[2] != '-'):
        return True


# Função que reune todas as funções anteriores e retorna um valor booleano indicando se houve ou não vitória de algum jogador.
def checar_tudo(tab, jog):
    if checar_coluna(tab, jog) == True or checar_linha(tab, jog) == True or checar_diag(tab, jog) == True:
        return True


# Função que retorna uma string formatada do tabuleiro para facilitar a visualização dos jogadores.
def imprimir(tab):
    str = ''
    for x in range (0, len(tab)):
        if (x + 1) % 3 == 0:
            str = str + '­ | ' + tab[x] + ' ' + '|\n'
        else:
            str = str + '­ | ' + tab[x]

    return str


# Função que modifica alguma casa do tabuleiro (caso esta esteja vazia), e retorna um vencedor caso o resultado de checar_tudo() seja Verdadeiro.
def jogada(pos):
    global x, cont, terminado
    tab = tabuleiro
    x = not x
    if terminado == False:
        try:
            pos = int(pos)
        except:
            return 'Por favor digite um número para escolher a casa.'
        else:
            try:
                if tab[pos - 1]:
                    pass
            except:
                return 'Não tem essa casa no jogo. Tente Novamente'
            else:
                if tab[pos - 1] != '-':
                    return 'Já tem gente ai! Escolha outra casa'
                else:
                    if x == True:
                        tab[pos - 1] = 'x'
                        cont += 1
                        if checar_tudo(tab, 'x') == True:
                            terminado = True
                            return imprimir(tabuleiro) + f'O jogo acabou! Parabéns, X. Você ganhou.'
                            
                        elif cont > 8:
                            return imprimir(tabuleiro) + 'Empate! Ninguém venceu.'
                        else:
                            return imprimir(tabuleiro) + 'É sua vez O. Em qual casa deseja jogar? '
                    else:
                        tab[pos - 1] = '○'
                        cont += 1
                        if checar_tudo(tab, '○') == True:
                            terminado = True
                            return imprimir(tabuleiro) + f'O jogo acabou! Parabéns, O. Você ganhou.'
                            
                        else:
                            return imprimir(tabuleiro) + 'É sua vez X. Em qual casa deseja jogar?'
                    

    else:
        return 'O jogo já acabou. Utilize o comando *velha para limpar o tabuleiro.'       


# Função que "limpa" o array 'tabuleiro' e reseta os valores das variáveis 'x', 'cont' e 'terminado' para seus respectivos valores padrões
def resetar():
    global tabuleiro, x, cont, terminado
    tabuleiro = tabuleiro = ['-', '-', '-',
                             '-', '-', '-',
                             '-', '-', '-']
    x = False
    cont = 0
    terminado = False

    return 'Vamos Jogar!' + '\n' + imprimir(tabuleiro) + 'É sua vez X. Em qual casa deseja jogar?'
