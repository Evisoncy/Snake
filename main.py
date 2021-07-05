from aplicacion import *
from tkinter import *

# Recuerda tener todos los archivos en una misma carpeta
# para que los imports no tengan problemas.
if __name__ == '__main__':
    aplicacion = aplicacion ()
   
    raiz=Tk()
    raiz.title("SNAKE")
    raiz.resizable(0,0)
    raiz.config(bg="black")
    ventana = Frame(raiz,height=300, width=300)
    ventana.config(bg="black")
    ventana.pack()
    img=PhotoImage(file="snake.png")
    imagen = Label(ventana, image=img)
    imagen.place(x=47,y=22)

    #funciones de los botones
    def iniciar():
        aplicacion.on_execute()

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
    botonIniciar = Button(ventana, text="J1 vs J2", font=("Verdana",8),command=iniciar).place(x=15,y=250)
    botonIniciarvsC = Button(ventana, text="J1 vs Computadora", font=("Verdana",8)).place(x=90,y=250)
    botonReglas = Button(ventana, text="Reglas", font=("Verdana",8),command=reglas).place(x=230,y=250)
#   botonIniciar = Button(ventana, text="Iniciar", font=("Verdana",11),command=iniciar).place(x=26,y=31)


    raiz.mainloop()