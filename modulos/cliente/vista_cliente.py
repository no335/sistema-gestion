# popup principal para clientes
import tkinter as tk
from tkinter import ttk
from base.vista_popup import BasePopup
# utliliza objetos de tipo cliente
from .modelo_cliente import Cliente

# hereda de BasePopup
# que define el método abrir y el constructor
class ClientePopup(BasePopup):
    
    # metodo para abrir el popup
    def abrir(self):
        # llama a la superclase para generar la ventana
        # con titulo Cliente
        super().abrir(title="Cliente")
