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
from types import NoneType


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

teclas_presionadas = {} #dicionario que almacena el estado de las teclas presionadas

flag_mover_arriba = False #Bandera que indica si debe moverse la nave hacia arriba
flag_mover_abajo = False #Bandera que indica si debe moverse la nave hacia abajo
flag_mover_izquierda = False #Bandera que indica si debe moverse la nave hacia izquierda
flag_mover_derecha = False #Bandera que indica si debe moverse la nave hacia derecha
flag_mover_municion = False #Bandera que indica si se debe moverse la municion
no_tag_municion = 0 #Ayuda a darle un tag diferente a cada munición

tiempo_nave = 6 #indica el tiempo que pasa entre que la nave se mueve de su posición actual a la siguiente despazándose pixel por pixel
tiempo_municion = 6 #indica el tiempo que pasa entre que la municion se mueve de su posición actual a la siguiente despazándose pixel por pixel
frecuencia_de_disparo = 0.006

def accion_a_ejecutar(event):
    """
    Elige la acción a realizar según la tecla o teclas presionadas
    """
    global teclas_presionadas
    teclas_presionadas[event.keycode] = event.keysym
    if 'Up' in teclas_presionadas.values():
        mover_nave_arriba()
    elif 'Down' in teclas_presionadas.values():
        mover_nave_abajo()
    elif 'Left' in teclas_presionadas.values():
        mover_nave_izquierda()
    elif 'Right' in teclas_presionadas.values():
        mover_nave_derecha()
    elif 'x' in teclas_presionadas.values():
        mover_municion()

def actualiza_estado_tecla(event):
    """
    actualiza el estado de la tecla
    """
    global teclas_presionadas
    del teclas_presionadas[event.keycode]
    if event.keysym == 'Up':
        detener_movimiento_nave_arriba()
    elif event.keysym == 'Down':
        detener_movimiento_nave_abajo()
    elif event.keysym == 'Left':
        detener_movimiento_nave_izquierda()
    elif event.keysym == 'Right':
        detener_movimiento_nave_derecha()

def movimiento_nave_arriba():
    """
    Mueve la nave recursivamente
    """
    global flag_mover_arriba #permite cambiar el valor de la variable global
    if flag_mover_arriba == True:
        y1 = lienzo_juego.bbox('nave_jugador')[1]#.bbox retorna una tupla (x1, y1, x2, y2) donde los primeros dos valores son la esquina superior izquierda del rectángulo y los ultimos dos la esquina inferior derecha del rectángulo
        if y1 > 1:
            lienzo_juego.move("nave_jugador", 0, -1)
            lienzo_juego.after(tiempo_nave, movimiento_nave_arriba)
        else:
            flag_mover_arriba = False

def detener_movimiento_nave_arriba():
    """
    detiene el movimiento de la nave en la dirección hacia arriba
    """
    global flag_mover_arriba #permite cambiar el valor de la variable global
    flag_mover_arriba = False

def mover_nave_arriba():
    """
    Da la orden de comenzar a mover la nave
    """
    global flag_mover_arriba #permite cambiar el valor de la variable global
    y1 = lienzo_juego.bbox('nave_jugador')[1]#.bbox retorna una tupla (x1, y1, x2, y2) donde los primeros dos valores son la esquina superior izquierda del rectángulo y los ultimos dos la esquina inferior derecha del rectángulo
    if y1 > 1:
        flag_mover_arriba = True
        movimiento_nave_arriba()

"""
#Hilo para que la nave se mueva hacia arriba
up = Thread(target=movimiento_nave_arriba, args=())
up.start()
"""
def movimiento_nave_abajo():
    """
    Mueve la nave recursivamente
    """
    global flag_mover_abajo #permite cambiar el valor de la variable global
    if flag_mover_abajo == True:
        y2 = lienzo_juego.bbox('nave_jugador')[3]#.bbox retorna una tupla (x1, y1, x2, y2) donde los primeros dos valores son la esquina superior izquierda del rectángulo y los ultimos dos la esquina inferior derecha del rectángulo
        if y2 < 575:
            lienzo_juego.move("nave_jugador", 0, 1)
            lienzo_juego.after(tiempo_nave, movimiento_nave_abajo)
        else:
            flag_mover_abajo = False

def detener_movimiento_nave_abajo():
    """
    detiene el movimiento de la nave en la dirección hacia abajo
    """
    global flag_mover_abajo #permite cambiar el valor de la variable global
    flag_mover_abajo = False

def mover_nave_abajo():
    """
    Da la orden de comenzar a mover la nave
    """
    global flag_mover_abajo #permite cambiar el valor de la variable global
    y2 = lienzo_juego.bbox('nave_jugador')[1]#.bbox retorna una tupla (x1, y1, x2, y2) donde los primeros dos valores son la esquina superior izquierda del rectángulo y los ultimos dos la esquina inferior derecha del rectángulo
    if y2 < 575:
        flag_mover_abajo = True
        movimiento_nave_abajo()

"""
#Hilo para que la nave se mueva hacia abajo
down = Thread(target=movimiento_nave_abajo, args=())
down.start()
"""
def movimiento_nave_izquierda():
    """
    Mueve la nave recursivamente
    """
    global flag_mover_izquierda #permite cambiar el valor de la variable global
    if flag_mover_izquierda == True:
        x1 = lienzo_juego.bbox('nave_jugador')[0]#.bbox retorna una tupla (x1, y1, x2, y2) donde los primeros dos valores son la esquina superior izquierda del rectángulo y los ultimos dos la esquina inferior derecha del rectángulo
        if x1 > 1:
            lienzo_juego.move("nave_jugador", -1, 0)
            lienzo_juego.after(tiempo_nave, movimiento_nave_izquierda)
        else:
            flag_mover_izquierda = False

def detener_movimiento_nave_izquierda():
    """
    detiene el movimiento de la nave en la dirección hacia la izquierda
    """
    global flag_mover_izquierda #permite cambiar el valor de la variable global
    flag_mover_izquierda = False

def mover_nave_izquierda():
    """
    Da la orden de comenzar a mover la nave
    """
    global flag_mover_izquierda #permite cambiar el valor de la variable global
    x1 = lienzo_juego.bbox('nave_jugador')[0]#.bbox retorna una tupla (x1, y1, x2, y2) donde los primeros dos valores son la esquina superior izquierda del rectángulo y los ultimos dos la esquina inferior derecha del rectángulo
    if x1 > 1:
        flag_mover_izquierda = True
        movimiento_nave_izquierda()
"""
#Hilo para que la nave se mueva hacia la izquierda
left = Thread(target=movimiento_nave_izquierda, args=())
left.start()
"""
def movimiento_nave_derecha():
    """
    Mueve la nave recursivamente
    """
    global flag_mover_derecha #permite cambiar el valor de la variable global
    if flag_mover_derecha == True:
        x2 = lienzo_juego.bbox('nave_jugador')[2]#.bbox retorna una tupla (x1, y1, x2, y2) donde los primeros dos valores son la esquina superior derecha del rectángulo y los ultimos dos la esquina inferior derecha del rectángulo
        if x2 < 778:
            lienzo_juego.move("nave_jugador", 1, 0)
            lienzo_juego.after(tiempo_nave, movimiento_nave_derecha)
        else:
            flag_mover_derecha = False

def detener_movimiento_nave_derecha():
    """
    detiene el movimiento de la nave en la dirección hacia la derecha
    """
    global flag_mover_derecha #permite cambiar el valor de la variable global
    flag_mover_derecha = False

def mover_nave_derecha():
    """
    Da la orden de comenzar a mover la nave
    """
    global flag_mover_derecha #permite cambiar el valor de la variable global
    x2 = lienzo_juego.bbox('nave_jugador')[2]#.bbox retorna una tupla (x1, y1, x2, y2) donde los primeros dos valores son la esquina superior derecha del rectángulo y los ultimos dos la esquina inferior derecha del rectángulo
    if x2 < 778:
        flag_mover_derecha = True
        movimiento_nave_derecha()
"""
#Hilo que para que se mueva la nave hacia la izquierda
right = Thread(target=movimiento_nave_derecha, args=())
right.start()
"""
"""
def hilo_movimiento_municion(tag_municion):
    move_municion = Thread(target=movimiento_municion, args=(tag_municion,))
    move_municion.start()
"""

def movimiento_municion(tag_municion):
    """
    Mueve la municion recursivamente
    """
    global flag_mover_municion #permite cambiar el valor de la variable global
    if flag_mover_municion == True:
        x2_municion = lienzo_juego.bbox(tag_municion)[2]#.bbox retorna una tupla (x1, y1, x2, y2) donde los primeros dos valores son la esquina superior derecha del rectángulo y los ultimos dos la esquina inferior derecha del rectángulo   
        if x2_municion < 778:
            
            lienzo_juego.move(tag_municion, 1, 0)
            lienzo_juego.after(tiempo_municion, movimiento_municion, tag_municion)
        else:
            destruir_municion(tag_municion)
        
            

def destruir_municion(tag_municion):
    """
    detiene el movimiento de la nave
    """
    global flag_mover_municion #permite cambiar el valor de la variable global
    flag_mover_municion = False
    lienzo_juego.delete(tag_municion)

def mover_municion():
    """
    Da la orden de comenzar a mover la nave
    """
    global flag_mover_municion #permite cambiar el valor de la variable global
    global no_tag_municion #permite cambiar el valor de la variable global que le da distintas etiquetas a las municiones
    lienzo_juego.bell()
    x2 = lienzo_juego.bbox('nave_jugador')[2]#.bbox retorna una tupla (x1, y1, x2, y2) donde los primeros dos valores son la esquina superior derecha del rectángulo y los ultimos dos la esquina inferior derecha del rectángulo
    if x2 < 778:
        flag_mover_municion = True
        x1_municion = lienzo_juego.bbox('nave_jugador')[2]
        y1_municion = lienzo_juego.bbox('nave_jugador')[1] + ((lienzo_juego.bbox('nave_jugador')[3] - lienzo_juego.bbox('nave_jugador')[1]) // 2 - 1)
        x2_municion = x1_municion + 5
        y2_municion = y1_municion + 2
        #Crea la municion (un rectangulo)
        tag_municion = 'municion_' + str(no_tag_municion)
        lienzo_juego.create_rectangle(x1_municion, y1_municion, x2_municion, y2_municion, fill = 'black', outline = 'black', tags = tag_municion)
        no_tag_municion += 1
        movimiento_municion(tag_municion)

#Evento que ejecuta una accion dependiendo de la tecla o teclas presionadas
lienzo_juego.bind('<KeyPress>', accion_a_ejecutar)

#Evento que actualiza el estado de la tecla o teclas presionadas
lienzo_juego.bind('<KeyRelease>', actualiza_estado_tecla)

lienzo_juego.focus_set()

def actualiza_estado_pantalla():
    """
    Actualiza lo que se muestra en pantalla
    """
    lienzo_juego.after(6, lienzo_juego.update())

ventana_juego.mainloop()