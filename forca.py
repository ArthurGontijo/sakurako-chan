import random


palavra = ''
output = []
vidas = 6
terminado = False
usadas = []


def sortear_e_limpar():
    global palavra, output, vidas, terminado, usadas
    palavra = ''
    output = []
    vidas = 6
    terminado = False
    usadas = []
    f = open('palavras.txt', encoding='utf8')
    linhas = f.readlines()
    palavra = random.choice(linhas).lower().strip('\n')
    fazer_tracos(palavra)
    return imprimir_palavra_com_tracos(output)


def fazer_tracos(plv):
    for letra in plv:
        output.append('-')


def imprimir_palavra_com_tracos(lista):
    str = ''
    for x in lista:
        str += x
    
    return str 


def checar_letra(chute):
    chute = chute.lower()
    global palavra, output, vidas, terminado, usadas
    acertou = False
    if terminado == True:
        return 'O jogo já acabou! Utilize o comando *forcanovo para iniciar um novo jogo.'
    
    else:
        if chute not in 'abcdefghijklmnopqrstuvwxyzáãâéêõôíç':
            return 'Por favor utilize letras.'
        elif chute in usadas:
            return 'Você já falou essa letra.'
        else:
            for x in range(0, len(palavra)):
                if palavra[x] == chute:
                    output[x] = chute
                    acertou = True
            if acertou == False:
                vidas -= 1
                if vidas == 0:
                    terminado = True
                    return f'Você perdeu! A resposta era: {palavra}'
                else:
                    return imprimir_palavra_com_tracos(output) + '\n' + f'Vidas = {vidas}'
            elif imprimir_palavra_com_tracos(output) == palavra:
                terminado = True
                return imprimir_palavra_com_tracos(output) + '\n' + f'Parabéns! Você venceu!'
            else:

                usadas.append(chute)
                return imprimir_palavra_com_tracos(output) + '\n' + f'Vidas = {vidas}'
