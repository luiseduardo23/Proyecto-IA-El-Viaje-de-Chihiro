import numpy as np
from arbol import *

# 0:Espacio en blanco
# 1:Bloque
# 2: Chihiro
# 3: Haku
# 4: Moneda
# 5: Sin rostro

#Variables:
monedas=0
i_size=0
j_size=0
i=0
j=0
estadoIniciali = 0
estadoInicialj = 0
#________________________________

#obteniendo dimensiones del ambiente:
archivo = open("ejemplo.txt")
linea = archivo.readline()
for letra in linea:
    j_size += 1
    
j_size -= 1 #Le restamos el salto de linea
    
while linea:
    i_size+=1
    linea= archivo.readline()
archivo.seek(0)

#guardando el ambiente en un arreglo___________
ambiente = np.zeros((i_size,j_size))

while True:
    linea = archivo.readline()
    linea = linea.rstrip('\n')
    for letra in linea:
        if(int(letra)==2):
            estadoIniciali= i
            estadoInicialj= j
        ambiente[i][j] = int(letra)
        j+= 1
    if (i==i_size-1):
        break;
    else:
        i+=1
        j=0
print (ambiente)

#_____________________________________________

def preferenteAmplitud():
    return none
