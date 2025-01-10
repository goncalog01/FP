# Goncalo Filipe Costa Guerreiro  95581

##########################################################################################################
#                                               TAD posicao                                              #
##########################################################################################################
# Representacao interna: {'x': x, 'y': y}                                                                #
##########################################################################################################
# cria_posicao: N2 -> posicao                                                                            #
#                                                                                                        #
# cria_copia_posicao: posicao -> posicao                                                                 #
#                                                                                                        #
# obter_pos_x: posicao -> N                                                                              #
#                                                                                                        #
# obter_pos_y: posicao -> N                                                                              #
#                                                                                                        #
# eh_posicao: universal -> booleano                                                                      #
#                                                                                                        #
# posicoes_iguais: posicao x posicao -> booleano                                                         #
#                                                                                                        #
# posicao_para_str: posicao -> str                                                                       #
##########################################################################################################

######################
# Funcoes auxiliares #
######################

def int_nao_neg(n):
    return isinstance(n, int) and n >= 0

def igual(x, y):
    return x == y

#####################
# Operacoes basicas #
#####################

def cria_posicao(x, y):
    '''
    A funcao cria_posicao recebe os valores correspondentes as coordenadas 
    de uma posicao e devolve a posicao correspondente.

    cria_posicao: N2 -> posicao
    '''

    if int_nao_neg(x) and int_nao_neg(y):
        return {'x': x, 'y': y}
    else:
        raise ValueError ('cria_posicao: argumentos invalidos')
    
def cria_copia_posicao(pos):
    '''
    A funcao cria_copia_posicao recebe uma posicao
    e devolve uma copia nova da posicao.

    cria_copia_posicao: posicao -> posicao
    '''

    return cria_posicao(pos['x'], pos['y'])

def obter_pos_x(pos):
    '''
    A funcao obter_pos_x recebe uma posicao e devolve a sua componente x.

    obter_pos_x: posicao -> N
    '''

    return pos['x']

def obter_pos_y(pos):
    '''
    A funcao obter_pos_y recebe uma posicao e devolve a sua componente y.

    obter_pos_y: posicao -> N
    '''    
    return pos['y']

def eh_posicao(arg):
    '''
    A funcao eh_posicao devolve True caso o seu argumento 
    seja um TAD posicao e False caso contrario.

    eh_posicao: universal -> booleano
    '''

    return isinstance(arg, dict) and len(arg) == 2 and 'x' in arg and \
           'y' in arg and int_nao_neg(arg['x']) and int_nao_neg(arg['y'])

def posicoes_iguais(pos1, pos2):
    '''
    A funcao posicoes_iguais recebe duas posicoes e
    devolve True apenas se as posicoes sao iguais.

    posicoes_iguais: posicao x posicao -> booleano
    '''

    return igual(pos1['x'], pos2['x']) and igual(pos1['y'], pos2['y'])

def posicao_para_str(pos):
    '''
    A funcao posicao_para_str recebe uma posicao e devolve a cadeia de caracteres '(x, y)'
    que a representa, sendo os valores x e y as suas coordenadas.

    posicao_para_str: posicao -> str
    '''

    return str((obter_pos_x(pos), obter_pos_y(pos)))

#########################
# Funcoes de alto nivel #
#########################

def obter_posicoes_adjacentes(pos):
    '''
    A funcao obter_posicoes_adjacentes recebe uma posicao e devolve um tuplo com as posicoes
    adjacentes a essa posicao de acordo com a ordem de leitura de um labirinto.

    obter_posicoes_adjacentes: posicao -> tuplo de posicoes
    '''

    posicoes_adj = ()
    
    # em cada caso verifica se a posicao adjacente e' uma posicao valida
    # e se for esse caso a posicao e' adicionada ao tuplo
    if int_nao_neg(obter_pos_x(pos)) and int_nao_neg(obter_pos_y(pos) - 1):
        pos_adj = cria_posicao(obter_pos_x(pos), obter_pos_y(pos) - 1)
        posicoes_adj = posicoes_adj + (pos_adj,)
        
    if int_nao_neg(obter_pos_x(pos) - 1) and int_nao_neg(obter_pos_y(pos)):
        pos_adj = cria_posicao(obter_pos_x(pos) - 1, obter_pos_y(pos))
        posicoes_adj = posicoes_adj + (pos_adj,)
        
    if int_nao_neg(obter_pos_x(pos) + 1):
        pos_adj = cria_posicao(obter_pos_x(pos) + 1, obter_pos_y(pos))
        posicoes_adj = posicoes_adj + (pos_adj,)
        
    if int_nao_neg(obter_pos_y(pos) + 1):
        pos_adj = cria_posicao(obter_pos_x(pos), obter_pos_y(pos) + 1)
        posicoes_adj = posicoes_adj + (pos_adj,)
        
    return posicoes_adj


##########################################################################################################
#                                               TAD unidade                                              #
##########################################################################################################
# Representacao interna: {'pos': posicao, 'vida': vida, 'forca': forca, 'exer': exercito}                #
##########################################################################################################
# cria_unidade: posicao x N x N x str -> unidade                                                         #
#                                                                                                        #
# cria_copia_unidade: unidade -> unidade                                                                 #
#                                                                                                        #
# obter_posicao: unidade -> posicao                                                                      #
#                                                                                                        #
# obter_exercito: unidade -> str                                                                         #
#                                                                                                        #
# obter_forca: unidade -> N                                                                              #
#                                                                                                        #
# obter_vida: unidade -> N                                                                               #
#                                                                                                        #
# muda_posicao: unidade x posicao -> unidade                                                             #
#                                                                                                        #
# remove_vida: unidade x N -> unidade                                                                    #
#                                                                                                        #
# eh_unidade: universal -> booleano                                                                      #
#                                                                                                        #
# unidades_iguais: unidade x unidade -> booleano                                                         #
#                                                                                                        #
# unidade_para_char: unidade -> str                                                                      #
#                                                                                                        #
# unidade_para_str: unidade -> str                                                                       #
##########################################################################################################

######################
# Funcoes auxiliares #
######################

def int_pos(n):
    return isinstance(n, int) and n > 0

def cad_car(cc):
    return isinstance(cc, str) and cc != ''

#####################
# Operacoes basicas #
#####################

def cria_unidade(pos, vida, forca, exer):
    '''
    A funcao cria_unidade recebe uma posicao, dois valores inteiros maiores que 0
    correspondentes a vida e forca da unidade, e uma cadeia de caracteres nao vazia
    correspondente ao exercito da unidade; e devolve a unidade correspondente.

    cria_unidade: posicao x N x N x str -> unidade
    '''

    if eh_posicao(pos) and int_pos(vida) and int_pos(forca) and cad_car(exer):
        return {'pos': pos, 'vida': vida, 'forca': forca, 'exer': exer}
    else:
        raise ValueError ('cria_unidade: argumentos invalidos')
    
def cria_copia_unidade(uni):
    '''
    A funcao cria_copia_unidade recebe uma unidade
    e devolve uma nova copia da unidade.

    cria_copia_unidade: unidade -> unidade
    '''

    return cria_unidade(uni['pos'], uni['vida'], uni['forca'], uni['exer'])

def obter_posicao(uni):
    '''
    A funcao obter_posicao recebe uma unidade e devolve a sua posicao.

    obter_posicao: unidade -> posicao
    '''

    return uni['pos']

def obter_exercito(uni):
    '''
    A funcao obter_exercito recebe uma unidade e devolve a cadeia
    de caracteres correspondente ao seu exercito.

    obter_exercito: unidade -> str
    '''

    return uni['exer']

def obter_forca(uni):
    '''
    A funcao obter_forca recebe uma unidade e devolve
    o valor correspondente a sua forca de ataque.

    obter_forca: unidade -> N
    '''

    return uni['forca']

def obter_vida(uni):
    '''
    A funcao obter_vida recebe uma unidade e devolve
    o valor correspondente aos seus pontos de vida.

    obter_vida: unidade -> N
    '''

    return uni['vida']

def muda_posicao(uni, pos):
    '''
    A funcao muda_posicao recebe uma unidade e uma posicao, modifica destrutivamente
    a unidade alterando a sua posicao com o novo valor, e devolve a propria unidade.

    muda_posicao: unidade x posicao -> unidade
    '''

    uni['pos'] = pos
    return uni

def remove_vida(uni, vida):
    '''
    A funcao remove_vida recebe uma unidade e um valor, modifica destrutivamente a
    unidade alterando os seus pontos de vida substraindo o valor, e devolve a propria unidade.

    remove_vida: unidade x N -> unidade
    '''

    uni['vida'] = uni['vida'] - vida
    return uni

def eh_unidade(arg):
    '''
    A funcao eh_unidade devolve True caso o seu argumento
    seja um TAD unidade e False caso contrario.

    eh_unidade: universal -> booleano
    '''

    return isinstance(arg, dict) and len(arg) == 4 and 'pos' in arg and \
           'vida' in arg and 'forca' in arg and 'exer' in arg and \
           eh_posicao(arg['pos']) and int_pos(arg['vida']) and \
           int_pos(arg['forca']) and cad_car(arg['exer'])

def unidades_iguais(uni1, uni2):
    '''
    A funcao unidades_iguais recebe duas unidades e
    devolve True apenas se as unidades sao iguais.

    unidades_iguais: unidade x unidade -> booleano
    '''

    return igual(uni1['pos'], uni2['pos']) and igual(uni1['vida'], uni2['vida']) and \
           igual(uni1['forca'], uni2['forca']) and igual(uni1['exer'], uni2['exer'])

def unidade_para_char(uni):
    '''
    A funcao unidade_para_char recebe uma unidade e devolve a cadeia de caracteres
    dum unico elemento, correspondente ao primeiro caracter em maiuscula do seu exercito.

    unidade_para_char: unidade -> str
    '''

    if ord(uni['exer'][0]) < 97 or ord(uni['exer'][0]) > 122:
    # se o primeiro caracter nao for uma letra minuscula, devolve o proprio caracter
        return uni['exer'][0]
    else:
    # se o primeiro caracter for uma letra minuscula, transforma-o em letra maiuscula
        return chr(ord(uni['exer'][0]) - 32)
    
def unidade_para_str(uni):
    '''
    A funcao unidade_para_str recebe um unidade e
    devolve a cadeia de caracteres que a representa.

    unidade_para_str: unidade -> str
    '''

    return unidade_para_char(uni) + '[' + str(uni['vida']) + ', ' + str(uni['forca']) + \
           ']@' + posicao_para_str(uni['pos'])

#########################
# Funcoes de alto nivel #
#########################

def unidade_ataca(uni1, uni2):
    '''
    A funcao unidade_ataca recebe duas unidades e modifica destrutivamente a unidade 2
    retirando o valor de pontos de vida correspondente a forca de ataque da unidade 1.
    A funcao devolve True se a unidade 2 for destruida ou False caso contrario.

    unidade_ataca: unidade x unidade -> booleano
    '''

    uni2 = remove_vida(uni2, obter_forca(uni1))
    if obter_vida(uni2) > 0:
        return False
    else:
        return True
    
def ordenar_unidades(conj_uni):
    '''
    A funcao ordenar_unidades recebe um tuplo de unidades e devolve um tuplo
    contendo as mesmas unidades do tuplo fornecido como argumento, ordenadas
    de acordo com a ordem de leitura do labirinto.

    ordenar_unidades: tuplo unidades -> tuplo unidades
    '''

    def chave_ord(uni):
    # a chave de ordenacao devolve as coordenadas das posicoes na ordem inversa
    # de forma a ordenar primeiro segundo os yy e apenas depois segundo os xx
    # de acordo com a ordem de leitura do labirinto
        return (obter_pos_y(obter_posicao(uni)), obter_pos_x(obter_posicao(uni)))
    
    return tuple(sorted(conj_uni, key = chave_ord))


##########################################################################################################
#                                                TAD mapa                                                #
##########################################################################################################
# Representacao interna: {'dim': dimensao, 'paredes': paredes, 'exer1': exercito 1, 'exer2': exercito 2} #
##########################################################################################################
# cria_mapa: tuplo x tuplo x tuplo x tuplo -> mapa                                                       #
#                                                                                                        #
# cria_copia_mapa: mapa -> mapa                                                                          #
#                                                                                                        #
# obter_tamanho: mapa -> tuplo                                                                           #
#                                                                                                        #
# obter_nome_exercitos: mapa -> tuplo                                                                    #
#                                                                                                        #
# obter_unidades_exercito: mapa x str -> tuplo unidades                                                  #
#                                                                                                        #
# obter_todas_unidades: mapa -> tuplo                                                                    #
#                                                                                                        #
# obter_unidade: mapa x posicao -> unidade                                                               #
#                                                                                                        #
# eliminar_unidade: mapa x unidade -> mapa                                                               #
#                                                                                                        #
# mover_unidade: mapa x unidade x posicao -> mapa                                                        #
#                                                                                                        #
# eh_posicao_unidade: mapa x posicao -> booleano                                                         #
#                                                                                                        #
# eh_posicao_corredor: mapa x posicao -> booleano                                                        #
#                                                                                                        #
# eh_posicao_parede: mapa x posicao -> booleano                                                          #
#                                                                                                        #
# mapas_iguais: mapa x mapa -> booleano                                                                  #
#                                                                                                        #
# mapa_para_str: mapa -> str                                                                             #
##########################################################################################################

######################
# Funcoes auxiliares #
######################

def verifica_dim(dim):
    return isinstance(dim, tuple) and len(dim) == 2 and isinstance(dim[0], int) and \
           isinstance(dim[1], int) and dim[0] >= 3 and dim[1] >= 3

def verifica_paredes(paredes, dim):
    if isinstance(paredes, tuple):
        for pos in paredes:
            if not (eh_posicao(pos) and 0 < obter_pos_x(pos) < dim[0] - 1 and \
                    0 < obter_pos_y(pos) < dim[1] - 1):
                return False
        return True
    else:
        return False
    
def verifica_exer(exer, dim):
    if isinstance(exer, tuple) and len(exer) > 0:
        for uni in exer:
            if not (eh_unidade(uni) and 0 < obter_pos_x(obter_posicao(uni)) < dim[0] - 1 and \
                    0 < obter_pos_y(obter_posicao(uni)) < dim[1] - 1):
                return False
        return True
    else:
        return False
    
#####################
# Operacoes basicas #
#####################

def cria_mapa(dim, paredes, exer1, exer2):
    '''
    A funcao cria_mapa recebe um tuplo de 2 valores inetiros correspondentes a dimensao,
    um tuplo de posicoes correspondentes as paredes interiores do labirinto e dois tuplos
    de unidades correspondentes aos dois exercitos; e devolve o mapa que representa
    internamente o labirinto e as unidades presentes.

    cria_mapa: tuplo x tuplo x tuplo x tuplo -> mapa
    '''

    if verifica_dim(dim) and verifica_paredes(paredes, dim) and \
       verifica_exer(exer1, dim) and verifica_exer(exer2, dim):
        return {'dim': dim, 'paredes': paredes, 'exer1': exer1, 'exer2': exer2}
    else:
        raise ValueError ('cria_mapa: argumentos invalidos')
    
def cria_copia_mapa(mapa):
    '''
    A funcao cria_copia_mapa recebe um mapa e devolve uma nova copia do mapa.

    cria_copia_mapa: mapa -> mapa
    '''

    d = mapa['dim']
    w = mapa['paredes']
    exer1 = ()
    exer2 = ()
    for uni in mapa['exer1']:
        exer1 = exer1 + (cria_unidade(obter_posicao(uni), obter_vida(uni), obter_forca(uni), obter_exercito(uni)),)
    for uni in mapa['exer2']:
        exer2 = exer2 + (cria_unidade(obter_posicao(uni), obter_vida(uni), obter_forca(uni), obter_exercito(uni)),)
    return cria_mapa(d, w, exer1, exer2)

def obter_tamanho(mapa):
    '''
    A funcao obter_tamanho recebe um mapa e devolve um tuplo de dois valores inteiros
    correspondendo o primeiro deles a dimensao x e o segundo a dimensao y do mapa.

    obter_tamanho: mapa -> tuplo
    '''

    return mapa['dim']

def obter_nome_exercitos(mapa):
    '''
    A funcao obter_nome_exercitos recebe um mapa e devolve devolve um tuplo ordenado
    com duas cadeias de caracteres correspondendo aos nomes dos exercitos do mapa.

    obter_nome_exercitos: mapa -> tuplo
    '''

    return tuple(sorted((obter_exercito(mapa['exer1'][0]), obter_exercito(mapa['exer2'][0]))))

def obter_unidades_exercito(mapa, exer):
    '''
    A funcao obter_unidades_exercito recebe um mapa e uma cadeia de caracteres correspondente
    ao nome de um dos exercito do mapa e devolve um tuplo contendo as unidades do mapa
    pertencentes ao exercito indicado, ordenadas em ordem de leitura do labirinto.

    obter_unidades_exercito: mapa x str -> tuplo unidades
    '''

    for uni in mapa['exer1']:
        if obter_exercito(uni) == exer:
            return ordenar_unidades(mapa['exer1'])
    for uni in mapa['exer2']:
        if obter_exercito(uni) == exer:
            return ordenar_unidades(mapa['exer2'])
    # se a cadeira de caracteres corresponder a um exercito sem unidades, devolve um tuplo vazio
    return ()
    
def obter_todas_unidades(mapa):
    '''
    A funcao obter_todas_unidades recebe um mapa e devolve um tuplo contendo
    todas as unidades do mapa, ordenadas em ordem de leitura do labirinto.

    obter_todas_unidades: mapa -> tuplo
    '''

    return ordenar_unidades(mapa['exer1'] + mapa['exer2'])

def obter_unidade(mapa, pos):
    '''
    A funcao obter_unidade recebe um mapa e uma posicao e
    devolve a unidade do mapa que se encontra na posicao.

    obter_unidade: mapa x posicao -> unidade
    '''

    for uni in obter_todas_unidades(mapa):
        if posicoes_iguais(obter_posicao(uni), pos):
            return uni
        
def eliminar_unidade(mapa, uni):
    '''
    A funcao eliminar_unidade recebe um mapa e uma unidade, e modifica destrutivamente
    o mapa eliminando a unidade do mapa e deixando livre a posicao onde
    se encontrava a unidade. Devolve o proprio mapa.

    eliminar_unidade: mapa x unidade -> mapa
    '''

    if uni in mapa['exer1']:
        exer_str = 'exer1'
    else:
        exer_str = 'exer2'

    exer = obter_exercito(mapa[exer_str][0])
    i = 0
    
    while i < len(obter_unidades_exercito(mapa, exer)):
    # percorre as unidades do exercito
        if unidades_iguais(obter_unidades_exercito(mapa, exer)[i], uni):
        # quando encontra a unidade a eliminar, modifica destrutivamente o exercito no mapa;
        # o exercito passa apenas a contar as unidades que se encontram antes e depois
        # da unidade a remover, sendo esta eliminada
            mapa[exer_str] = obter_unidades_exercito(mapa, exer)[:i] + \
                obter_unidades_exercito(mapa, exer)[i + 1:]
        i = i + 1
        
    return mapa

def mover_unidade(mapa, uni, pos):
    '''
    A funcao mover_unidade recebe um mapa, uma unidade e uma posicao, e modifica
    destrutivamente o mapa e a unidade alterando a posicao da unidade no mapa
    para a nova posicao e deixando livre a posicao onde se encontrava.
    Devolve o proprio mapa.

    mover_unidade: mapa x unidade x posicao -> mapa
    '''

    if uni in mapa['exer1']:
        exer = obter_exercito(mapa['exer1'][0])
    else:
        exer = obter_exercito(mapa['exer2'][0])
        
    for unidade in obter_unidades_exercito(mapa, exer):
    # percorre as unidades do exercito
        if unidades_iguais(uni, unidade):
        # quando encontra a unidade, altera a sua posicao
            unidade = muda_posicao(unidade, pos)
    return mapa

def eh_posicao_unidade(mapa, pos):
    '''
    A funcao eh_posicao_unidade recebe um mapa e uma posicao, e devolve True
    apenas no caso da posicao do mapa estar ocupada por uma unidade.

    eh_posicao_unidade: mapa x posicao -> booleano
    '''

    for uni in obter_todas_unidades(mapa):
    # percorre todas as unidades do mapa
        if posicoes_iguais(obter_posicao(uni), pos):
        # verifica se alguma das unidades se encontra na posicao
            return True
    return False

def eh_posicao_corredor(mapa, pos):
    '''
    A funcao eh_posicao_corredor recebe um mapa e uma posicao, e devolve True
    apenas no caso da posicao do mapa corresponder a um corredor no labirinto
    (independentemente de estar ou nao ocupado por uma unidade).

    eh_posicao_corredor: mapa x posicao -> booleano
    '''
    # verifica se a posicao se encontra dentro do mapa, sem corresponder a uma parede
    return 0 < obter_pos_x(pos) < obter_tamanho(mapa)[0] - 1 and \
           0 < obter_pos_y(pos) < obter_tamanho(mapa)[1] - 1 and \
           pos not in mapa['paredes']

def eh_posicao_parede(mapa, pos):
    '''
    A funcao eh_posicao_parede recebe um mapa e uma posicao, e devolve True
    apenas no caso da posicao do mapa corresponder a uma parede do labirinto.

    eh_posicao_parede: mapa x posicao -> booleano
    '''
    # verifica se posicao pertence aos limites exteriores do mapa ou se corresponde a uma parede interior
    return obter_pos_x(pos) == 0 or obter_pos_x(pos) == obter_tamanho(mapa)[0] - 1 or \
           obter_pos_y(pos) == 0 or obter_pos_y(pos) == obter_tamanho(mapa)[1] - 1 or \
           pos in mapa['paredes']

def mapas_iguais(mapa1, mapa2):
    '''
    A funcao mapas_iguais recebe dois mapas e devolve True apenas se os mapas sao iguais.

    mapas_iguais: mapa x mapa -> booleano
    '''

    return igual(obter_tamanho(mapa1), obter_tamanho(mapa2)) and \
           igual(mapa1['paredes'], mapa2['paredes']) and \
           igual(mapa1['exer1'], mapa2['exer1']) and igual(mapa1['exer2'], mapa2['exer2'])

def mapa_para_str(mapa):
    '''
    A funcao mapa_para_str recebe um mapa e devolve uma cadeia de caracteres que
    representa o mapa, com as unidades representadas pela sua representacao externa.

    mapa_para_str: mapa -> str
    '''

    l = ''
    for y in range(obter_tamanho(mapa)[1]):
        for x in range(obter_tamanho(mapa)[0]):
            if eh_posicao_parede(mapa, cria_posicao(x, y)):
            # verifica se a posicao corresponde a uma parede
                l = l + '#'
            elif eh_posicao_unidade(mapa, cria_posicao(x, y)):
            # verifica se a posicao corresponde a uma unidade
                # se for esse o caso, escreve a letra que representa o exercito da unidade
                l = l + unidade_para_char(obter_unidade(mapa, cria_posicao(x, y)))
            else:
            # a posicao corresponde a um espaco livre
                l = l + '.'
        if y < obter_tamanho(mapa)[1] - 1:
            l = l + '\n'
    return l

#########################
# Funcoes de alto nivel #
#########################

def obter_inimigos_adjacentes(mapa, uni):
    '''
    A funcao obter_inimigos_adjacentes recebe um mapa e uma unidade e devolve um tuplo
    contendo as unidades inimigas adjacentes a unidade de acordo com a ordem de leitura do labirinto.
    
    obter_inimigos_adjacentes: mapa x unidade -> tuplo unidades
    '''

    uni_adj = ()
    
    for pos in obter_posicoes_adjacentes(obter_posicao(uni)):
    # percorre todas as posicoes adjacentes 'a posicao da unidade
        if eh_posicao_unidade(mapa, pos) and \
           obter_exercito(obter_unidade(mapa, pos)) != obter_exercito(uni):
        # se a posicao corresponder a uma unidade do exercito inimigo,
        # entao a unidade e' adicionada ao tuplo
            uni_adj = uni_adj + (obter_unidade(mapa, pos),)
            
    return ordenar_unidades(uni_adj)

def obter_movimento(mapa, unit):
    '''
    A funcao obter_movimento devolve a posicao seguinte da unidade argumento
    de acordo com as regras de movimento das unidades no labirinto.

    obter_movimento: mapa x unidade -> posicao
    '''

    ######################
    # Funcoes auxiliares #
    ######################
    def pos_to_tuple(pos):
        return obter_pos_x(pos), obter_pos_y(pos)

    def tuple_to_pos(tup):
        return cria_posicao(tup[0], tup[1])

    def tira_repetidos(tup_posicoes):
        conj_tuplos = set(tuple(map(pos_to_tuple, tup_posicoes)))
        return tuple(map(tuple_to_pos, conj_tuplos))

    def obter_objetivos(source):
        enemy_side = tuple(filter(lambda u: u != obter_exercito(source), obter_nome_exercitos(mapa)))[0]
        target_units = obter_unidades_exercito(mapa, enemy_side)
        tup_com_repetidos = \
            tuple(adj
                  for other_unit in target_units
                  for adj in obter_posicoes_adjacentes(obter_posicao(other_unit))
                  if eh_posicao_corredor(mapa, adj) and not eh_posicao_unidade(mapa, adj))
        return tira_repetidos(tup_com_repetidos)

    def backtrack(target):
        result = ()
        while target is not None:
            result = (target,) + result
            target, _ = visited[target]
        return result

    ####################
    # Funcao principal #
    ####################
    # Nao mexer se ja esta' adjacente a inimigo
    if obter_inimigos_adjacentes(mapa, unit):
        return obter_posicao(unit)

    visited = {}
    # posicao a explorar, posicao anterior e distancia
    to_explore = [(pos_to_tuple(obter_posicao(unit)), None, 0)]
    # registro do numero de passos minimo ate primeira posicao objetivo
    min_dist = None
    # estrutura que guarda todas as posicoes objetivo a igual minima distancia
    min_dist_targets = []

    targets = tuple(pos_to_tuple(obj) for obj in obter_objetivos(unit))

    while to_explore:  # enquanto nao esteja vazio
        pos, previous, dist = to_explore.pop(0)

        if pos not in visited:  # posicao foi ja explorada?
            visited[pos] = (previous, dist)  # registro no conjunto de exploracao
            if pos in targets:  # se a posicao atual eh uma dos objetivos
                # se eh primeiro objetivo  ou se esta a  distancia minima
                if min_dist is None or dist == min_dist:
                    # acrescentor 'a lista de posicoes minimas
                    min_dist = dist
                    min_dist_targets.append(pos)
            else:  # nao 'e objetivo, acrescento adjacentes
                for adj in obter_posicoes_adjacentes(tuple_to_pos(pos)):
                    if eh_posicao_corredor(mapa, adj) and not eh_posicao_unidade(mapa, adj):
                        to_explore.append((pos_to_tuple(adj), pos, dist + 1))

        # Parar se estou a visitar posicoes mais distantes que o minimo,
        # ou se ja encontrei todos os objetivos
        if (min_dist is not None and dist > min_dist) or len(min_dist_targets) == len(targets):
            break

    # se encontrei pelo menos uma posicao objetivo, 
    # escolhe a de ordem de leitura menor e devolve o primeiro movimento
    if len(min_dist_targets) > 0:
        # primeiro dos objetivos em ordem de leitura
        tar = sorted(min_dist_targets, key=lambda x: (x[1], x[0]))[0]
        path = backtrack(tar)
        return tuple_to_pos(path[1])

    # Caso nenhuma posicao seja alcancavel
    return obter_posicao(unit)


##########################################################################################################
#                                           Funcoes adicionais                                           #
##########################################################################################################

def calcula_pontos(mapa, exer):
    '''
    A funcao calcula_pontos recebe um mapa e uma cadeia de caracteres correspondente
    ao nome de um dos exercitos do mapa e devolve a sua pontuacao. A pontuacao dum
    exercito e' o total dos pontos de vida de todas as unidades do exercito.
    
    calcula_pontos: mapa x str -> int
    '''

    pontos = 0
    for uni in obter_unidades_exercito(mapa, exer):
    # percorre todas as unidades do exercito, somando os seus pontos de vida
        pontos = pontos + obter_vida(uni)
    return pontos

def simula_turno(mapa):
    '''
    A funcao simula_turno recebe um mapa e modifica-o de acordo com a simulacao de
    um turno de batalha completo, e devolve o proprio mapa. Isto e', seguindo a ordem
    de leitura do labirinto, cada unidade (viva) realiza um unico movimento e (eventualmente)
    um ataque de acordo com as regras de ataque das unidades no labirinto.
    
    simula_turno: mapa -> mapa
    '''

    nomes_exer = obter_nome_exercitos(mapa)
    
    for uni in obter_todas_unidades(mapa):
    # percorre todas a unidades do mapa, por ordem de leitura
        if len(obter_unidades_exercito(mapa, nomes_exer[0])) > 0 and \
           len(obter_unidades_exercito(mapa, nomes_exer[1])) > 0:
        # verifica se nenhum dos exercitos se encontra vazio;
        # se for esse o caso, a batalha terminou, logo nao sao realizados
        # mais movimentos nem ataques
            if obter_vida(uni) > 0:
            # verifica se a unidade ainda se encontra viva
                if len(obter_inimigos_adjacentes(mapa, uni)) == 0:
                # se a unidade nao se encontra adjacente a nenhum inimigo, movimenta-se
                    mapa = mover_unidade(mapa, uni, obter_movimento(mapa, uni))
                if len(obter_inimigos_adjacentes(mapa, uni)) != 0:
                # apos o movimento, volta a verificar se a unidade ja se encontra adjacente a um inimigo;
                # se for esse o caso, ataca
                    if unidade_ataca(uni, obter_inimigos_adjacentes(mapa, uni)[0]):
                    # se a unidade atacada for destruida, entao e' eliminada do mapa
                        mapa = eliminar_unidade(mapa, obter_inimigos_adjacentes(mapa, uni)[0])
                        
    return mapa

def simula_batalha(fich, modo):
    '''
    A funcao simula_batalha recebe um ficheiro (que contem a dimensao e posicoes
    das paredes do mapa e os nomes, vida, forca e unidades de cada um dos exercitos)
    e um modo (True ou False). No modo quiet (False) mostra-se pela saida standard o
    mapa e a pontuacao no inicio da simulacao e apos do ultimo turno de batalha.
    No modo verboso (True), mostra-se tambem o mapa e a pontuacao apos de cada turno de batalha.

    simula_batalha: str x booleano -> str
    '''

    # leitura do ficheiro linha a linha
    f = open(fich, 'r')
    dim = eval(f.readline())
    e1 = eval(f.readline())
    e2 = eval(f.readline())
    w = eval(f.readline())
    pos1 = eval(f.readline())
    pos2 = eval(f.readline())
    f.close()
    
    # tratamento da informacao do ficheiro
    exer1 = tuple(cria_unidade(cria_posicao(p[0], p[1]), e1[1], e1[2], e1[0]) for p in pos1)
    exer2 = tuple(cria_unidade(cria_posicao(p[0], p[1]), e2[1], e2[2], e2[0]) for p in pos2)
    paredes = tuple(cria_posicao(p[0], p[1]) for p in w)
    mapa = cria_mapa(dim, paredes, exer1, exer2)
    mapa_cp = cria_copia_mapa(mapa)
    nomes_exer = obter_nome_exercitos(mapa)
    
    # escreve as pontuacoes iniciais e desenha o mapa
    print(mapa_para_str(mapa))
    print('[ ' + nomes_exer[0] + ':' + str(calcula_pontos(mapa, nomes_exer[0])) + ' ' + \
         nomes_exer[1] + ':' + str(calcula_pontos(mapa, nomes_exer[1])) + ' ]')
    
    while calcula_pontos(mapa, nomes_exer[0]) > 0 and calcula_pontos(mapa, nomes_exer[1]) > 0:
        mapa = simula_turno(mapa)
        if mapas_iguais(mapa, mapa_cp):
        # se o mapa nao e' alterado depois do turno, entao ha empate
            if not modo:
            # se o modo for False (quiet) escreve as pontuacao e desenha o mapa;
            # no caso do modo ser True (verboso) tal nao e' necessario, uma vez
            # que ja foi feito no ciclo anterior
                print(mapa_para_str(mapa))
                print('[ ' + nomes_exer[0] + ':' + str(calcula_pontos(mapa, nomes_exer[0])) + ' ' + \
                     nomes_exer[1] + ':' + str(calcula_pontos(mapa, nomes_exer[1])) + ' ]')
            return 'EMPATE'
        elif modo:
        # se o modo for True (verboso) escereve as pontuacoes e desenha o mapa em cada ciclo
            print(mapa_para_str(mapa))
            print('[ ' + nomes_exer[0] + ':' + str(calcula_pontos(mapa, nomes_exer[0])) + ' ' + \
                 nomes_exer[1] + ':' + str(calcula_pontos(mapa, nomes_exer[1])) + ' ]')
        if len(obter_unidades_exercito(mapa, nomes_exer[0])) > 0 and \
           len(obter_unidades_exercito(mapa, nomes_exer[1])) > 0:
        # verifica se nenhum dos exercitos esta vazio;
        # se esse for o caso entao a batalha acabou, logo nao e' necessario
        # alterar a copia do mapa
            mapa_cp = cria_copia_mapa(mapa)
            
    if not modo:
    # se o modo for False (quiet) escreve as pontuacao e desenha o mapa;
    # no caso do modo ser True (verboso) tal nao e' necessario, uma vez
    # que ja foi feito no ciclo anterior    
        print(mapa_para_str(mapa))
        print('[ ' + nomes_exer[0] + ':' + str(calcula_pontos(mapa, nomes_exer[0])) + ' ' + \
                 nomes_exer[1] + ':' + str(calcula_pontos(mapa, nomes_exer[1])) + ' ]')
        
    if calcula_pontos(mapa, nomes_exer[0]) <= 0:
    # se os pontos do primeiro exercito forem menores ou iguais a zero,
    # entao o segundo exercito venceu
        return nomes_exer[1]
    else:
    # caso contrario, venceu o primeiro exercito
        return nomes_exer[0]