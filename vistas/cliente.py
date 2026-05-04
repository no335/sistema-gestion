from base_popup import BasePopup
import tkinter as tk
from tkinter import ttk

class ClientePopup(BasePopup):
    
    def abrir(self):
        super().abrir(title="Cliente")
