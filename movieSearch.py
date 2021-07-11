import pyautogui as robot
import time

lista_peliculas = ["la la land"]

navegador = input("Que navegador usas?")
pelicula = input("Que Pelicula quieres buscar 🎬?")

#navegador = 266, 742
direc = 380, 49
buscarMega = 1002, 385
peliculaMega = 265, 392

buscarCueva = 958, 155
peliculaCueva = 215, 415

buscarYts = 726, 132
peliculaYts = 0, 0

duracion = 8

time.sleep(3)

#Funcion para abrir
def abrir (pos, click = 1):
    robot.moveTo(pos)
    robot.click(clicks=click)

#Abrir el navegador
robot.hotkey("Win","s")
time.sleep(2)
robot.typewrite(navegador)
time.sleep(1)
robot.hotkey("enter")
time.sleep(2)

#Introducir atajos de teclado
robot.hotkey("ctrl","t")
time.sleep(0.5)

abrir(direc,click=1)
time.sleep(2)

#escribir texto
robot.typewrite("megapeliculasrip.com")
robot.hotkey("enter")
time.sleep(3)

#Seleccionar cuadro de la pelicula
abrir(buscarMega,click=1)

#for elemento in range (len(lista_peliculas)):
#print(elemento)
#robot.typewrite(lista_peliculas[elemento])

robot.typewrite(pelicula)
robot.hotkey("enter")
time.sleep(2)
abrir(peliculaMega, click=1)

#Abrir Cuevana
robot.hotkey("ctrl","t")
time.sleep(0.5)

abrir(direc,click=1)
time.sleep(2)

robot.typewrite("cuevana3.io")
robot.hotkey("enter")
time.sleep(3)

abrir(buscarCueva, click=1)
robot.typewrite(pelicula)
robot.hotkey("enter")
time.sleep(2)

abrir(peliculaCueva, click=1)
time.sleep(2)

#Abrir Yts
robot.hotkey("ctrl","t")
time.sleep(0.6)

abrir(direc,click=1)
time.sleep(3)

robot.typewrite("yts.mx")
robot.hotkey("enter")
time.sleep(5)

abrir(buscarYts,click=1)
robot.typewrite(pelicula)
time.sleep(2)
robot.hotkey("enter")

salida = input ("Disfruta tu pelicula 🎥")

print=("Proceso Terminado, Disfruta tu pelicula 🎥!")

