# base para los popups base de cada modulo
# utlilza tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
# logger para guardar mensajes del sistema
import logging
# se crea o se obtiene una instancia de logger
# relacionada con el nombre del módulo
logger = logging.getLogger(__name__)

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
        # # abrir un popup
        messagebox.showinfo(title, mensaje)

    def cargar_formulario(self, entidad, formulario):
        """Recibe una instancia de entidad y llena el formulario con los
        valores que tiene este objeto"""
        # inicializar valores en el formulario
        # tomándolos del objeto cliente
        for propiedad, valor in entidad.diccionario().items():
            if propiedad not in formulario or  valor is None:
                continue
            if isinstance(formulario[propiedad], tk.StringVar):
                logger.debug('%s is StrVar' % propiedad)
                formulario[propiedad].set(valor)
            elif isinstance(formulario[propiedad], ttk.Combobox):
                logger.debug('%s is Combobox' % propiedad)
                formulario[propiedad].set(valor)
            elif isinstance(formulario[propiedad], tk.IntVar):
                logger.debug('%s is IntVar' % propiedad)
                try: 
                    formulario[propiedad].set(int(valor))
                except (ValueError, TypeError):
                    logger.error(f"CompraPopup.cargar_formulario: Valor Int inválido para {propiedad}")
                    formulario[propiedad].set(False)

            elif isinstance(formulario[propiedad], tk.BooleanVar):
                try:
                    formulario[propiedad].set(bool(int(valor)))
                except (ValueError, TypeError):
                    logger.error(f"CompraPopup.cargar_formulario: Valor Bool inválido para {propiedad}")
                    formulario[propiedad].set(False)


