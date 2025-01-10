# 95581  Goncalo Filipe Costa Guerreiro

def eh_labirinto(lab):
    # eh_labirinto: universal -> booleano
    """
    Esta funcao recebe um argumento de qualquer tipo e devolve True se o seu
    argumento corresponde a um labirinto e False caso contrario.
    """
    if isinstance(lab, tuple):
    # verifica se o argumento e' um tuplo
        if len(lab) < 3:
        # verifica se o tamanho do tuplo e' maior ou igual a 3
            return False
        i = 0
        while i < len(lab):
            if not isinstance(lab[i], tuple):
            # verifica se dentro do tuplo apenas existem tuplos
                return False
            elif len(lab[i]) < 3:
            # verifica se cada um dos tuplos tem tamanho igual ou superior a 3
                return False
            for n in lab[i]:
                if not isinstance(n, int) or n not in (0, 1):
                # verifica se dentro de cada tuplo apenas existem inteiros iguais a 0 ou 1
                    return False
            if i == 0 or i == len(lab) - 1:
                for n in lab[i]:
                    if n != 1:
                    # verifica se no primeiro e ultimo tuplos apenas existem 1's
                        return False
            else:
                if lab[i][0] != 1 or lab[i][-1] != 1:
                # verifica se os tuplos do meio comecam e acabam por 1
                    return False
            if i > 0:
                if len(lab[i]) != len(lab[i - 1]):
                # verifica se os tuplos tem todos o mesmo tamanho
                    return False
            i = i + 1
        return True
    else:
        return False

def eh_posicao(pos):
    # eh_posicao: universal -> booleano
    """
    Esta funcao recebe um argumento de qualquer tipo e devolve True se o seu
    argumento corresponde a uma posicao e False caso contrario.
    """
    if isinstance(pos, tuple):
    # verifica se o argumento e' um tuplo
        if len(pos) != 2:
        # verifica se o tuplo tem 2 elementos
            return False
        for n in pos:
            if not isinstance(n, int) or n < 0:
            # verifica se o tuplo e' constituido por inteiros nao negativos
                return False
        return True
    else:
        return False
    
def eh_conj_posicoes(conj_pos):
    # eh_conj_posicoes: universal -> booleano    
    """
    Esta funcao recebe um argumento de qualquer tipo e devolve True se o seu
    argumento corresponde a um conjunto de posicoes unicas e False caso contrario.
    """
    if isinstance(conj_pos, tuple):
    # verifica se o argumento e' um tuplo
        posicoes = ()
        for el in conj_pos:
            if not eh_posicao(el) or el in posicoes:
            # verifica se cada elemento do tuplo e' uma posicao e se nao tem posicoes repetidas
                return False
            else:
                posicoes = posicoes + (el,)
        return True
    else:
        return False
    
def tamanho_labirinto(lab):
    # tamanho_labirinto: labirinto -> tuplo    
    """
    Esta funcao recebe um labirinto e devolve um tuplo de dois valores inteiros
    correspondendo o primeiro deles ao numero de colunas e o segundo ao numero
    de linhas.
    """
    if eh_labirinto(lab):
        colunas = len(lab)
        # o numero de colunas corresponde ao tamanho do tuplo
        linhas = len(lab[0])
        # o numero de linhas corresponde ao tamanho dos tuplos dentro do tuplo
        return (colunas, linhas)
    else:
        raise ValueError ('tamanho_labirinto: argumento invalido')
    
def eh_mapa_valido(lab, conj_pos):
    # eh_mapa_valido: labirinto x conj_posicoes -> booleano
    """
    Esta funcao recebe um labirinto e um conjunto de posicoes correspondente as 
    unidades presentes no labirinto, e devolve True se o segundo argumento
    corresponde a um conjunto de posicoes compativeis (nao ocupadas por paredes)
    dentro do labirinto e False caso contrario.
    """
    if eh_labirinto(lab) and eh_conj_posicoes(conj_pos):
        dim_lab = tamanho_labirinto(lab)
        for pos in conj_pos:
            x = pos[0]
            y = pos[-1]            
            if x >= dim_lab[0] or y >= dim_lab[-1]:
            # verifica se a posicao se encontra dentro do labirinto
                return False
            elif lab[x][y] == 1:
            # verifica se a posicao nao corresponde a uma parede
                return False
        return True
    else:
        raise ValueError ('eh_mapa_valido: algum dos argumentos e invalido')
    
def eh_posicao_livre(lab, conj_uni, pos):
    # eh_posicao_livre: labirinto x conj_posicoes x posicao -> booleano
    """
    Esta funcao recebe um labirinto, um conjunto de posicoes correspondente a
    unidades presentes no labirinto e uma posicao, e devolve True se a posicao
    corresponde a uma posicao livre (nao ocupada nem por paredes, nem por unidades)
    dentro do labirinto e False caso contrario.
    """
    if eh_labirinto(lab) and eh_conj_posicoes(conj_uni) and \
       eh_posicao(pos) and eh_mapa_valido(lab, conj_uni):
        if not eh_mapa_valido(lab, (pos,)) or pos in conj_uni:
        # verifica se a posicao se encontra dentro do labirinto sem corresponder a uma parede nem a uma unidade
            return False
        return True
    else:
        raise ValueError ('eh_posicao_livre: algum dos argumentos e invalido')
    
def posicoes_adjacentes(pos):
    # posicoes_adjacentes: posicao -> conj_posicoes
    """
    Esta funcao recebe uma posicao e devolve o conjunto de posicoes adjacentes
    da posicao em ordem de leitura de um labirinto.
    """
    if eh_posicao(pos):
        conj_pos_adj = ()
        pos_adj1 = (pos[0], pos[-1] - 1)
        pos_adj2 = (pos[0] - 1, pos[-1])
        pos_adj3 = (pos[0] + 1, pos[-1])
        pos_adj4 = (pos[0], pos[-1] + 1)
        pos_adj = (pos_adj1, pos_adj2, pos_adj3, pos_adj4)
        for pos in pos_adj:
            if eh_posicao(pos):
            # verifica se cada uma das posicoes adjacentes corresponde a uma posicao
                conj_pos_adj = conj_pos_adj + (pos,)
        return conj_pos_adj
    else:
        raise ValueError ('posicoes_adjacentes: argumento invalido')
    
def mapa_str(lab, conj_uni):
    # mapa_str: labirinto x conj_posicoes -> cad. carateres
    """
    Esta funcao recebe um labirinto e um conjunto de posicoes correspondente as 
    unidades presentes no labirinto e devolve a cadeia de carateres que as representa.
    """
    if eh_labirinto(lab) and eh_conj_posicoes(conj_uni) and \
       eh_mapa_valido(lab, conj_uni):
        l = ''
        for y in range(len(lab[0])):
            for x in range(len(lab)):
                if lab[x][y] == 1:
                # verifica se a posicao corresponde a uma parede
                    l = l + '#'
                elif (x, y) in conj_uni:
                # verifica se a posicao corresponde a uma unidade
                    l = l + 'O'
                else:
                # se nenhuma das condicoes se verificar, entao corresponde a uma posicao livre
                    l = l + '.'
            if y < len(lab[0]) - 1:
                l = l + '\n'
        return l
    else:
        raise ValueError ('mapa_str: algum dos argumentos e invalido')
    
def obter_objetivos(lab, conj_uni, uni):
    # obter_objetivos: labirinto x conj_posicoes x posicao -> conj_posicoes
    """
    Esta funcao recebe um labirinto, um conjunto de posicoes correspondente
    as unidades presentes no labirinto e uma posicao correspondente a uma das
    unidades, e devolve o conjunto de posicoes (em qualquer ordem) nao ocupadas
    dentro do labirinto correspondente a todos os possiveis objetivos (posicoes
    livres dentro do labirinto adjacentes as restantes unidades) da unidade 
    correspondente a posicao dada.
    """
    if eh_labirinto(lab) and eh_conj_posicoes(conj_uni) and \
       eh_mapa_valido(lab, conj_uni) and eh_posicao(uni) and uni in conj_uni:
        objetivos = ()
        for unidade in conj_uni:
            if unidade != uni:
                for pos_adj in posicoes_adjacentes(unidade):
                    if eh_posicao_livre(lab, conj_uni, pos_adj) and \
                       pos_adj not in objetivos:
                    # para cada posicao adjacente, verifica se e' uma posicao livre e se ainda nao foi adicionada a objetivos
                        objetivos = objetivos + (pos_adj,)
        return objetivos
    else:
        raise ValueError ('obter_objetivos: algum dos argumentos e invalido')
    
def obter_caminho(lab, conj_uni, uni):
    # obter_caminho: labirinto x conj_posicoes x posicao -> conj_posicoes    
    """
    Esta funcao recebe um labirinto, um conjunto de posicoes correspondente as
    unidades presentes no labirinto, e uma posicao correspondente a uma das
    unidades, e devolve um conjunto de posicoes (potencialmente vazio caso nao
    exista nenhuma unidade alcancavel) correspondente ao caminho de numero minimo
    de passos desde a posicao dada ate a posicao objetivo (ou seja, a posicao
    mais proxima de acordo com a ordem de leitura do labirinto que se encontra
    ao numero minimo de passos).
    """
    if eh_labirinto(lab) and eh_conj_posicoes(conj_uni) and \
       eh_mapa_valido(lab, conj_uni) and eh_posicao(uni) and uni in conj_uni:
        res = ()
        pos_visitadas = ()
        fila_exp = ((uni, ()),)
        objetivos = obter_objetivos(lab, conj_uni, uni)
        for pos_adj in posicoes_adjacentes(uni):
            if pos_adj in conj_uni:
            # verifica se a unidade ja se encontra adjacente a outra
                return res
        while len(fila_exp) > 0:
            pos_atual = fila_exp[0][0]
            caminho_atual = fila_exp[0][1]
            if pos_atual not in pos_visitadas:
            # verifica se a posicao atual ja foi visitada anteriormente
                pos_visitadas = pos_visitadas + (pos_atual,)
                # atualiza as posicoes visitadas
                caminho_atual = caminho_atual + (pos_atual,)
                # atualiza o caminho atual
                if pos_atual in objetivos:
                # verifica se a posicao atual corresponde a um objetivo
                    res = caminho_atual
                    break
                else:
                    for pos_adj in posicoes_adjacentes(pos_atual):
                        if eh_posicao_livre(lab, conj_uni, pos_adj):
                        # adiciona cada posicao adjacente e o caminho atual 'a fila de exploracao
                            fila_exp = fila_exp + ((pos_adj, caminho_atual),)
            else:
            # se ja foi visitada, remove esse elemento da fila de exploracao
                fila_exp = fila_exp[1:]
        return res
    else:
        raise ValueError ('obter_caminho: algum dos argumentos e invalido')
    
def mover_unidade(lab, conj_uni, uni):
    # mover_unidade: labirinto x conj_posicoes x posicao -> conj_posicoes
    """
    Esta funcao recebe um labirinto, um conjunto de posicoes correspondente as
    unidades presentes no labirinto, e uma posicao correspondente a uma das
    unidades, e devolve o conjunto de posicoes atualizado correspondente as
    unidades presentes no labirinto apos a unidade dada ter realizado um unico
    movimento.
    """
    if eh_labirinto(lab) and eh_conj_posicoes(conj_uni) and \
       eh_mapa_valido(lab, conj_uni) and eh_posicao(uni) and uni in conj_uni:
        caminho = obter_caminho(lab, conj_uni, uni)
        if len(caminho) == 0:
        # se o caminho for vazio, as unidades nao sao alteradas
            return conj_uni
        else:
            unidades = ()
            for unidade in conj_uni:
                if unidade == uni:
                # a unidade passa para a posicao correspondente ao primeiro elemento do caminho
                    unidades = unidades + (caminho[1],)
                else:
                # as restantes unidades nao sao alteradas
                    unidades = unidades + (unidade,)
            return unidades
    else:
        raise ValueError ('mover_unidade: algum dos argumentos e invalido')