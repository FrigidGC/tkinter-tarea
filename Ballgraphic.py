#Ventana con las 2 pelotas que rebotan
import tkinter as tk

#Ventana del grafico
xspeed1 = 6
xspeed2 = 5
yspeed1 = 4
yspeed2= 3
choque_activo=False
def GraficoBolas(root):
    window= tk.Toplevel(root)
    window.geometry("600x600")
    window.resizable(width=False, height=False)
    window.title("Bolas rebotando")
    canva2 = tk.Canvas(window, bg="#87CEEB", width=600, height=600)
    canva2.pack()
#Las bolas
    Ball = canva2.create_oval(300, 250, 380, 330, fill="yellow")
    Ball2 = canva2.create_oval(100, 50, 180, 130, fill="red")

#Detectar Colisión
    def Collision():
        global xspeed1, yspeed1, xspeed2, yspeed2
        xspeed1, xspeed2 = xspeed2, xspeed1
        yspeed1, yspeed2 = yspeed2, yspeed1

#                if yspeed1 == yspeed2: #ambos van al mismo rumbo
                #no cambian de rumbo en Y
#                    xspeed1 = - xspeed1
#                    xspeed2 = - xspeed2
#                else:
#                    yspeed1 = -yspeed1
#                    yspeed2 = -yspeed2
#                    xspeed1 = -xspeed1
#                    xspeed2 = -xspeed2
#                if xspeed1 == xspeed2:
                #No cambian de rumbo en X
#                    yspeed2 = -yspeed2
#                    yspeed1 = -yspeed1
#                else:
#                    xspeed1 = -xspeed1
#                    xspeed2 = -xspeed2
#                    yspeed1 = -yspeed1
#                    yspeed2 = -yspeed2

#Movimiento de las bolas
    def moveball():
        global choque_activo
        global xspeed1, yspeed1, xspeed2, yspeed2
        canva2.move(Ball,xspeed1,yspeed1)
        (left1, top1, right1, bottom1) = canva2.coords(Ball)
        if left1 <= 0 or right1 >= 600:
            xspeed1 = -xspeed1
        if  top1 <= 0 or bottom1 >= 600:
            yspeed1 = -yspeed1

        canva2.move(Ball2,xspeed2,yspeed2)
        (left2, top2, right2, bottom2) = canva2.coords(Ball2)
        if left2 <= 0 or right2 >= 600:
            xspeed2 = -xspeed2
        if  top2 <= 0 or bottom2 >= 600:
            yspeed2 = -yspeed2
        canva2.after(10, moveball)

#Colisión
        if not (
                right1 < left2 or   # bola1 está a la izquierda
                left1 > right2 or   # bola1 está a la derecha
                bottom1 < top2 or   # bola1 está arriba
                top1 > bottom2      # bola1 está abajo
                ):
            choque=True
        else:
            choque=False
            choque_activo=False
        if choque and not choque_activo:
            Collision()
            choque_activo=True
    canva2.after(10, moveball)