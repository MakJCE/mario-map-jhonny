class Casilla:
    es_muro = False
    es_tuberia = False
    es_mario = False
    visitado = False
    padre = None
    simbologia = {"Mario":'M', "Tuberia":'T', "Muro":"W", "Casilla": "C"}
    valor = 0
    def representacion(self):
        if self.es_muro:
            return(self.simbologia.get("Muro"))
        elif self.es_tuberia:
            return(self.simbologia.get("Tuberia"))
        elif self.es_mario:
            return (self.simbologia.get("Mario"))
        else:
            return(f'{self.valor}')
    def asignarTipo(self, simbolo):
        if simbolo == self.simbologia.get("Muro"):
            self.es_muro = True
        elif simbolo == self.simbologia.get("Mario"):
            self.es_mario = True
        elif simbolo == self.simbologia.get("Tuberia"):
            self.es_tuberia = True
    def designarPadre(self, padre):
        self.padre = padre

