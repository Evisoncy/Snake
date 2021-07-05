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

    #botones del menu principal
    botonIniciar = Button(ventana, text="J1 vs J2", font=("Verdana",8),command=iniciar).place(x=15,y=250)
    botonIniciar = Button(ventana, text="J1 vs Computadora", font=("Verdana",8)).place(x=90,y=250)
    botonIniciar = Button(ventana, text="Reglas", font=("Verdana",8)).place(x=230,y=250)
#    botonIniciar = Button(ventana, text="Iniciar", font=("Verdana",11),command=iniciar).place(x=26,y=31)


    raiz.mainloop()