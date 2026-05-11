# Este es el punto de entrada de toda la aplicación
# se requeren los modulos de tkinter para generar la 
# interfaz grárfica
import tkinter as tk
from tkinter import ttk

# Se requieren los módulos de cada una de las secciones de
# la aplicación
from modulos.cliente.vista_cliente import ClientePopup
from modulos.compra.vista_compra import CompraPopup
from modulos.empleado.vista_empleado import EmpleadoPopup
from modulos.login.vista_login import LoginPopup
from modulos.servicio.vista_servicio import ServicioPopup
from modulos.reserva.vista_reserva import ReservaPopup

def pruebas_cliente():
    from modulos.cliente.pruebas_cliente import prueba_creacion, prueba_actualizacion, prueba_creacion_error, prueba_actualizacion_error
    prueba_creacion()
    prueba_creacion_error()
    prueba_actualizacion()
    prueba_actualizacion_error()

# Generar la ventana base
root = tk.Tk()
# definir el tamaño de la ventana
root.geometry('300x230')
# evitar que cambie de tamaño vertical y horizontalmente
root.resizable(False, False)
# poner el título
root.title('Sistema de servicios')
# ajustar el ícono
root.iconbitmap('./assets/rocket_space_icon_185991.ico')

# generar una caja para agregarle contenido
frame = ttk.Frame(root)
# hacer que quede en la primera columna del 
# sistema de cuadrícula de tkinter
frame.columnconfigure(0, weight=1)
# agregarlo como parte de la cuadrícula
frame.grid(column=0, row=0)

# generar un área contenedora de gráficos en el frame anterior
canvas = tk.Canvas(frame, width=199, height=199, bg='white')
# agregarla
canvas.pack(side=tk.LEFT)
# cargar una imagen de los assets
python_image = tk.PhotoImage(file='assets/robot.png')
# "imprimir" la imagen en el area de gráficos
canvas.create_image(
    (100, 100),
    image=python_image
)

# funcion para abrir un popup dado
# recibe la clase y la ventana base
def abrir_popup(clase_popup, root):
    # genera una instancia
    popup = clase_popup(root)
    # llama al metodo abrir
    popup.abrir()

#genera un segunda caja 
frame2 = ttk.Frame(root)
# la agrega a la cuadrícula de tkinter en una
# segunda columna
frame2.grid(column=1, row=0)
# generar un botón Login al recuadro 2
popup_login = ttk.Button(
    frame2,
    text='Login',
    # al hacer clic llamar el abrir popup con la clase para login
    command=lambda: abrir_popup(LoginPopup, root)
)
# agregar el botón Loginal recuadro 2
# utilizando el apilamiento
popup_login.pack(
    ipadx=5, # espaciamiento horizontal
    ipady=5, # espaciamiento vertical
    expand=True # ampliar para ocupar todo el area
)

# generar un botón Clientes al recuadro 2
popup_cliente = ttk.Button(
    frame2,
    text='Clientes',
    # al hacer clic llamar el abrir popup con la clase para cliente
    command=lambda: abrir_popup(ClientePopup, root)
)
# agregar el botón Clientes al recuadro 2
# utilizando el apilamiento
popup_cliente.pack(
    ipadx=5, # espaciamiento horizontal
    ipady=5, # espaciamiento vertical
    expand=True # ampliar para ocupar todo el area
)

# generar un botón Compras al recuadro 2
popup_compra = ttk.Button(
    frame2,
    text='Compras',
    # al hacer clic llamar el abrir popup con la clase para compras
    command=lambda: abrir_popup(CompraPopup, root)
)
# agregar el botón Compras al recuadro 2
# utilizando el apilamiento
popup_compra.pack(
    ipadx=5, # espaciamiento horizontal
    ipady=5, # espaciamiento vertical
    expand=True # ampliar para ocupar todo el area
)

# generar un botón Empleados al recuadro 2
popup_empleado = ttk.Button(
    frame2,
    text='Empleados',
    # al hacer clic llamar el abrir popup con la clase para empleados
    command=lambda: abrir_popup(EmpleadoPopup, root)
)
# agregar el botón Empleados al recuadro 2
# utilizando el apilamiento
popup_empleado.pack(
    ipadx=5, # espaciamiento horizontal
    ipady=5, # espaciamiento vertical
    expand=True # ampliar para ocupar todo el area
)

# generar un botón  al recuadro 2
popup_servicio = ttk.Button(
    frame2,
    text='Servicios',
    # al hacer clic llamar el abrir popup con la clase para servicio
    command=lambda: abrir_popup(ServicioPopup, root)
)
# agregar el botón Servicios al recuadro 2
# utilizando el apilamiento
popup_servicio.pack(
    ipadx=5, # espaciamiento horizontal
    ipady=5, # espaciamiento vertical
    expand=True # ampliar para ocupar todo el area
)

# generar un botón Ventas al recuadro 2
popup_reserva = ttk.Button(
    frame2,
    text='Reservas',
    # al hacer clic llamar el abrir popup con la clase para venta
    command=lambda: abrir_popup(VentaPopup, root)
)
# agregar el botón Ventas al recuadro 2
# utilizando el apilamiento
popup_reserva.pack(
    ipadx=5, # espaciamiento horizontal
    ipady=5, # espaciamiento vertical
    expand=True # ampliar para ocupar todo el area
)

# abrir ventana prinicipal
root.mainloop()