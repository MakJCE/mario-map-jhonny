from typing import Tuple


from casilla import Casilla
class Tablero:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y
        # Las casillas se van a formar con las dimensiones proporcionadas
        # Teniendo una lista de listas de la clase Casilla
        self.casillas = [[Casilla() for y in range(self.y)] for x in range(self.x)]

    def ponerMurosTuberiasYMario(self, pos_muros, pos_tuberias, pos_mario):
        pos_x = 1
        for fila in self.casillas:
            pos_y = 1
            for casilla in fila:
                if (pos_x, pos_y) in pos_muros:
                    casilla.es_muro=True
                if (pos_x, pos_y) in pos_tuberias:
                    casilla.es_tuberia=True
                if (pos_x, pos_y) == pos_mario:
                    casilla.es_mario=True
                pos_y += 1
            pos_x += 1

    def mostrarCasillas(self):
        # mostrando cabecera con indices verticales del tablero
        print('  ',end='')
        for i in range(1, 1 + self.y):
            print(f'__{i}_', end='')
        print()
        pos_x = 1
        # Luego se muestra el indice lateral y los valores por fila
        for fila in self.casillas:
            print(f'{pos_x} |', end='')
            for casilla in fila:
                print(f' {casilla.representacion()} |',end='')
            pos_x += 1
            print()

    # Se usa el algoritmo ...
    def resolver():
        pass

    def busqueda_de_estados(estado, estado_objetivo, acciones):
        pass