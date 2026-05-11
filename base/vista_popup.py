# base para los popups base de cada modulo
# utlilza tkinter
import tkinter as tk
from tkinter import ttk

# generar clase
class BasePopup():
    
    # debe recibir una referencia a la ventana base
    def __init__(self, root):
        # la guarda como propiedad
        self.root = root

    # metodo para abrir la ventana
    # debe ser ampliado por las subclases
    def abrir(self, title="No title"):
        # abrir el popup relacionarlo con la ventana raiz existente
        # y guardarlo en una propiedad de la clase
        self.popup = tk.Toplevel(self.root)
        # utilizar el título recibido
        self.popup.title(title)
        # determinar el tamaño de la ventana
        self.popup.geometry('400x600')
        # cambiar el ícono
        self.popup.iconbitmap('./assets/rocket_space_icon_185991.ico')

    def mostrar_error(self, mensaje, title="Error"):
        # abrir el popup relacionarlo con la ventana raiz existente
        # y guardarlo en una propiedad de la clase
        self.error = tk.Toplevel(self.root)
        # utilizar el título recibido
        self.error.title(title)
        # determinar el tamaño de la ventana
        self.error.geometry('300x100')
        # cambiar el ícono
        self.error.iconbitmap('./assets/rocket_space_icon_185991.ico')
        label_1 = ttk.Label(self.error, text=mensaje)
        label_1.pack(padx=20, pady=20)

        # agregar boton para cerrar
        crear_button = ttk.Button(self.error, text="Aceptar", command=lambda: self.error.destroy())
        crear_button.pack(pady=5, padx=5)

