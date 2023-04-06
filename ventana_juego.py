"""
******************************************************************************************************
                                            Instituto Tecnológico de Costa Rica
                                                Ingeniería en Computadores
        Lenguaje Python 3.11.2
        Tkinter 8.6.12
        Space Impact
        Autor: Jeison Johel Picado Picado
        Versión: 1.0
        Fecha de Última Modificación: Marzo, 05/04/2023
        ******************************************************************************************************
"""
from tkinter import * #librería de la interfaz gráfica a utilizar
import time

#Crea la ventana del juego
ventana_juego = Tk()
ventana_juego.minsize(width = 800, height = 600)
ventana_juego.resizable(width = NO, height = NO)
ventana_juego.config(background='black')

#Crea el lienzo donde se desarrolla el juego
lienzo_juego = Canvas(ventana_juego, width = 776, height = 576, background='violet')
lienzo_juego.place(x = 10, y = 10)

#Crea la nave (un cuadrado provisional)
nave = lienzo_juego.create_rectangle(5, 5, 40, 40, fill = 'purple', outline = 'black', tags = 'nave_jugador')

def mover_nave_arriba(event):
    """
    Mueve la nave de su posición actual a una posición mas arriba dentro del lienzo del juego
    """
    lienzo_juego.move("nave_jugador", 0, -10)

def mover_nave_abajo(event):
    """
    Mueve la nave de su posición actual a una posición mas abajo dentro del lienzo del juego
    """
    lienzo_juego.move("nave_jugador", 0, 10)

def mover_nave_izquierda(event):
    """
    Mueve la nave de su posición actual a una posición mas a la izquierda dentro del lienzo del juego
    """
    lienzo_juego.move("nave_jugador", -10, 0)

def mover_nave_derecha(event):
    """
    Mueve la nave de su posición actual a una posición mas a la derecha del lienzo del juego
    """
    lienzo_juego.move("nave_jugador", 10, 0)

#Eventos del movimiento de la nave
lienzo_juego.bind('<Up>', mover_nave_arriba) #Al presionar la flecha hacia arriba estando en el lienzo juego mueve la nave hacia arriba
lienzo_juego.bind('<Down>', mover_nave_abajo) #Al presionar la flecha hacia arriba estando en el lienzo juego mueve la nave hacia abajo
lienzo_juego.bind('<Left>', mover_nave_izquierda) #Al presionar la flecha hacia arriba estando en el lienzo juego mueve la nave hacia la izquierda
lienzo_juego.bind('<Right>', mover_nave_derecha) #Al presionar la flecha hacia arriba estando en el lienzo juego mueve la nave hacia la derecha

lienzo_juego.focus_set()

ventana_juego.mainloop()