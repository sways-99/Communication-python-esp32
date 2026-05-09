import serial as srl
import keyboard
import tkinter as tk
import time 

arduino = srl.Serial("com3", 9600)
time.sleep(2)

root = tk.Tk()
root.title("COLORES")

label = tk.Label(root, text="¡Presiona un boton!")
label.pack(anchor="center")


def Azul():
        arduino.write(b"A")

def Rojo():
        arduino.write(b"R")

def Verde(): 
        arduino.write(b"V")


buttonA = tk.Button(root,text="AZUL",command=Azul)
buttonA.pack(pady=5)

buttonR = tk.Button(root,text="ROJO",command=Rojo)
buttonR.pack(pady=5)

buttonV = tk.Button(root,text="VERDE",command=Verde)
buttonV.pack(pady=5)

root.mainloop()


