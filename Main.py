import Ballgraphic
import tkinter as tk
choque_activo=False
#Ventana principal
root = tk.Tk()
root.title("tarea-taller-grafico")
root.geometry("800x800")
root.resizable(width=False, height=False)

canva1 = tk.Canvas(root, bg="yellow", width=800, height=800)
canva1.pack()

Button1 = tk.Button(canva1, text="Bolas rebotando", command=lambda:Ballgraphic.GraficoBolas(root))
Button1.pack()
root.mainloop()