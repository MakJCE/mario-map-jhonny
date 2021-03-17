from accion import Accion
from tablero import Tablero
from casilla import Casilla
import numpy
from sys import stdin

tablero = Tablero()

# Funciones Adicionales
def cadenaTupla(cadena): #Convierte una cadena a una tupla
    retorno = (0,0)
    try:
        retorno = tuple([int(x) for x in cadena.split()])
    except ValueError:
        print("los parametros ingresados no corresponden al tipo de formato: numero")
        exit()
    except:
        print("ha ocurrido un error")
        exit()
    return retorno

def crearTableroPorParametros():
    # Obtenemos:
    # Dimensiones de la tabla
    dimensiones= cadenaTupla(input("Ingresa las dimensiones de la tabla> x y: "))
    # Posicion de Mario
    pos_mario = cadenaTupla(input("Ingresa la posicion de Mario en la tabla> x y: "))
    # Posiciones de Muros
    pos_muros = [cadenaTupla(x) for x in input("Ingresa las posiciones de los muros> x1 y1, x2 y2, ... :").split(',')]
    # Posicion de las tuberias
    pos_tuberias = [cadenaTupla(x) for x in input("Ingresa las posiciones de las tuberias> x1 y1, x2 y2, ... :").split(',')]
    # Se crea el tablero
    tablero.crearTableroPorParametros(dimensiones[0], dimensiones[1], pos_muros, pos_tuberias, pos_mario)

def crearTableroPorMapa():
    # Extraemos la simbologia de los tipos de casillas
    simbologia = Casilla().simbologia
    print(f' La simbologia de los elementos es la siguiente: {" ".join([f" {simbolo} para {nombre}," for nombre, simbolo in simbologia.items()])}')
    print("Ingrese fila por fila separados por un espacio los elementos del tablero. Para terminar ingrese un punto despues de la ultima linea")
    tablero_ingreso = []
    # Ingresamos en una lista las lineas del tablero como listas creando una matriz de simbolos
    for linea in stdin:
        if linea == ".\n":
            break
        tablero_ingreso.append([num for num in linea.split()])
    # Se crea el tablero
    tablero.crearTableroPorMapa(tablero_ingreso)

###---------------------- Inicio ------------------- ###

print("MENU\n1)Crear tablero a partir de parametros\n2)Crear tablero ingresandolo.")
opcion = int(input("Ingrese el numero de la opcion que guste: "))
if opcion == 1:
    crearTableroPorParametros()
elif opcion == 2:
    crearTableroPorMapa()

tablero.resolver()
tablero.mostrarCasillas()
tablero.mostrarCaminoMario()