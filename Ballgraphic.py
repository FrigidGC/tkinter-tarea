#Ventana con las 2 pelotas que rebotan
import tkinter as tk

def GraficoBolas(root):
    window = tk.Toplevel(root)
    window.geometry("600x800")
    window.resizable(False, False)
    window.title("Bolas rebotando")

    canva2 = tk.Canvas(window, bg="#87CEEB", width=600, height=600)
    canva2.pack()

#Los sliders para controlar la velocidad de las bolas
    tk.Label(window, text="Velocidad X bola").pack()
    velocidadx_scale = tk.Scale(window, from_=1, to=20, orient='horizontal')
    velocidadx_scale.set(6)
    velocidadx_scale.pack()

    tk.Label(window, text="Velocidad Y bola").pack()
    velocidady_scale = tk.Scale(window, from_=1, to=20, orient='horizontal')
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
    volver_btn = tk.Button(window, text="Volver", command=window.destroy)
    volver_btn.pack(pady=10)