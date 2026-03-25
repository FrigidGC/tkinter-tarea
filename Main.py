import tkinter as tk
import pygame
# Inicializar el mixer de pygame
pygame.mixer.init()


#Análisis de numeros
def NumerosPares(root):

    # Encuentra los numeros validos para hacer pares y lo agrega a una lista
    def encontrar_pares(n, a=1, resultado=None):
        if resultado is None:
            resultado = []

        if a > n:
            return resultado

        if n % a == 0:
            b = n // a
            if a <= b:
                resultado.append((a, b))

        return encontrar_pares(n, a + 1, resultado)

    # Funcion para el boton que llama a la funcion anterior
    def calcular():
        try:
            n = int(entry.get())

            if n <= 0:
                resultado_label.config(text="Ingrese un entero positivo") #Agrega el resultado en el label
                return

            pares = encontrar_pares(n)

            texto = "Pares:\n"
            for a, b in pares:
                texto += f"({a}, {b})\n"

            resultado_label.config(text=texto)
        except ValueError:
            resultado_label.config(text="Error: Ingrese un número entero válido")

    # Ventana secundaria
    ventana = tk.Toplevel(root)
    ventana.title("Pares (a x b = n)")
    ventana.geometry("300x400")
    ventana.resizable(False, False)

    tk.Label(ventana, text="Ingrese un número:", font=("comic-sans", 12)).pack(pady=10)

    entry = tk.Entry(ventana)
    entry.pack(pady=10)

    tk.Button(ventana, text="Calcular", command=calcular).pack(pady=10)

    resultado_label = tk.Label(ventana, text="", font=("comic-sans", 12))
    resultado_label.pack(pady=20)
    tk.Button(ventana, text="Cerrar", command=ventana.destroy, bg="#f44336", fg="white", width=15).pack(pady=10)

#Musica
def Musica(root):
    #Control de música
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

    # Ventana
    ventanap = tk.Toplevel(root)
    ventanap.title("Ficha Personal")
    ventanap.geometry("500x750")
    ventanap.resizable(False, False)

    #canvas
    CMusic = tk.Canvas(ventanap, width=500, height=750)
    CMusic.pack()

    # Botones, label e imagen
    imagen = tk.PhotoImage(file="Men_At_Work.png") 
    imagenmostrar = tk.Label(CMusic, image=imagen)
    imagenmostrar.image = imagen
    imagenmostrar.pack(pady=10)

    tk.Label(CMusic, text="Género musical: Pop Rock", font=("Arial", 16)).pack(pady=20)
    tk.Button(CMusic, text="Play", width=10, command=play_music).pack(pady=10)
    tk.Button(CMusic, text="Pause", width=10, command=pause_music).pack(pady=10)
    tk.Button(CMusic, text="Unpause", width=10, command=unpause_music).pack(pady=10)
    tk.Button(CMusic, text="Stop", width=10, command=stop_music).pack(pady=10)
    def cerrar():
        pygame.mixer.music.stop()
        ventanap.destroy()
    ventanap.protocol("WM_DELETE_WINDOW", cerrar)
    tk.Button(CMusic, text="Cerrar", command=lambda: cerrar(), bg="#f44336", fg="white", width=15).pack(pady=10)

#Ficha personal
def Ficha(root):
# Ventana
    ventanaf = tk.Toplevel(root)
    ventanaf.title("Ficha Personal")
    ventanaf.geometry("600x800")
    ventanaf.configure(bg="#87CEEB")
    ventanaf.resizable(False, False)
    tk.Label(ventanaf, text="Ficha Personal", font=("Arial", 20, "bold"), bg="#f0f0f0").pack(pady=20)

# Canvas
    Canvaf = tk.Canvas(ventanaf,bg="#B6FFFB", width=600, height=600)
    Canvaf.pack()
    imagenper = tk.PhotoImage(file="CasaProg.png") 
    imagenpermostrar = tk.Label(Canvaf, image=imagenper)
    imagenpermostrar.image = imagenper
    imagenpermostrar.pack(pady=0)
    tk.Label(Canvaf, text="Nombre: Andrés Felipe Guerrero Cervantes", font=("Arial", 18, "bold"), bg="#B6FFFB").pack(pady=15)
    tk.Label(Canvaf, text="Carnet: 2026094459", font=("Arial", 18, "bold"), bg="#B6FFFB").pack(pady=15)
    tk.Label(Canvaf, text="Edad: 18 Años", font=("Arial", 18, "bold"), bg="#B6FFFB").pack(pady=15)
    tk.Label(Canvaf, text="Biografía: Estudiante de primer ingreso del Tecnologico de Costa Rica ", font=("Arial", 10, "bold"), bg="#B6FFFB").pack(pady=10)
    tk.Label(Canvaf, text="en la carrera de Computadores, tengo 18 años y vivo en Pérez Zeledón", font=("Arial", 10, "bold"), bg="#B6FFFB").pack(pady=10)
    tk.Button(Canvaf, text="Cerrar", command=ventanaf.destroy, bg="#f44336", fg="white", width=15).pack(pady=10)

#Grafico
def GraficoBolas(root):
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
    volver_btn = tk.Button(window, text="Cerrar Ventana", command=window.destroy, bg="#f44336", fg="white", width=15)
    volver_btn.pack(pady=10)

#Ventana principal
root = tk.Tk()
root.title("tarea-taller-grafico")
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
ButtonBall.pack(pady=10)

ButtonPers = tk.Button(root, text="Ficha Personal", command=lambda:Ficha(root))
ButtonPers.pack(pady=10)

ButtonPers = tk.Button(root, text="Musica", command=lambda:Musica(root))
ButtonPers.pack(pady=10)

ButtonNum = tk.Button(root, text="Análisis de numeros", command=lambda:NumerosPares(root))
ButtonNum.pack(pady=10)

root.mainloop()