"""
**************************************************************************************************************
                                            Instituto Tecnológico de Costa Rica
                                                Ingeniería en Computadores
        Lenguaje Python 3.11.2
        Tkinter 8.6.12
        Space Impact
        Autor: Jeison Johel Picado Picado
        Versión: 1.0
        Fecha de Última Modificación: Marzo, 05/04/2023
**************************************************************************************************************
"""
from tkinter import * #librería de la interfaz gráfica a utilizar
import time #librería  de tiempo
from threading import Thread ##Thread (hilo), para evitar threading.Thread

def ventana_juego():
    #Crea la ventana del juego
    ventana_juego = Toplevel()
    ventana_juego.minsize(width = 800, height = 600)
    ventana_juego.resizable(width = NO, height = NO)
    ventana_juego.config(background='black')

    #Crea el lienzo donde se desarrolla el juego
    lienzo_juego = Canvas(ventana_juego, width = 776, height = 576, background='violet')
    lienzo_juego.place(x = 10, y = 10)

    #Crea la nave (un cuadrado provisional)
    nave = lienzo_juego.create_rectangle(5, 5, 40, 40, fill = 'purple', outline = 'black', tags = 'nave_jugador')

    flag_mover_arriba = False #Bandera que indica si debe moverse la nave hacia arriba
    flag_mover_abajo = False #Bandera que indica si debe moverse la nave hacia abajo
    flag_mover_izquierda = False #Bandera que indica si debe moverse la nave hacia izquierda
    flag_mover_derecha = False #Bandera que indica si debe moverse la nave hacia derecha
    flag_mover_municion = False #Bandera que indica si se debe moverse la municion
    no_tag_municion = 0

    tiempo_nave = 0.006 #indica el tiempo que pasa entre que la nave se mueve de su posición actual a la siguiente despazándose pixel por pixel
    tiempo_municion = 0.006 #indica el tiempo que pasa entre que la municion se mueve de su posición actual a la siguiente despazándose pixel por pixel

    def hilo_movimiento_nave_arriba():
        up = Thread(target=movimiento_nave_arriba, args=())
        up.start()

    def movimiento_nave_arriba():
        """
        Mueve la nave recursivamente
        """
        nonlocal flag_mover_arriba
        if flag_mover_arriba == True:
            y1 = lienzo_juego.bbox('nave_jugador')[1]#.bbox retorna una tupla (x1, y1, x2, y2) donde los primeros dos valores son la esquina superior izquierda del rectángulo y los ultimos dos la esquina inferior derecha del rectángulo
            if y1 > 1:
                lienzo_juego.move("nave_jugador", 0, -1)
                time.sleep(tiempo_nave)
                lienzo_juego.update()
                movimiento_nave_arriba()
            else:
                flag_mover_arriba = False

    def detener_movimiento_nave_arriba(event):
        """
        detiene el movimiento de la nave
        """
        nonlocal flag_mover_arriba
        flag_mover_arriba = False
        lienzo_juego.focus_set()

    def mover_nave_arriba(event):
        """
        Da la orden de comenzar a mover la nave
        """
        nonlocal flag_mover_arriba
        ventana_juego.focus_set() #pasa el foco a la ventana principal, esto evita que el evento llame a la función varias veces
        y1 = lienzo_juego.bbox('nave_jugador')[1]#.bbox retorna una tupla (x1, y1, x2, y2) donde los primeros dos valores son la esquina superior izquierda del rectángulo y los ultimos dos la esquina inferior derecha del rectángulo
        if y1 > 1:
            flag_mover_arriba = True
            hilo_movimiento_nave_arriba()
            lienzo_juego.focus_set()

    def hilo_movimiento_nave_abajo():
        down = Thread(target=movimiento_nave_abajo, args=())
        down.start()

    def movimiento_nave_abajo():
        """
        Mueve la nave recursivamente
        """
        nonlocal flag_mover_abajo
        if flag_mover_abajo == True:
            y2 = lienzo_juego.bbox('nave_jugador')[3]#.bbox retorna una tupla (x1, y1, x2, y2) donde los primeros dos valores son la esquina superior izquierda del rectángulo y los ultimos dos la esquina inferior derecha del rectángulo
            if y2 < 575:
                lienzo_juego.move("nave_jugador", 0, 1)
                time.sleep(tiempo_nave)
                lienzo_juego.update()
                movimiento_nave_abajo()
            else:
                flag_mover_abajo = False

    def detener_movimiento_nave_abajo(event):
        """
        detiene el movimiento de la nave
        """
        nonlocal flag_mover_abajo
        flag_mover_abajo = False
        lienzo_juego.focus_set()

    def mover_nave_abajo(event):
        """
        Da la orden de comenzar a mover la nave
        """
        nonlocal flag_mover_abajo

        ventana_juego.focus_set() #pasa el foco a la ventana principal, esto evita que el evento llame a la función varias veces
        y2 = lienzo_juego.bbox('nave_jugador')[3]#.bbox retorna una tupla (x1, y1, x2, y2) donde los primeros dos valores son la esquina superior izquierda del rectángulo y los ultimos dos la esquina inferior derecha del rectángulo
        if y2 < 575:
            flag_mover_abajo = True
            hilo_movimiento_nave_abajo()
            lienzo_juego.focus_set()

    def hilo_movimiento_nave_izquierda():
        left = Thread(target=movimiento_nave_izquierda, args=())
        left.start()

    def movimiento_nave_izquierda():
        """
        Mueve la nave recursivamente
        """
        nonlocal flag_mover_izquierda
        if flag_mover_izquierda == True:
            x1 = lienzo_juego.bbox('nave_jugador')[0]#.bbox retorna una tupla (x1, y1, x2, y2) donde los primeros dos valores son la esquina superior izquierda del rectángulo y los ultimos dos la esquina inferior derecha del rectángulo
            if x1 > 1:
                lienzo_juego.move("nave_jugador", -1, 0)
                time.sleep(tiempo_nave)
                lienzo_juego.update()
                movimiento_nave_izquierda()
            else:
                flag_mover_izquierda = False

    def detener_movimiento_nave_izquierda(event):
        """
        detiene el movimiento de la nave
        """
        nonlocal flag_mover_izquierda
        flag_mover_izquierda = False
        lienzo_juego.focus_set()

    def mover_nave_izquierda(event):
        """
        Da la orden de comenzar a mover la nave
        """
        nonlocal flag_mover_izquierda
        ventana_juego.focus_set() #pasa el foco a la ventana principal, esto evita que el evento llame a la función varias veces
        x1 = lienzo_juego.bbox('nave_jugador')[0]#.bbox retorna una tupla (x1, y1, x2, y2) donde los primeros dos valores son la esquina superior izquierda del rectángulo y los ultimos dos la esquina inferior derecha del rectángulo
        if x1 > 1:
            flag_mover_izquierda = True
            hilo_movimiento_nave_izquierda()
            lienzo_juego.focus_set()

    def hilo_movimiento_nave_derecha():
        right = Thread(target=movimiento_nave_derecha, args=())
        right.start()

    def movimiento_nave_derecha():
        """
        Mueve la nave recursivamente
        """
        nonlocal flag_mover_derecha
        if flag_mover_derecha == True:
            x2 = lienzo_juego.bbox('nave_jugador')[2]#.bbox retorna una tupla (x1, y1, x2, y2) donde los primeros dos valores son la esquina superior derecha del rectángulo y los ultimos dos la esquina inferior derecha del rectángulo
            if x2 < 778:
                lienzo_juego.move("nave_jugador", 1, 0)
                time.sleep(tiempo_nave)
                lienzo_juego.update()
                movimiento_nave_derecha()
            else:
                flag_mover_derecha = False

    def detener_movimiento_nave_derecha(event):
        """
        detiene el movimiento de la nave
        """
        nonlocal flag_mover_derecha
        flag_mover_derecha = False
        lienzo_juego.focus_set()

    def mover_nave_derecha(event):
        """
        Da la orden de comenzar a mover la nave
        """
        ventana_juego.focus_set() #pasa el foco a la ventana principal, esto evita que el evento llame a la función varias veces
        x2 = lienzo_juego.bbox('nave_jugador')[2]#.bbox retorna una tupla (x1, y1, x2, y2) donde los primeros dos valores son la esquina superior derecha del rectángulo y los ultimos dos la esquina inferior derecha del rectángulo
        if x2 < 778:
            flag_mover_derecha = True
            hilo_movimiento_nave_derecha()
            lienzo_juego.focus_set()

    def hilo_movimiento_municion(tag_municion):
        move_municion = Thread(target=movimiento_municion, args=(tag_municion,))
        move_municion.start()

    def movimiento_municion(tag_municion):
        """
        Mueve la municion recursivamente
        """
        if flag_mover_municion == True:
            x1_municion = lienzo_juego.bbox(tag_municion)[0]#.bbox retorna una tupla (x1, y1, x2, y2) donde los primeros dos valores son la esquina superior derecha del rectángulo y los ultimos dos la esquina inferior derecha del rectángulo
            if x1_municion < 778:
                
                lienzo_juego.move(tag_municion, 1, 0)
                time.sleep(tiempo_municion)
                lienzo_juego.update()
                movimiento_municion(tag_municion)
            else:
                destruir_municion(tag_municion)
                

    def destruir_municion(tag_municion):
        """
        detiene el movimiento de la nave
        """
        nonlocal flag_mover_municion
        flag_mover_municion = False
        lienzo_juego.delete(tag_municion)

    def mover_municion(event):
        """
        Da la orden de comenzar a mover la nave
        """
        nonlocal flag_mover_municion
        x2 = lienzo_juego.bbox('nave_jugador')[2]#.bbox retorna una tupla (x1, y1, x2, y2) donde los primeros dos valores son la esquina superior derecha del rectángulo y los ultimos dos la esquina inferior derecha del rectángulo
        if x2 < 778:
            flag_mover_municion = True
            x1_municion = lienzo_juego.bbox('nave_jugador')[2]
            y1_municion = lienzo_juego.bbox('nave_jugador')[1] + ((lienzo_juego.bbox('nave_jugador')[3] - lienzo_juego.bbox('nave_jugador')[1]) // 2 - 1)
            x2_municion = x1_municion + 5
            y2_municion = y1_municion + 2
            #Crea la nave (un cuadrado provisional)
            tag_municion = 'municion_' + str(no_tag_municion)
            municion = lienzo_juego.create_rectangle(x1_municion, y1_municion, x2_municion, y2_municion, fill = 'black', outline = 'black', tags = tag_municion)
            no_tag_municion =+ 1
            hilo_movimiento_municion(tag_municion)

    #Eventos que dan movimiento a la nave
    lienzo_juego.bind('<Up>', mover_nave_arriba) #Al presionar la flecha hacia arriba estando en el lienzo juego mueve la nave hacia arriba
    lienzo_juego.bind('<Down>', mover_nave_abajo) #Al presionar la flecha hacia arriba estando en el lienzo juego mueve la nave hacia abajo
    lienzo_juego.bind('<Left>', mover_nave_izquierda) #Al presionar la flecha hacia arriba estando en el lienzo juego mueve la nave hacia la izquierda
    lienzo_juego.bind('<Right>', mover_nave_derecha) #Al presionar la flecha hacia arriba estando en el lienzo juego mueve la nave hacia la derecha

    #Evento que dispara la munición
    lienzo_juego.bind('<KeyPress-x>', mover_municion)

    #Eventos que detienen el movimiento de la nave
    ventana_juego.bind('<KeyRelease-Up>', detener_movimiento_nave_arriba)
    ventana_juego.bind('<KeyRelease-Down>', detener_movimiento_nave_abajo)
    ventana_juego.bind('<KeyRelease-Left>', detener_movimiento_nave_izquierda)
    ventana_juego.bind('<KeyRelease-Right>', detener_movimiento_nave_derecha)

    def dame_coord(event):
        print(lienzo_juego.bbox('nave_jugador'))

    lienzo_juego.bind('<KeyPress-n>', dame_coord)

    ventana_juego.focus_set()



    ventana_juego.mainloop()