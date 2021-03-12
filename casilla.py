class Casilla:
    es_muro = False
    es_tuberia = False
    es_mario = False
    valor = 0
    def representacion(self):
        if self.es_muro:
            return('W')
        elif self.es_tuberia:
            return('T')
        elif self.es_mario:
            return 'M'
        else:
            return(f'{self.valor}')