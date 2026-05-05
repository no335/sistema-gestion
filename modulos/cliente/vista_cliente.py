import tkinter as tk
from tkinter import ttk
from base.vista_popup import BasePopup

class ClientePopup(BasePopup):
    
    def abrir(self):
        super().abrir(title="Cliente")
