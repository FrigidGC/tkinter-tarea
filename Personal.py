#Ventana que con ficha personal del programador que reproduce musica
import tkinter as tk
import pygame

def Ficha(root):
    # Inicializar el mixer de pygame
    pygame.mixer.init()

    #Control de música
    def play_music():
        pygame.mixer.music.play()

    def pause_music():
        pygame.mixer.music.pause()

    def unpause_music():
        pygame.mixer.music.unpause()

    def stop_music():
        pygame.mixer.music.stop()

    # Cargar música
    pygame.mixer.music.load("who-can-it-be-now.mp3")

    # Ventana
    ventanap = tk.Toplevel(root)
    ventanap.title("Ficha Personal")
    ventanap.geometry("500x700")
    ventanap.resizable(False, False)

    #canvas
    CMusic = tk.Canvas(ventanap, width=500, height=700)
    CMusic.pack()

    # Botones, label e imagen
    imagen = tk.PhotoImage(file="Men_At_Work.png") 
    imagenmostrar = tk.Label(CMusic, image=imagen)
    imagenmostrar.pack(pady=10)

    tk.Label(CMusic, text="Género musical: Pop Rock", font=("Arial", 16)).pack(pady=20)
    tk.Button(CMusic, text="Play", width=10, command=play_music).pack(pady=10)
    tk.Button(CMusic, text="Pause", width=10, command=pause_music).pack(pady=10)
    tk.Button(CMusic, text="Unpause", width=10, command=unpause_music).pack(pady=10)
    tk.Button(CMusic, text="Stop", width=10, command=stop_music).pack(pady=10)

    ventanap.mainloop()

