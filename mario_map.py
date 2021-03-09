# Funciones Adicionales
def cadena_a_tupla(cadena): #Convierte una cadena a una tupla
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


# Obtener variables
# 
# dimensiones de la tabla
dimensiones= cadena_a_tupla(input("Ingresa las dimensiones de la tabla> x y: "))

# Posicion de Mario
pos_mario = cadena_a_tupla(input("Ingresa la posicion de Mario en la tabla> x y: "))

# Posiciones de Muros
pos_muros = [cadena_a_tupla(x) for x in input("Ingresa las posiciones de los muros> x1 y1, x2 y2, ... :").split(',')]

#Posicion de las tuberias
pos_tuberias = [cadena_a_tupla(x) for x in input("Ingresa las posiciones de las tuberias> x1 y1, x2 y2, ... :").split(',')]

print("dimensiones: ",dimensiones)
print("posicion de mario: ",pos_mario)
print("posiciones de los muros: ",pos_muros)
print("posiciones de las tuberias: ",pos_tuberias)