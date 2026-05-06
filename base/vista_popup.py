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

