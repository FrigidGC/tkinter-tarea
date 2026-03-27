import tkinter as tk
import pygame
# Inicializar el mixer de pygame
pygame.mixer.init()

ventanas_abiertas = 0

#Análisis de numeros
def NumerosPares(root):
    #Define si puede o no abri una ventana
    global ventanas_abiertas

    if ventanas_abiertas == 1:
        return
    ventanas_abiertas += 1

    # Encuentra los numeros validos para hacer pares y lo agrega a una lista
    def encontrar_pares(num, a=1, resultado=None):
        if resultado is None:
            resultado = []

        if a > (num/2):
            return resultado

        if num % a == 0:
            b = num // a
            if a <= b:
                resultado.append((a,",", b),)
                resultado.append(",")

        return encontrar_pares(num, a + 1, resultado)
#Al ser la funcion recursiva no acepta numeros mayores a 980, ya que choca con el limite de interacciones al revisar el numero
    # Funcion para el boton que llama a la funcion anterior
    def calcular():
        try:
            num = int(Entrada.get())
            canvasnum.delete("all")
            if num > 1991:
                canvasnum.create_text(10, 10, text="Ingrese un numero menor a 1991", font=("Arial", 12), anchor="nw")
                return
            if num <= 0:
                canvasnum.create_text(10, 10, text="Ingrese un entero positivo", anchor="nw")
                return

            pares = encontrar_pares(num)


        #Agrega el resultado en el canvas
            canvasnum.create_text(10, 10, text=pares, font=("Arial", 12), anchor="nw", width=350)

        #atrapar error    
        except ValueError:
            canvasnum.delete("all")
            canvasnum.create_text(10, 10, text="Ingrese un número válido", anchor="nw")
#Ventana
    ventana = tk.Toplevel(root)
    ventana.title("Pares (a x b = n)")
    ventana.geometry("400x470")
    ventana.resizable(False, False)

    tk.Label(ventana, text="Ingrese un número:", font=("Arial", 16)).pack(pady=10)
    tk.Label(ventana, text="Restricción:Recursividad, numero maximo: 1991", font=("Arial", 10)).pack(pady=10)
#La caja de texto que recibe el numero
    Entrada = tk.Entry(ventana)
    Entrada.pack(pady=10)
#canva
    canvasnum = tk.Canvas(ventana, width=360, height=250, bg="white")
    canvasnum.pack()
#Boton para calcular
    tk.Button(ventana, text="Calcular", command=calcular).pack(pady=10)

    def cerrar():
        global ventanas_abiertas
        ventanas_abiertas -= 1
        ventana.destroy()
    ventana.protocol("WM_DELETE_WINDOW", cerrar)
    tk.Button(ventana, text="Cerrar", command=lambda:cerrar(), bg="#f44336", fg="white", width=15).pack()

#Ficha personal
def Ficha(root):
    #Define si puede o no abrir una ventana
    global ventanas_abiertas

    if ventanas_abiertas == 1:
        return
    ventanas_abiertas += 1

# Ventana
    ventanaf = tk.Toplevel(root)
    ventanaf.title("Ficha Personal")
    ventanaf.geometry("950x800")
    ventanaf.configure(bg="#87CEEB")
    ventanaf.resizable(False, False)
    tk.Label(ventanaf, text="Ficha Personal", font=("Arial", 20, "bold"), bg="#f0f0f0").pack(pady=20)

 #La variables de control de música
    def play_music():
        pygame.mixer.music.play()

    def pause_music():
        pygame.mixer.music.pause()

    def unpause_music():
        pygame.mixer.music.unpause()

    def stop_music():
        pygame.mixer.music.stop()

    # Cargar música, Recortado con Blender btw
    pygame.mixer.music.load("who-can-it-be-now.mp3")

# Canvas Ficha
    Canvaf = tk.Canvas(ventanaf,bg="#B6FFFB", width=600, height=600)
    Canvaf.pack()
    imagenper = tk.PhotoImage(file="CasaProg.png") 
    imagenpermostrar = tk.Label(Canvaf, image=imagenper)
    imagenpermostrar.image = imagenper
    imagenpermostrar.pack(pady=0, side="left")
    tk.Label(Canvaf, text="Nombre: Andrés Felipe Guerrero Cervantes", font=("Arial", 18, "bold"), bg="#B6FFFB").pack(pady=15)
    tk.Label(Canvaf, text="Carnet: 2026094459", font=("Arial", 18, "bold"), bg="#B6FFFB").pack(pady=15)
    tk.Label(Canvaf, text="Edad: 18 Años", font=("Arial", 18, "bold"), bg="#B6FFFB").pack(pady=15)
    tk.Label(Canvaf, text="Biografía: Estudiante de primer ingreso del Tecnologico de Costa Rica ", font=("Arial", 10, "bold"), bg="#B6FFFB").pack(pady=10)
    tk.Label(Canvaf, text="en la carrera de Computadores, tengo 18 años y vivo en Pérez Zeledón", font=("Arial", 10, "bold"), bg="#B6FFFB").pack(pady=10)

# Canvas Musica
    CMusic = tk.Canvas(ventanaf, bg="yellow", width=500, height=750)
    CMusic.pack(pady=10)

    # Botones, label e imagen
    imagenM = tk.PhotoImage(file="Men_At_Work.png") 
    imagenmusic = tk.Label(CMusic, image=imagenM)
    imagenmusic.image = imagenM
    imagenmusic.pack(pady=10, padx=20, side="left")

    tk.Label(CMusic, text="Género musical: Pop Rock", font=("Arial", 16)).pack(pady=20, padx=20)
    tk.Button(CMusic, text="Play", width=10, command=play_music).pack(pady=10, padx=20)
    tk.Button(CMusic, text="Pause", width=10, command=pause_music).pack(pady=10, padx=20)
    tk.Button(CMusic, text="Unpause", width=10, command=unpause_music).pack(pady=10, padx=20)
    tk.Button(CMusic, text="Stop", width=10, command=stop_music).pack(pady=10, padx=20)


#Cierra la musica al cerrar ventana
    def cerrar():
        global ventanas_abiertas
        ventanas_abiertas -= 1
        ventanaf.destroy()
        pygame.mixer.music.stop()

    ventanaf.protocol("WM_DELETE_WINDOW", cerrar)
    tk.Button(Canvaf, text="Cerrar", command=lambda:cerrar(), bg="#f44336", fg="white", width=15).pack(pady=10)

#Grafico
def GraficoBolas(root):
#Define si puede o no abrir una ventana
    global ventanas_abiertas

    if ventanas_abiertas == 1:
        return
    ventanas_abiertas += 1

    window = tk.Toplevel(root)
    window.geometry("600x800")
    window.resizable(False, False)
    window.title("Bolas rebotando")

    canva2 = tk.Canvas(window, bg="#87CEEB", width=600, height=600)
    canva2.pack()

#Los sliders para controlar la velocidad de las bolas
    tk.Label(window, text="Velocidad X bola").pack()
    velocidadx_scale = tk.Scale(window, from_=1, to=15, orient='horizontal')
    velocidadx_scale.set(6)
    velocidadx_scale.pack()

    tk.Label(window, text="Velocidad Y bola").pack()
    velocidady_scale = tk.Scale(window, from_=1, to=15, orient='horizontal')
    velocidady_scale.set(4)
    velocidady_scale.pack()

#Las Bolas
    Ball = canva2.create_oval(300, 250, 380, 330, fill="yellow")
    Ball2 = canva2.create_oval(100, 50, 180, 130, fill="red")

# Variables Velocidades a partir del valor de los sliders
    xspeed1 = velocidadx_scale.get()
    yspeed1 = velocidady_scale.get()
    xspeed2 = -velocidadx_scale.get()
    yspeed2 = -velocidady_scale.get()
    choque_activo = False

    def moveball():
        nonlocal xspeed1, yspeed1, xspeed2, yspeed2, choque_activo

# Convierte las velocidades en 1 o -1 para multiplicar por la velocidad real
        xspeedmult1 = (1 if xspeed1 >= 0 else -1)
        yspeedmult1 = (1 if yspeed1 >= 0 else -1)
        xspeedmult2 = (1 if xspeed2 >= 0 else -1)
        yspeedmult2 = (1 if yspeed2 >= 0 else -1)
        xspeed1 = xspeedmult1* velocidadx_scale.get()
        yspeed1 = yspeedmult1 * velocidady_scale.get()
        xspeed2 = xspeedmult2 * velocidadx_scale.get()
        yspeed2 = yspeedmult2 * velocidady_scale.get()

# Mover bolas
        canva2.move(Ball, xspeed1, yspeed1)
        canva2.move(Ball2, xspeed2, yspeed2)

#Coordenadas
        left1, top1, right1, bottom1 = canva2.coords(Ball)
        left2, top2, right2, bottom2 = canva2.coords(Ball2)

# Rebote paredes
        if left1 <= 0 or right1 >= 600:
            xspeed1 = -xspeed1
        if top1 <= 0 or bottom1 >= 600:
            yspeed1 = -yspeed1
        if left2 <= 0 or right2 >= 600:
            xspeed2 = -xspeed2
        if top2 <= 0 or bottom2 >= 600:
            yspeed2 = -yspeed2

# Colisión
        if not (right1 < left2 or left1 > right2 or bottom1 < top2 or top1 > bottom2) and not choque_activo:
                xspeed1, xspeed2 = xspeed2, xspeed1
                yspeed1, yspeed2 = yspeed2, yspeed1
                choque_activo = True
        else:
            choque_activo = False

        canva2.after(10, moveball)

    moveball()

    # Botón para volver a la ventana principal
    def cerrar():
        global ventanas_abiertas
        ventanas_abiertas -= 1
        window.destroy()

    window.protocol("WM_DELETE_WINDOW", cerrar)
    volver_btn = tk.Button(window, text="Cerrar Ventana", command=lambda:cerrar(), bg="#f44336", fg="white", width=15)
    volver_btn.pack(pady=10)

#Ventana principal
root = tk.Tk()
root.title("Tarea-taller-grafico")
root.geometry("500x650")
root.resizable(width=False, height=False)
root.configure(bg="yellow")
tk.Label(root, text="Menú Principal", font=("Arial", 20, "bold"), bg="yellow").pack(pady=30)


Canv1 = tk.Canvas(root, bg="#f0f0f0", width=500, height=330)
Canv1.pack(pady=0)
imagenp = tk.PhotoImage(file="ConBdeVaca.png") 
imagenpmostrar = tk.Label(Canv1, image=imagenp)
imagenpmostrar.image = imagenp
imagenpmostrar.pack(pady=0)

ButtonBall = tk.Button(root, text="Bolas rebotando", command=lambda:GraficoBolas(root))
ButtonBall.pack(pady=15)

ButtonPers = tk.Button(root, text="Ficha Personal", command=lambda:Ficha(root))
ButtonPers.pack(pady=15)

ButtonNum = tk.Button(root, text="Análisis de numeros", command=lambda:NumerosPares(root))
ButtonNum.pack(pady=15)

root.mainloop()