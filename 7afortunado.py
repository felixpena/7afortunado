from tkinter import *


class SieteAfortunado:
    def __init__(self):
        self.crear_interfaz()
    
    def crear_interfaz(self):
        ventana = Tk()
        ventana.minsize(340,450)
        ventana.geometry("340x450")

        boton = Button(ventana, text="jugar", command=self.jugar, font="arial 18 bold")
        boton.pack()
        foto = PhotoImage(file=r"image\money.png")
        self.gano = Label(ventana, image=foto) 

        self.campos = [StringVar() for elemento in range(3)]
        posicion = 10
        for campo in self.campos:
            label = Label(ventana, textvariable = campo, background = "white", foreground="black", font="arial 42 bold")
            label.place(x=posicion, y=100,width=100,height=100)
            posicion += 110
        
        mainloop()
    
    def jugar():
        print("jugando!")

jugar = SieteAfortunado()