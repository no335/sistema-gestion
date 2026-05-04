import tkinter as tk
from tkinter import ttk
from cliente import ClientePopup
from compra import CompraPopup
from empleado import EmpleadoPopup
from login import LoginPopup
from servicio import ServicioPopup
from venta import VentaPopup


root = tk.Tk()
root.geometry('300x230')
root.resizable(False, False)
root.title('Sistema de servicios')
root.iconbitmap('./assets/rocket_space_icon_185991.ico')

frame = ttk.Frame(root)
frame.columnconfigure(0, weight=1)

frame.grid(column=0, row=0)

canvas = tk.Canvas(frame, width=199, height=199, bg='white')
canvas.pack(side=tk.LEFT)

python_image = tk.PhotoImage(file='assets/robot.png')
canvas.create_image(
    (100, 100),
    image=python_image
)


def abrir_popup(clase_popup, root):
    popup = clase_popup(root)
    popup.abrir()

frame2 = ttk.Frame(root)
# frame2.columnconfigure(1, weight=1)
frame2.grid(column=1, row=0)

popup_cliente = ttk.Button(
    frame2,
    text='Clientes',
    command=lambda: abrir_popup(ClientePopup, root)
)
popup_cliente.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

popup_compra = ttk.Button(
    frame2,
    text='Compras',
    command=lambda: abrir_popup(CompraPopup, root)
)
popup_compra.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

popup_empleado = ttk.Button(
    frame2,
    text='Empleado',
    command=lambda: abrir_popup(EmpleadoPopup, root)
)
popup_empleado.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

popup_login = ttk.Button(
    frame2,
    text='Login',
    command=lambda: abrir_popup(LoginPopup, root)
)
popup_login.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

popup_servicio = ttk.Button(
    frame2,
    text='Servicios',
    command=lambda: abrir_popup(ServicioPopup, root)
)
popup_servicio.pack(
    ipadx=5,
    ipady=5,
    expand=True
)


popup_venta = ttk.Button(
    frame2,
    text='Ventas',
    command=lambda: abrir_popup(VentaPopup, root)
)
popup_venta.pack(
    ipadx=5,
    ipady=5,
    expand=True
)
root.mainloop()