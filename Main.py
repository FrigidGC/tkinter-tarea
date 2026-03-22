import tkinter as tk
from Ballgraphic import GraficoBolas
#Ventana principal
root = tk.Tk()
root.title("tarea-taller-grafico")
root.geometry("800x800")
root.resizable(width=False, height=False)

canva1 = tk.Canvas(root, bg="yellow", width=800, height=800)
canva1.pack()

root.mainloop()