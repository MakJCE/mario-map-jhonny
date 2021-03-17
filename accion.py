class Accion:
    arriba = lambda self, posicion: (posicion[0] - 1, posicion[1])
    abajo = lambda self, posicion: (posicion[0] + 1, posicion[1])
    derecha = lambda self, posicion: (posicion[0], posicion[1] + 1)
    izquierda = lambda self, posicion: (posicion[0], posicion[1] - 1)