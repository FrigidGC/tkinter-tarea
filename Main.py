import tkinter as tk
ventana = tk.Tk()
ventana.title("tarea-taller-grafico")
ventana.geometry("800x800")
ventana.resizable(width=false, height=false)

canva1 = tk.Canvas(ventana, bg="yellow", width=800, height=800)
canva1.pack()

ventana.mainloop()