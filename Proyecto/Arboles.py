class Arboles:
    def __init__(self):
        self.Arriba= None
        self.Derecha= None
        self.Abajo=None
        self.CostoG= None
        self.CostoH=None
        self.Padre=None
        self.PosX=None
        self.PosY=None
        self.monedas=0

    def costoF(self):
        return self.CostoG+self.CostoH