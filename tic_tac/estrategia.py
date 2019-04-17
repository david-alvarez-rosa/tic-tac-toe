"""
Estrategia general, importa estrategia básica.
"""


import cfg
from equivalencias import *
from basic import moveBasic


def actualiza(i, j):
    """
    Actualiza el tablero que ve el jugador y el resto de variables internas
    (como el tablero que ve la máquina).
    """
    cfg.board[i][j] = 0
    if cfg.eb == True:
        return

    # Si es el primer movimiento se detecta la rama inicial.
    if cfg.nodo == -1:
        for i in range(3):
            posSig = cfg.ramas[i][0]

            cfg.boardInt[posSig[0]][posSig[1]] = 0
            sim = equivalente(cfg.boardInt, cfg.board)
            if sim != -2:
                cfg.sims.append(sim)
                cfg.rama = i
                cfg.nodo = 0
                return
            cfg.boardInt[posSig[0]][posSig[1]] = -3

    # A partir del segundo movimiento detectamos el nodo.
    for pos in range(len(cfg.conex[cfg.rama][cfg.nodo])):
        nodoSig = cfg.conex[cfg.rama][cfg.nodo][pos]
        posSig = cfg.ramas[cfg.rama][nodoSig]

        if (posSig == "EB"):
            cfg.eb = True
            return

        cfg.boardInt[posSig[0]][posSig[1]] = 0
        sim = equivalente(simetriaMultiple(cfg.board, cfg.sims), cfg.boardInt)

        if sim != -2:
            cfg.sims.append(sim)
            cfg.nodo = nodoSig
            return
        cfg.boardInt[posSig[0]][posSig[1]] = -3


def move():
    """
    Decide el siguiente movimiento a realizar.
    """
    if cfg.eb == True:
        moveBasic(cfg.board)
        return

    if len(cfg.conex[cfg.rama][cfg.nodo]) > 1:
        print("Error de longitud")

    cfg.nodo = cfg.conex[cfg.rama][cfg.nodo][0]
    move = cfg.ramas[cfg.rama][cfg.nodo]

    if move == "EB":
        cfg.eb = True
        moveBasic(cfg.board)
        return

    cfg.boardInt[move[0]][move[1]] = 1
    cfg.board = simetriaMultipleInversa(cfg.boardInt, cfg.sims)
    return