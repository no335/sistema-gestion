# popup principal para login
import tkinter as tk
from tkinter import ttk
from base.vista_popup import BasePopup
from .modelo_usuario import Usuario

class LoginPopup(BasePopup):
    contrasena_var = None
    usuario_var = None
    mensaje = None

    def abrir(self):
        super().abrir(title="Login")
        self.popup.geometry('260x260')
        # variable para contrasena
        LoginPopup.contrasena_var = tk.StringVar()
        # variable para usuarui
        LoginPopup.usuario_var = tk.StringVar()
        # etiqueta para mensaje
        LoginPopup.mensaje = ttk.Label(self.popup, text='')
        # etiqueta 1
        ttk.Label(self.popup, text='User login').grid(padx=10, pady=10, column=0, row=0)
        # etiqueta 2
        ttk.Label(self.popup, text='User').grid(padx=10, pady=10, column=0, row=1)
        # entrada texto
        usuario = ttk.Entry(self.popup, textvariable=LoginPopup.usuario_var)
        usuario.grid(padx=10, pady=10, column=1, row=1)
        # etiuqueta 3
        ttk.Label(self.popup, text='Password').grid(padx=10, pady=10, column=0, row=2)
        # entrada texto
        contrasena = ttk.Entry(self.popup, show='*', textvariable=LoginPopup.contrasena_var)
        contrasena.grid(padx=10, pady=10, column=1, row=2)
        # mensaje
        LoginPopup.mensaje.config(text="")
        LoginPopup.mensaje.grid(padx=0, pady=0, column=1, row=3)
        # boton ingresar
        button_a = ttk.Button(self.popup, text="Login", command=self.iniciar_sesion)
        button_a.grid(padx=5, pady=5, column=1, row=4)
        # boton salir
        button_b = ttk.Button(self.popup, text="Exit", command=lambda: self.popup.destroy())
        button_b.grid(padx=5, pady=5, column=1, row=5)

    def iniciar_sesion(self):
        validar = Usuario.iniciar_sesion(
            LoginPopup.usuario_var.get(),
            LoginPopup.contrasena_var.get()
        )
        if validar:
            # iniciar sesion
            LoginPopup.mensaje.config(text="Logging in")
            LoginPopup.root.destroy()
            self.popup.destroy()
            pass
        else:
            # mostrar error
            LoginPopup.mensaje.config(text="User or password not valid")
            pass
