
import tkinter as tk
#Ventana principal
root = tk.Tk()
root.title("tarea-taller-grafico")
root.geometry("800x800")
root.resizable(width=False, height=False)
import Ballgraphic
canva1 = tk.Canvas(root, bg="yellow", width=800, height=600)
canva1.pack()

ButtonBall = tk.Button(root, text="Bolas rebotando", command=lambda:Ballgraphic.GraficoBolas(root))
ButtonBall.pack()
root.mainloop()