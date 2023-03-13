#A*
#Set de abiertos(arbol)
#Set  de cerrados(lista ya revisados)
#añada nodo incial a los abiertos
#loop
#nodoActual= nodo en abiertos con el menor costo F
#remueva a nodoActual de abiertos y añadalo a cerrados
#si nodoActual es nodo objetivo (romper ciclo)

#por cada vecino del nodo actual
#si el vecino es un obstaculo o esta en el set de cerrados -> pase al siguiente vecino
#si el camino al vecino es el mas corto o si el vecino no esta en el set de abiertos
    #setear costo F del vecino
    #setear a nodoActual como nodoPadre del vecino 
    #si vecino no esta en abiertos
        #añadir vecino a abiertos

from Arboles import *
import numpy as np
import math

#Interpretación de las matrices
# 0:Espacio en blanco
# 1:Bloque
# 2: Chihiro
# 3: Haku
# 4: Moneda
# 5: Sin rostro


#Distancia entre 2 puntos
def distancia(X1,Y1,X2,Y2):
    d=pow((X2-X1),2)+pow((Y2-Y1),2)
    return math.sqrt(d)

###Autor: Michael Palacios Gaviria
###Recibe un tablero de jeugo,y devuelve la lista de posiciones de la mejor ruta usando A*
def asterisco(Tablero):
    Arbol= Arboles()
    abiertos=[]
    visitados=[]
    monedasRecogidas=0
    posXActual=0
    posYActual=0
    posXMeta=0
    posYMeta=0
    Arbol= Arboles()
    Arbol.CostoG= 0
    tamanioTablero=int(Tablero.size/3)

    #Capturamos posiciones iniciales y finales 
    for fila in range(3):
        for columna in range(tamanioTablero):
            if Tablero[fila][columna]==2:#chihiro
                posXActual=fila
                posYActual=columna
                Arbol.PosX=fila
                Arbol.PosY=columna
            elif Tablero[fila][columna]==3:#haku
                posXMeta=fila
                posYMeta=columna            
    Arbol.CostoH=distancia(posXActual,posYActual,posXMeta,posYMeta)
    
    while(esMeta(posXActual,posYActual,posXMeta,posYMeta)):
        #Derecha
        tentativaMovimiento=posYActual+1
        if(tentativaMovimiento<tamanioTablero):#evitar desborde por la derecha
            if(Tablero[posXActual][tentativaMovimiento]!=1):#obstaculo
                Arbol.Derecha=Arboles()
                pesoNuevo=1
                if(Tablero[posXActual][tentativaMovimiento]==4):#Moneda
                    pesoNuevo=2 
                elif(Tablero[posXActual][tentativaMovimiento]==5):#Sin Rostro
                    pesoNuevo=2-(5*Arbol.monedas)
                    #print("Peso en el sin rostro"+str(pesoNuevo))
                Arbol.Derecha.CostoG=Arbol.CostoG+pesoNuevo
                Arbol.Derecha.CostoH=distancia(posXActual,posYActual+1,posXMeta,posYMeta)
                Arbol.Derecha.PosX=posXActual
                Arbol.Derecha.PosY=posYActual+1
                Arbol.Derecha.Padre=Arbol    
        #Arriba
        tentativaMovimiento=posXActual-1
        if(tentativaMovimiento>=0):#evitar desborde por arriba
            if(Tablero[tentativaMovimiento][posYActual]!=1):#obstaculo
                Arbol.Arriba=Arboles()
                pesoNuevo=1
                if(Tablero[tentativaMovimiento][posYActual]==4):#Moneda
                    pesoNuevo=2 
                elif(Tablero[tentativaMovimiento][posYActual]==5):#Sin Rostro
                    pesoNuevo=2-(5*Arbol.monedas)
                    #print("Peso en el sin rostro"+str(pesoNuevo))
                Arbol.Arriba.CostoG=Arbol.CostoG+pesoNuevo
                Arbol.Arriba.CostoH=distancia(posXActual-1,posYActual,posXMeta,posYMeta)
                Arbol.Arriba.PosX=posXActual-1
                Arbol.Arriba.PosY=posYActual
                Arbol.Arriba.Padre=Arbol

        #Abajo
        tentativaMovimiento=posXActual+1
        if(tentativaMovimiento<3):#evitar desborde por abajo
            if(Tablero[tentativaMovimiento][posYActual]!=1):#obstaculo
                Arbol.Abajo=Arboles()
                pesoNuevo=1
                if(Tablero[tentativaMovimiento][posYActual]==4):#Moneda
                    pesoNuevo=2 
                elif(Tablero[tentativaMovimiento][posYActual]==5):#Sin Rostro
                    pesoNuevo=2-(5*Arbol.monedas)
                    #print("Peso en el sin rostro"+str(pesoNuevo))
                Arbol.Abajo.CostoG=Arbol.CostoG+pesoNuevo
                Arbol.Abajo.CostoH=distancia(posXActual+1,posYActual,posXMeta,posYMeta)
                Arbol.Abajo.PosX=posXActual+1
                Arbol.Abajo.PosY=posYActual
                Arbol.Abajo.Padre=Arbol

        #Escoger Mejor Movimiento

        if Arbol.Abajo is not None:
            abiertos.append(Arbol.Abajo)
        if Arbol.Derecha is not None:
            abiertos.append(Arbol.Derecha)
        if Arbol.Arriba is not None:
            abiertos.append(Arbol.Arriba)
        seleccion=-1
        numero=2000

        for pos in range(len(abiertos)):
            if (abiertos[pos].costoF()<numero):
                numero=abiertos[pos].costoF()
                seleccion=pos

        Arbol=abiertos[seleccion]
        visitados.append(abiertos[seleccion])
        if(Tablero[abiertos[seleccion].PosX][abiertos[seleccion].PosY]==4):#Moneda
            if(Arbol.Padre is not None):
                Arbol.monedas=Arbol.Padre.monedas+1
                #print("moneda recogida"+str(Arbol.monedas))
            else:
                Arbol.monedas=1
        elif(Tablero[abiertos[seleccion].PosX][abiertos[seleccion].PosY]==5):#Sin Rostro
            Arbol.monedas=0
        posXActual=abiertos[seleccion].PosX
        posYActual=abiertos[seleccion].PosY
        abiertos.pop(seleccion)
        #print("Posicion Actual:"+str(posXActual)+","+str(posYActual)+" Meta:"+str(posXMeta)+","+str(posYMeta))
        #fin del ciclo
    
    
    A=[]
    B=[]
    A.append(posXMeta)
    B.append(posYMeta)
    costoTotal=Arbol.CostoG
    print(str(costoTotal))
    while(Arbol.Padre is not None):
        #reportar posiciones 
        #print("Pos X "+str(Arbol.Padre.PosX)+" Pos Y "+str(Arbol.Padre.PosY))
        A.append(Arbol.Padre.PosX)
        B.append(Arbol.Padre.PosY)
        Arbol=Arbol.Padre
    A.reverse()
    B.reverse()
    Respuesta=np.zeros((len(A),2))
    for fila in range(len(A)):
        Respuesta[fila][0]=A[fila]
        Respuesta[fila][1]=B[fila]
    return Respuesta
            

def esMeta(x1,y1,x2,y2):
    return ((x1-x2)+(y1-y2))!=0

def main():
    m= np.zeros((3,20))
    m[1][0]=2
    m[1][19]=3

    #Obstaculos
    m[1][1]=1
    m[0][1]=1
    m[1][2]=1
    m[2][4]=1
    m[1][4]=1
    m[1][5]=1
    m[1][6]=1
    m[1][8]=1
    m[2][8]=1
    m[1][9]=1

    #Moneda

    #print(m)
    #print(asterisco(m))

#main()



