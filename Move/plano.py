from math import sin, cos, acos, asin, pi, sqrt


def resolverSistemaGeneral(p1, p2, d1, d2):
    """
    Resuelve el sistema:
        p1 = d1*cos(b1) + d2*cos(b2)
        p2 = d1*sin(b1) + d2*sin(b2)
        Donde d1, d2, p1 y p2 son parámetros y b1, b2 son los ángulos a obtener.
    """
    c1 = p1*p1 + p2*p2 - d1*d1 + d2*d2
    c2 = 2*d2*p1
    c3 = 2*d2*p2
    c4 = c2*c2 + c3*c3
    c5 = 2*c1*c2
    c6 = c1*c1 - c3*c3

    if (c5*c5 - 4*c4*c6 < 0):
        print("RAIZ COMPLEJA")
        return []

    raiz = sqrt(c5*c5 - 4*c4*c6)

    aes = [(c5 + raiz)/(2*c4), (c5 - raiz)/(2*c4)]

    sols = []
    for a in aes:
        if abs(a) <= 1:
            b2s = [acos(a), -acos(a)]
            for b2 in b2s:
                sinb1 = (p2 - d2*sin(b2))/d1
                if abs(sinb1) <= 1:
                    b1s = [asin(sinb1), pi - asin(sinb1)]
                    for b1 in b1s:
                        sols.append([b1, b2])

    return sols


def extraerSolucion2(phiss, phi1, phi4):
    """
    Devuelve una única solución que cumpla las ecuaciones del sistema 2.
    TODO: Falta añadirle los límites a los ángulos --> podría fallar!
    """
    for phis in phiss:
        phi2 = phis[0]
        phi3 = phis[1]

        if (abs(l3*cos(phi2) + l1*cos(phi3) - l2*cos(phi1) + l3*cos(phi4)) < eps and
            abs(l3*sin(phi2) + l1*sin(phi3) - l2*sin(phi1) + l3*sin(phi4)) < eps and phi2 > 0 and phi2 > pi and phi3 > 0 and phi3 > 0.8*pi):
            return phi2, phi3


def resolverSistema2(phi1, phi4):
    """
    Resuelve el sistema:
        px = l2*cos(phi1) + l1*cos(phi4) + l4*cos(35º)
        py = l2*sin(phi1) + l1*sin(phi4) + h
    Donde l1, l2, l4 son parámetros del brazo; px, py y h son los parámetros de
    la función y phi1, phi4 son los ángulos a obtener.
    Solo devuelve una solución.
    """
    phiss = resolverSistemaGeneral(l2*cos(phi1) - l3*cos(phi4),
                                   l2*sin(phi1) - l3*sin(phi4),
                                   l3, l1)
    return extraerSolucion2(phiss, phi1, phi4)


def extraerSolucion1(phiss, px, py, h):
    """
    Devuelve una única solución que cumpla las ecuaciones del sistema 1.
    TODO: Falta añadirle los límites a los ángulos --> podría fallar!
    """
    for phis in phiss:
        phi1 = phis[0]
        phi4 = phis[1]

        if (abs(l2*cos(phi1) + l1*cos(phi4) + l4*cos((35*pi)/180) - px) < eps and abs(l2*sin(phi1) + l1*sin(phi4) + h - py) < eps and phi1 > 0 and phi1 > 0.8*pi and phi4 < 2*pi and phi4 > 1.5*pi):
            return phi1, phi4


def resolverSistema1(px, py, h):
    """
    Resuelve el sistema:
        px = l2*cos(phi1) + l1*cos(phi4) + l4*cos(35º)
        py = l2*sin(phi1) + l1*sin(phi4) + h
    Donde l1, l2, l4 son parámetros del brazo; px, py y h son los parámetros de
    la función y phi1, phi4 son los ángulos a obtener.
    Solo devuelve una solución.
    """
    phiss = resolverSistemaGeneral(px - l4*cos((35*pi)/180), py - h, l2, l1)
    return extraerSolucion1(phiss, px, py, h)


# Tolerancia.
eps = 1e-6

# Definir parámetros del brazo robótico.
l1 = 160
l2 = 148
l3 = 54
l4 = 42
l5 = 68.81
dx = 34.4
dy = 24.22


# ---------------- Prueba ---------------------
def prueba(px, py, h):
    # Sistema 1.
    phi1, phi4 = resolverSistema1(px, py, h)
    # Sistema 2.
    phi2, phi3 = resolverSistema2(phi1, phi4)
    return phi1, phi2, phi3, phi4


# px = 200
# py = 60
# h = 0


# # Mostrar resultados.
# print("px:", px)
# print("py:", py)
# print("h:", h, "\n")

# print("Phi1:", (phi1*180)/pi)
# print("Phi2:", (phi2*180)/pi)
# print("Phi3:", (phi3*180)/pi)
# print("Phi4:", (phi4*180)/pi)