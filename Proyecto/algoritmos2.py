from arbol import *

def porCosto2(matriz, xi, yi):
    NoMeta = True
    listaXYCostos =[]
    matriz[xi][yi]=0
    nn=0 #numero de nodos
    arbol = Arbol(nn,[xi,yi],0,[],0, None) #Se crea el arbol con la posición inicial, el costo acumulado, listado de posiciones de monedas obtenidas y numero de monedas actuales
    target = arbol #Apuntador para indicarnos el nodo de menor costo Actual

    while(NoMeta):
        if(matriz[target.elemento[0]][target.elemento[1]]!=3): #Verificamos si No es meta
            #Expandimos los nodos y calculamos costos
            x= target.elemento[0]+1
            y=target.elemento[1]
            if(x<3):
                if(matriz[x][y]==0 or matriz[x][y]==3):
                    nn+=1
                    Arbol.agregarElemento(nn, [x,y], target.costoA+1, target, target.listaM.copy(), target.cantMA)
                    listaXYCostos.append([nn,target.costoA+1])
                    
                if(matriz[x][y]==4):
                    boolean = True
                    for pos in target.listaM:
                        if (pos[0]==x and pos[1]==y):
                            nn+=1
                            Arbol.agregarElemento(nn, [x,y], target.costoA+1, target, target.listaM.copy(), target.cantMA)
                            listaXYCostos.append([nn,target.costoA+1])
                            boolean = False
                    if(boolean):
                        nn+=1
                        Arbol.agregarElemento(nn, [x,y], target.costoA+2, target, (target.listaM.copy()+[[x,y]]), target.cantMA+1)
                        listaXYCostos.append([nn,target.costoA+2])
                            
                if(matriz[x][y]==5):
                    if (target.cantMA>=1):
                        if(target.costoA>=3):
                            nn+=1
                            Arbol.agregarElemento(nn, [x,y], target.costoA-3, target, target.listaM.copy(), 0)
                            listaXYCostos.append([nn,target.costoA-3])
                        else:
                            nn+=1
                            Arbol.agregarElemento(nn,[x,y], 0, target, target.listaM.copy(),0)
                            listaXYCostos.append([nn,0])
                    else:
                        nn+=1
                        Arbol.agregarElemento( nn, [x,y], target.costoA+2, target, target.listaM.copy(), 0)
                        listaXYCostos.append([nn,target.costoA+2])

            x = target.elemento[0]-1
            if(x>=0):        
                if(matriz[x][y]==0 or matriz[x][y]==3):
                    nn+=1
                    Arbol.agregarElemento(nn, [x,y], target.costoA+1,target, target.listaM.copy(), target.cantMA)
                    listaXYCostos.append([nn,target.costoA+1])

                if(matriz[x][y]==4):
                    boolean = True
                    for pos in target.listaM:
                        if (pos[0]==x and pos[1]==y):
                            nn+=1
                            Arbol.agregarElemento(nn, [x,y], target.costoA+1, target, target.listaM.copy(),target.cantMA)
                            listaXYCostos.append([nn,target.costoA+1])
                            boolean = False
                    if(boolean):
                        nn+=1
                        Arbol.agregarElemento(nn,  [x,y], target.costoA+2, target, (target.listaM.copy()+[[x,y]]), target.cantMA+1)
                        listaXYCostos.append([nn,target.costoA+2])

                if(matriz[x][y]==5):
                    if (target.cantMA>=1):
                        if(target.costoA>=3):
                            nn+=1
                            Arbol.agregarElemento(nn, [x,y], target.costoA-3, target, target.listaM.copy(), 0)
                            listaXYCostos.append([nn,target.costoA-3])
                        else:
                            nn+=1
                            Arbol.agregarElemento(nn, [x,y], 0, target, target.listaM.copy(),0)
                            listaXYCostos.append([nn,0])
                    else:
                        nn+=1
                        Arbol.agregarElemento(nn, [x,y], target.costoA+2,target, target.listaM.copy(), 0)
                        listaXYCostos.append([nn,target.costoA+2])
            x= target.elemento[0]
            y=target.elemento[1] +1
            if(y<len(matriz[0])):

                if(matriz[x][y]==0 or matriz[x][y]==3):
                    nn+=1
                    Arbol.agregarElemento(nn, [x, y], target.costoA+1, target, target.listaM.copy(), target.cantMA)
                    listaXYCostos.append([nn,target.costoA+1])

                if(matriz[x][y]==4):
                    boolean = True
                    for pos in target.listaM:
                        if (pos[0]==x and pos[1]==y):
                            nn+=1
                            Arbol.agregarElemento(nn, [x,y], target.costoA+1, target, target.listaM.copy(), target.cantMA)
                            listaXYCostos.append([nn,target.costoA+1])
                            boolean = False
                    if(boolean):
                        nn+=1
                        Arbol.agregarElemento(nn, [x,y], target.costoA+2, target, (target.listaM.copy()+[[x,y]]), target.cantMA+1)
                        listaXYCostos.append([nn,target.costoA+2])

                if(matriz[x][y]==5):
                    if (target.cantMA>=1):
                        if(target.costoA>=3):
                            nn+=1
                            Arbol.agregarElemento(nn, [x,y], target.costoA-3, target, target.listaM.copy(), 0)
                            listaXYCostos.append([nn,target.costoA-3])
                        else:
                            nn+=1
                            Arbol.agregarElemento(nn, [x,y], 0, target, target.listaM.copy(),0)
                            listaXYCostos.append([nn,0])
                    else:
                        nn+=1
                        Arbol.agregarElemento(nn, [x,y], target.costoA+2, target, target.listaM.copy(), 0)
                        listaXYCostos.append([nn,target.costoA+2])
            y=target.elemento[1] -1              
            if (y >= 0):
               
                if(matriz[x][y]==0 or matriz[x][y]==3):
                    nn+=1
                    Arbol.agregarElemento(nn, [x,y], target.costoA+1, target, target.listaM.copy(), target.cantMA)
                    listaXYCostos.append([nn,target.costoA+1])

                if(matriz[x][y]==4):
                    boolean = True
                    for pos in target.listaM:
                        if (pos[0]==x and pos[1]==y):
                            nn+=1
                            Arbol.agregarElemento(nn, [x,y], target.costoA+1, target, target.listaM.copy(), target.cantMA)
                            listaXYCostos.append([nn,target.costoA+1])
                            boolean = False
                    if(boolean):
                        nn+=1
                        Arbol.agregarElemento(nn, [x,y], target.costoA+2, target, (target.listaM.copy()+[[x,y]]), target.cantMA+1)
                        listaXYCostos.append([nn,target.costoA+2])

                if(matriz[x, y]==5):
                    if (target.cantMA>=1):
                        if(target.costoA>=3):
                            nn+=1
                            Arbol.agregarElemento(nn, [x,y], target.costoA-3, target, target.listaM.copy(), 0)
                            listaXYCostos.append([nn,target.costoA-3])
                        else:
                            nn+=1
                            Arbol.agregarElemento(nn, [x,y], 0, target, target.listaM.copy(), target.costoA,0)
                            listaXYCostos.append([nn,0])
                    else:
                        nn+=1
                        Arbol.agregarElemento(nn,[x,y], target.costoA+2, target, target.listaM.copy(), 0)
                        listaXYCostos.append([nn,target.costoA+2])
                
            #Escogenmos el nodo de menor costo:
            minimo = listaXYCostos.pop(minimoL(listaXYCostos))
            target = Arbol.buscarSubarbol(arbol, minimo[0])
        else:
            NoMeta= False
    pila =[]
    res =[]
    #creamos la lista del recorrido hasta la meta
    while(target.padre != None):
        pila.append([target.elemento[0],target.elemento[1]])
        target = target.padre
    pila.append([xi,yi])

    while pila:
        res.append(pila.pop())
    print(nn)
    return res
        
def minimoL(lista):
    L0=lista[0][1]
    p=0
    L=1
    for L in range(0,len(lista)):
        if(int(lista[L][1])<int(L0)):
            L0= lista[L][1]
            p=L
    return p
