import tkinter as tk
from tkinter import ttk

class BasePopup():
    
    def __init__(self, root):
        self.root = root

    def abrir(self, title="No title"):
        self.popup = tk.Toplevel(self.root)
        self.popup.title(title)
        self.popup.geometry('400x600')
