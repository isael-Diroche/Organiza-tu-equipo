import tkinter as tk
from tkinter import *
from tkinter import messagebox
import os
from funciones import documentos, descargas, telegram, escritorio
font = ["Lucida Console", "Comfortaa SemiBold", "DM Sans Medium", "DM Sans Bold"]

# ================================================================================================== #
# pyinstaller --windowed --onefile --icon=./img/icono.ico main.py
# ================================================================================================== #
class UI(tk.Frame):
    def __init__(self, parent=None):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        ventana = self.parent
        # Fondo del programa
        Label(self.parent, image=fondo).place(x=-2, y=-2)

        # Configuraciones de la ventana
        ventana.title("Organizador automatico 0.1")
        # ventana.configure(bg=color_fondo)

        Label(self.parent,
              text="Archivos",
              font=(font[2], 10),
              cursor='hand2',
              bg="#293139",
              fg="#FFFFFF",
              ).place(x=23, y=6)

        Label(self.parent,
              text="Ayuda",
              font=(font[2], 10),
              cursor='hand2',
              bg="#293139",
              fg="#A9A9A9"
              ).place(x=90, y=6)

        Label(self.parent,
              text="Configuracion",
              font=(font[2], 10),
              cursor='hand2',
              bg="#293139",
              fg="#A9A9A9"
              ).place(x=143, y=6)

        # Boton para orgnizar las descargas
        Button(self.parent,
               text='Descargas',
               font=(font[1], 11),
               bd=0,
               fg="#FFFFFF",
               bg="#293139",
               activebackground="#293139",
               activeforeground="#767676",
               cursor='hand2',
               command=lambda: descargas()
               ).place(x=105, y=256)

        # Boton para orgnizar el Escritorio
        Button(self.parent,
               text='Escritorio',
               font=(font[1], 11),
               bd=0,
               fg="#FFFFFF",
               bg="#293139",
               activebackground="#293139",
               activeforeground="#767676",
               cursor='hand2',
               command=lambda: escritorio()
               ).place(x=110, y=304)

        # Boton para orgnizar los Documentos
        Button(self.parent,
               text='Documentos',
               font=(font[1], 11),
               bd=0,
               fg="#FFFFFF",
               bg="#293139",
               activebackground="#293139",
               activeforeground="#767676",
               cursor='hand2',
               command=lambda: documentos()
               ).place(x=100, y=351)

        # Boton para orgnizar la carpeta de Telegram
        Button(self.parent,
               text='Telegram',
               font=(font[1], 11),
               bd=0,
               fg="#FFFFFF",
               bg="#293139",
               activebackground="#293139",
               activeforeground="#767676",
               cursor='hand2',
               command=lambda: telegram()
               ).place(x=110, y=399)

        # Boton para cerrar el programa
        Button(self.parent,
               text='Salir',
               font=(font[3], 8),
               bd=0,
               fg="#E0DEFF",
               bg="#C14343",
               activebackground="#C14343",
               activeforeground="#303030",
               cursor='hand2',
               command=lambda: ventana.destroy()
               ).place(x=250, y=476)

        """Checkbutton(self.parent,
                    onvalue=1,
                    offvalue=0,
                    bd=0,
                    bg="#303943",
                    fg="#303943",
                    activebackground = "#303943",
                    activeforeground = "#303943",
                    highlightbackground= "#303943",
                    highlightcolor= "#303943",
                    offrelief=GROOVE,
                    overrelief=GROOVE,
                    state=ACTIVE
                    ).place(x=114, y=369)"""

    def move_window(self, event):
        ventana = self.parent
        ventana.geometry(f"+{event.x_root}+{event.y_root}")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x500")
    root.resizable(False, False)
    # root.attributes("-alpha", 0.5)
    fondo = PhotoImage(file="./media/images/background2.png")

    app = UI(parent=root)
    app.bind('<B1-Motion>', app.move_window)
    app.bind('<B1-Motion>', app.move_window)
    app.mainloop()