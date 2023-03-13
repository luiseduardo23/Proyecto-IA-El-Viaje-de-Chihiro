class Arbol:
    def __init__(self,ide, elemento, costoA, listaM, cantMA, padre):
        self.ide= ide
        self.hijos = []
        self.padre = padre
        self.elemento = elemento
        self.costoA = costoA #Costo Acumulado
        self.listaM = listaM #Lista de posiciones de monedas recogidas
        self.cantMA = cantMA #Cantidad de Monedas Actuales

    def buscarSubarbol(arbol, idePadre):
        if (arbol.ide == idePadre):
            return arbol
        for subarbol in arbol.hijos:
            a= Arbol.buscarSubarbol(subarbol, idePadre)
            if(a!=None):
                return a

    def agregarElemento(ide, elemento, costo , padre, listaM, cantMA):
        padre.hijos.append(Arbol(ide, elemento, costo, listaM, cantMA, padre))

#Código fuente utilizado de:
#https://sites.google.com/site/programacioniiuno/temario/unidad-5---grafos/rboles
