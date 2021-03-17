from abc import abstractproperty
from typing import Tuple
from accion import Accion
from agent import Agent
from casilla import Casilla
import queue


class Tablero:
    def __init__(self):
        self.dimensiones = (0,0)
        self.casillas = []
        self.agent = Agent()
        self.accion = Accion()
        self.pos_mario = None
        self.pos_tuberias = []
        self.restricciones_posiciones = [
            lambda posicion: posicion[0]<= self.dimensiones[0] and posicion[0] >= 0, #   Coordenadas en x validas  
            lambda posicion: posicion[1]<= self.dimensiones[1] and posicion[1] >= 0, #   Coordenadas en y validas
        ]
        self.restricciones_casillas = [
            lambda casilla: not casilla.es_muro, #                                    No es una casilla muro
            lambda casilla: not casilla.visitado, #                                   No es una casilla visitada
            lambda casilla: not casilla.es_tuberia #                                  No es una casilla tuberia
        ]

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

    def crearTableroPorParametros(self, dimension_x, dimension_y, pos_muros, pos_tuberias, pos_mario):
        # definimos propiedades utiles de la clase disminuyendo en uno, debido a la adaptacion de indices que inician en 0
        self.pos_tuberias = map(lambda posicion: (posicion[0]-1, posicion[1]-1) ,pos_tuberias)
        self.pos_mario = (pos_mario[0]-1, pos_mario[1]-1)
        self.dimensiones = (dimension_x-1, dimension_y-1)
        # Las casillas se van a formar con las dimensiones proporcionadas
        # Teniendo una lista de listas de la clase Casilla
        self.casillas = [[Casilla() for y in range(dimension_y)] for x in range(dimension_x)]
        self.ponerMurosTuberiasYMario(pos_muros, pos_tuberias, pos_mario)

    def definirPosicionesDeMurosYMario(self):
        for indice_x, fila in enumerate(self.casillas):
            for indice_y, elem in enumerate(fila):
                if elem.es_tuberia:
                    self.pos_tuberias.append((indice_x, indice_y))
                elif elem.es_mario:
                    self.pos_mario = (indice_x, indice_y)


    def crearTableroPorMapa(self, mapa):
        # Se obtinen las dimensiones
        dimension_x = len(mapa) - 1
        dimension_y = len(mapa[0]) - 1
        self.dimensiones = (dimension_x, dimension_y)
        # Se recorre la matriz de simbolos para crear la matriz de Casillas
        for fila in mapa:
            nueva_fila = []
            for elem in fila:
                # para crear nuestra matriz de Casillas aprovechamos para marcar su tipo (muro, tuberia, mario)
                casilla_aux = Casilla()
                casilla_aux.asignarTipo(elem)
                # Agregamos la casilla a la fila
                nueva_fila.append(casilla_aux)
            #Agregamos la fila a la matriz
            self.casillas.append(nueva_fila)
        self.definirPosicionesDeMurosYMario()

    def mostrarCasillas(self):
        dimension_x = self.dimensiones[0]
        dimension_y = self.dimensiones[1]
        # mostrando cabecera con indices verticales del tablero
        print('  ',end='')
        for i in range(dimension_y + 1):
            print(f'__{i + 1}_', end='')
        print()
        pos_x = 1
        # Luego se muestra el indice lateral y los valores por fila
        for fila in self.casillas:
            print(f'{pos_x} |', end='')
            for casilla in fila:
                print(f' {casilla.representacion()} |',end='')
            pos_x += 1
            print()

    # Se usa el algoritmo BFS
    
    
    def habilitarSucesores(self, sucesores):
        habilitados = []
        for sucesor in sucesores:
            if all([restriccion(sucesor) for restriccion in self.restricciones_posiciones]):
                casilla = self.casillas[sucesor[0]][sucesor[1]]
                if all([restriccion(casilla) for restriccion in self.restricciones_casillas]):
                    casilla.visitado = True
                    habilitados.append(sucesor)
        return habilitados

    def designarPadreASucesores(self, sucesores, padre):
        casilla_padre = self.casillas[padre[0]][padre[1]]
        for sucesor in sucesores:
            casilla_hijo = self.casillas[sucesor[0]][sucesor[1]]
            if casilla_hijo.valor == 0 or casilla_hijo.valor > casilla_padre.valor + 1:
                casilla_hijo.valor = casilla_padre.valor + 1
                casilla_hijo.designarPadre(padre)
    def limpiarVisitados(self):
        for fila in self.casillas:
            for casilla in fila:
                casilla.visitado = False

    def expandirSucesores(self, estado):
        acciones = [self.accion.arriba, self.accion.abajo, self.accion.derecha, self.accion.izquierda]
        sucesores = self.agent.funcion_transicion(estado, acciones)
        sucesores = self.habilitarSucesores(sucesores)
        self.designarPadreASucesores(sucesores, estado)
        return sucesores

    def busqueda_de_estados_BFS(self, estados_iniciales):
        # conjunto de colas para varios BFSs
        colas = []
        colas.extend([[estado_inicial] for estado_inicial in estados_iniciales])
        #cerrado = []
        num_expansion = 1
        while sum([len(cola) for cola in colas]) != 0:
            self.mostrarCasillas()
            print(f"Expansion numero {num_expansion}:")
            num_expansion += 1
            for cola in colas:
                if len(cola) != 0:
                    estado = cola.pop(0)
                    cola.extend(self.expandirSucesores(estado))
        self.limpiarVisitados()

    def resolver(self):
        self.busqueda_de_estados_BFS(self.pos_tuberias)

    def caminoParaMario(self ):
        # Primero añadimos la posicion de mario
        camino_nodos = []
        camino_nodos.append(self.pos_mario)
        # Definimos casilla iterable 
        #print(self.pos_mario)
        casilla_actual = self.casillas[self.pos_mario[0]][self.pos_mario[1]]
        num_saltos_requeridos = casilla_actual.valor
        # Recorremos el camino
        while(casilla_actual.padre != None):
            camino_nodos.append(casilla_actual.padre)
            casilla_actual = self.casillas[casilla_actual.padre[0]][casilla_actual.padre[1]]
        # retornamos solucion
        return (num_saltos_requeridos, camino_nodos)

    def mostrarCaminoMario(self):
        num_saltos, camino_nodos = self.caminoParaMario()
        print(f"Mario necesita {num_saltos} pasos para llegar a la tuberia mas cercana")
        print(f"A traves de las siguientes posiciones de casillas\
        {' -> '.join([repr((posicion[0] + 1, posicion[1] + 1)) for posicion in camino_nodos])}")
