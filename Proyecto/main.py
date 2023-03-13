from tkinter import *
from PIL import Image,ImageTk
import numpy as np
from threading import *
from algoritmos import *
from algoritmos2 import *
from Aasterisco import *
from ctypes import *
import time

#Interpretación de las matrices
# 0:Espacio en blanco
# 1:Bloque
# 2: Chihiro
# 3: Haku
# 4: Moneda
# 5: Sin rostro

#Variables:
monedas=0
monedasVar = None
costoA = 0
costoVar = None
i_size=0
j_size=0
i=0
j=0
estadoIniciali = 0
estadoInicialj = 0
btonlista =[]
matriz = None

#________________________________
def insertarImagen(boton, valor):
    if(valor==0):
        boton.config(image=vacio)
    if(valor==1):
        boton.config(image=bloque)
    if(valor==2):
        boton.config(image=chihiro)
    if(valor==3):
        boton.config(image=haku)
    if(valor==4):
        boton.config(image=moneda)
    if(valor==5):
        boton.config(image=kaonashi)
#_____________________________________________________________________________________________________________________________
def crearBotones(matriz):
    global i_size
    global j_size
    global btonlista
    global monedas 
    global costoA
    
    monedas=0
    monedasVar.set(monedas)
    costoA = 0
    costoVar.set(costoA)

    btonlista =[]
    
    for fil in range(i_size):
        btonlista.append([]) #creando la fila
        for col in range(j_size):
            btonlista[fil].append(Button(f1))
            btonlista[fil][col].config(bg="#97DFFF", borderwidth=1, relief= "solid")
            insertarImagen(btonlista[fil][col], matriz[fil][col])
            btonlista[fil][col].place(relx= (1/j_size)*col, rely=0.333333333*fil, relwidth= 1/j_size, relheight =1/i_size)

    b2["state"] = "normal"
    b3["state"] = "normal"
    b4["state"] = "normal"

#_____________________________________________________________________________________________________________________________
def crearHilo(f):
    global monedas 
    global costoA
    monedas=0
    costoA=0
    b1["state"] = "disabled"
    b2["state"] = "disabled"
    b3["state"] = "disabled"
    b4["state"] = "disabled"
    Thread(target = f).start() 
#__________________________________________________________
def algPorCosto():
    global matriz
    global estadoIniciali
    global estadoInicialj

    res = porCosto(matriz,estadoIniciali, estadoInicialj)
    aplicarLista(res,1)
    b1["state"] = "normal"
#__________________________________________________________
def algPorCosto2():
    global matriz
    global estadoIniciali
    global estadoInicialj
    res = porCosto2(matriz,estadoIniciali, estadoInicialj)
    aplicarLista(res,1)
    b1["state"] = "normal"
#__________________________________________________________
def algAAsterisco():
    global matriz
    res = asterisco(matriz)
    aplicarLista(res,1)
    b1["state"] = "normal"
#__________________________________________________________
def obtenerArchivo(nombre):
    #Declaro variables globales fuera de este ambiente:
    global j_size
    global i_size
    global i
    global j
    global estadoIniciali
    global estadoInicialj
    global matriz

    i_size=0
    j_size=0
    i=0
    j=0
    estadoIniciali = 0
    estadoInicialj = 0
    
    #obteniendo dimensiones del ambiente:
    archivo = open(nombre)
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
    matriz = ambiente
    crearBotones(ambiente)
#______________________________________________________________________________
def aplicarLista(listaRecorridos, x):
    global estadoIniciali
    global estadoInicialj
    global btonlista
    global costoA
    global monedas
    global monedasVar
    global costoVar
    global matriz
    
    if(x<len(listaRecorridos)):
        if(matriz[estadoIniciali][estadoInicialj]==5):
            insertarImagen(btonlista[estadoIniciali][estadoInicialj],5)
        else:
            insertarImagen(btonlista[estadoIniciali][estadoInicialj],0)
                
        estadoIniciali = int(listaRecorridos[x][0])
        estadoInicialj = int(listaRecorridos[x][1])
        if(matriz[estadoIniciali][estadoInicialj]==4):
            monedas+=1
            monedasVar.set(monedas)
            costoA += 2
            costoVar.set(costoA)
        elif(matriz[estadoIniciali][estadoInicialj]==5):
            if(monedas!=0):
                if(costoA>=3):
                    costoA = costoA-3
                    costoVar.set(costoA)
                else:
                    costoA = 0
                    costoVar.set(costoA)
            else:
                costoA = costoA+2
                costoVar.set(costoA)
            monedas=0
            monedasVar.set(monedas)
        else:
            costoA += 1
            costoVar.set(costoA)
            
        insertarImagen(btonlista[estadoIniciali][estadoInicialj],2)
        time.sleep(1)
        raiz.update_idletasks()
        aplicarLista(listaRecorridos, x+1) 
#_______________________________________________________________________________
        
#ventana Raiz
raiz = Tk()
raiz.title("Proyecto")
raiz.resizable(1,0)
raiz.geometry("1000x450")

#Imagenes
vacio = Image.open('null.png')
vacio = vacio.resize((100, 100), Image.ANTIALIAS) # Redimension (Alto, Ancho)
bloque = Image.open('bloque.jpg')
bloque = bloque.resize((100, 100), Image.ANTIALIAS) # Redimension (Alto, Ancho)
chihiro = Image.open('chihiro.jpg')
chihiro = chihiro.resize((70, 70), Image.ANTIALIAS) 
haku = Image.open('haku.jpg')
haku = haku.resize((70, 70), Image.ANTIALIAS)
moneda = Image.open('moneda.png')
moneda = moneda.resize((60,60), Image.ANTIALIAS)
kaonashi = Image.open('kaonashi.png')
kaonashi = kaonashi.resize((70, 70), Image.ANTIALIAS)

vacio = ImageTk.PhotoImage(vacio)
bloque = ImageTk.PhotoImage(bloque)
chihiro = ImageTk.PhotoImage(chihiro)
haku = ImageTk.PhotoImage(haku)
moneda = ImageTk.PhotoImage(moneda)
kaonashi = ImageTk.PhotoImage(kaonashi)

#Lineas
canvas = Canvas(width=1000, height=450, bg= '#E4B2F0')
canvas.pack(expand=YES, fill=BOTH)
canvas.create_line(30, 130, 620, 130,width=3, fill='white')
canvas.create_line(30, 180, 620, 180,width=3, fill='white')
canvas.create_line(640,20 , 640, 180,width=3, fill='white')

#frame
f1= Frame(raiz)
f1.config(bg="#E4B2F0")
f1.place(relx=0.05, rely=0.1, relheight= 0.47, relwidth=0.9)
f1.place(x=0,y=150)

#Etiquetas
etiqueta1 = Label(text = "Ingresa la ruta absoluta o relativa del \narchivo a cargar (incluyendo la extensión .txt)",bg= "#E4B2F0", font = ("Verdana", 12, "bold italic")).place(x=30, y=10)

monedasVar = IntVar()
monedasVar.set(monedas)
Label(textvariable= monedasVar ,bg= "#E4B2F0", font = ("Verdana", 14, "bold italic")).place(x=200, y=140)
Label(text = "Monedas: " ,bg= "#E4B2F0", font = ("Verdana", 14, "italic")).place(x=70, y=140)

costoVar = StringVar()
costoVar.set(costoA)
Label(textvariable= costoVar ,bg= "#E4B2F0", font = ("Verdana", 14, "bold italic")).place(x=500, y=140)
Label(text = "Costo Acumulado: " ,bg= "#E4B2F0", font = ("Verdana", 14, "italic")).place(x=300, y=140)

#Textfields
entrada = StringVar()
entrada.set("ejemplo.txt")
campo = Entry(raiz, font= ("Verdana",12), textvariable = entrada, width= 40).place(x=30, y=70)

#Botón
b1 = Button(raiz, command = lambda: obtenerArchivo(entrada.get()),text="Cargar", font= ("Verdana",18, "bold italic"))
b1.place(x=470, y=25)

b2 = Button(raiz, command = lambda: crearHilo(algPorCosto) ,text="Costo Uniforme (Rápido)", font= ("Verdana",13, "bold italic"), state="disabled")
b2.place(x=670, y=30)
b3 = Button(raiz, command = lambda: crearHilo(algPorCosto2) ,text="Costo Uniforme (Lento)", font= ("Verdana",13, "bold italic"), state="disabled")
b3.place(x=670, y=80)
b4 = Button(raiz, command = lambda: crearHilo(algAAsterisco) ,text="Algoritmo A*", font= ("Verdana",13, "bold italic"), state="disabled")
b4.place(x=670, y=130)

raiz.mainloop()
