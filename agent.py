from accion import Accion

class Agent:
    def funcion_transicion(self, estado, acciones):
        sucesores = [] 
        for accion in acciones:
            sucesor = accion(estado)
            sucesores.append(sucesor)
        return sucesores