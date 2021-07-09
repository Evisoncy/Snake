from aplication_i import aplicacion_i
from aplicacion import *
from tkinter import *
from aplication_e import *
from aplication_i import *

# Recuerda tener todos los archivos en una misma carpeta
# para que los imports no tengan problemas.
if __name__ == '__main__':
    aplicacion = aplicacion ()
    aplication_e = aplication_e ()
    aplicacion_i = aplicacion_i ()
    raiz=Tk()
    raiz.title("SNAKE")
    raiz.resizable(0,0)
    raiz.config(bg="black")
    ventana = Frame(raiz,height=550, width=300)
    ventana.config(bg="black")
    ventana.pack()
    img=PhotoImage(file="snake.png")
    imagen = Label(ventana, image=img)
    imagen.place(x=47,y=22)
    vsPC = Label(ventana, text="VS : PC", font=("Verdana",12), bg="black", fg="white").place(x=115,y=300)

    #funciones de los botones
    def iniciar():
        aplicacion.on_execute()

    def vsJ2():
        aplication_e.on_execute()

    def facil():
        aplicacion_i.on_execute()      

    def reglas():
        raiz = Tk()
        raiz.title("REGLAS")
        raiz.resizable(0,0)

        ventana = Frame(raiz, height="200", width="520")
        ventana.config(bg="black")
        ventana.pack()
        title = Label(ventana, text="REGLAS DE JUEGO", bg="black", fg="white").place(x=10, y=10)
        rule1 = Label(ventana, text="1. Cada jugador controlará una serpiente.", bg="black", fg="white").place(x=10, y=40)
        rule2 = Label(ventana, text="2. Cada jugador comienza con el mismo tamaño por defecto de serpiente.", bg="black", fg="white").place(x=10, y=60)
        rule3 = Label(ventana, text="3. Mientras más manzanas atrapes más grande será la serpiente.", bg="black", fg="white").place(x=10, y=80)
        rule4 = Label(ventana, text="4. Intenta no chocar la cabeza de tu serpiente con la parte del cuerpo tuya o de la otra serpiente.", bg="black", fg="white").place(x=10, y=100)
        rule5 = Label(ventana, text="5. Gana la serpiente más grande hasta el momento en que cualquier serpiente choque.", bg="black", fg="white").place(x=10, y=120)
        rule6 = Label(ventana, text="6. Caso contrario gana la primera serpiente en comer 15 manzanas.", bg="black", fg="white").place(x=10, y=140)
        raiz.mainloop()

    #botones del menu principal
    botonIniciar = Button(ventana, text="J1 vs J2", font=("Verdana",10),command=vsJ2).place(x=120,y=250)
    botonIniciarvsCF = Button(ventana, text="FACIL", font=("Verdana",10),command=facil).place(x=120,y=350)
    botonIniciarvsCM = Button(ventana, text="MEDIO", font=("Verdana",10)).place(x=120,y=400)
    botonIniciarvsCD = Button(ventana, text="DIFICiL", font=("Verdana",10),command=iniciar).place(x=119,y=450)
    botonReglas = Button(ventana, text="Reglas", font=("Verdana",10),command=reglas).place(x=120,y=500)
#   botonIniciar = Button(ventana, text="Iniciar", font=("Verdana",11),command=iniciar).place(x=26,y=31)


    raiz.mainloop()