import tkinter as tk
from tkinter import ttk

from base.vista_popup import BasePopup
from .modelo_reserva import Reserva

from modulos.cliente.modelo_cliente import Cliente
from modulos.empleado.empleado_modelo import Empleado
from modulos.servicio.modelo_servicio import Servicio

from datetime import datetime

class ReservaPopup(BasePopup):
    
    def abrir(self):
        """Genera el popup para ver las reservas"""
        # llama a la superclase para generar la ventana
        # con titulo Cliente
        super().abrir(title="Reservas")
        self.popup.geometry('600x600')
        # genera un recuadro para meter la vista tree
        frame = ttk.Frame(self.popup)
        # genera una etiqueta para la vista tree
        label_total = ttk.Label(frame, text='Reservas')
        # la agrega al recuadro
        label_total.pack(pady=0, padx=10)
        # agrega el recuadro al popup
        frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        # definir la vista tree
        treeview = ttk.Treeview(
            frame,
            # agregar las columnas a mostrar
            columns=(
                'id',
                'nombre',
                'fecha_creacion',
                'fecha',
                'cliente',
                'empleado',
                'servicio',
                'estado',
            )
        )
        # agregar la barra de desplazamiento horizontal al tree
        tree_scrollx = ttk.Scrollbar(treeview, orient=tk.HORIZONTAL, command=treeview.xview)
        # agregar la barra de desplazamiento vertical al tree
        tree_scrolly = ttk.Scrollbar(treeview, orient=tk.VERTICAL, command=treeview.yview)
        # leer el alto de el objeto tree
        treeview['yscrollcommand'] = tree_scrolly.set
        # leer el ancho de el objeto tree
        treeview['xscrollcommand'] = tree_scrollx.set
        # ocultar columna vacía
        treeview['show'] = 'headings'
        # configurar los encabezados
        
        treeview.heading('id',  text='id')
        treeview.heading('nombre',  text='nombre')
        treeview.heading('fecha_creacion',  text='fecha_creacion')
        treeview.heading('fecha',  text='fecha')
        treeview.heading('cliente',  text='cliente')
        treeview.heading('empleado',  text='empleado')
        treeview.heading('servicio',  text='servicio')
        treeview.heading('estado',  text='estado')

        # configurar las columnas
        treeview.column('id',  width=50)
        treeview.column('nombre',  width=150)
        treeview.column('fecha_creacion',  width=150)
        treeview.column('fecha',  width=150)
        treeview.column('cliente',  width=150)
        treeview.column('empleado',  width=150)
        treeview.column('servicio',  width=150)
        treeview.column('estado',  width=150)

        # agregar la vista tree al frame
        # ocupar todo el espacio
        treeview.pack(fill=tk.BOTH, expand=True)
        # llenar la vista tree con los objetos
        # de esta vista
        self.cargar_listado(treeview)
        # agregar las barras de desplazamiento 
        # la horizontal abajo
        tree_scrollx.pack(side=tk.BOTTOM, fill=tk.X)
        # la vertical a la derecha
        tree_scrolly.pack(side=tk.RIGHT, fill=tk.Y)

        frame_1 = ttk.Frame(self.popup)
        frame_1.pack(side=tk.LEFT, padx=10)
        frame_2 = ttk.Frame(self.popup)
        frame_2.pack(side=tk.RIGHT, padx=10)

        # agregar boton para nuevo cliente
        crear_button = ttk.Button(frame_1, text="Nueva reserva", command=lambda: self.abrir_formulario(treeview, nuevo=True))
        crear_button.pack(pady=5, padx=5, fill="x")
        # agregar boton para actualizar cliente
        actualizar_button = ttk.Button(frame_1, text="Actualizar reserva", command=lambda: self.abrir_formulario(treeview, nuevo=False))
        actualizar_button.pack(pady=5, padx=5, fill="x")
        # agregar boton para bloquear cliente
        aprobar_button = ttk.Button(frame_2, text="Confirmar reserva", command=lambda: self.confirmar(treeview))
        aprobar_button.pack(pady=5, padx=5, fill="x")
        # agregar boton para desbloquear cliente
        rechazar_button = ttk.Button(frame_2, text="Cancelar reserva", command=lambda: self.cancelar(treeview))
        rechazar_button.pack(pady=5, padx=5, fill="x")
        # agregar boton para bloquear cliente
        factura_button = ttk.Button(frame_2, text="Reserva completada", command=lambda: self.completar(treeview))
        factura_button.pack(pady=5, padx=5, fill="x")
        # agregar boton para bloquear cliente
        pago_button = ttk.Button(frame_2, text="Reserva pagada", command=lambda: self.pagar(treeview))
        pago_button.pack(pady=5, padx=5, fill="x")
    
    def confirmar(self, treeview):
        reserva = self.buscar_de_treeview(treeview)
        if not reserva:
            return
        if reserva.estado != '':
            self.mostrar_error("Solo puede confirmar nuevos")
        else:
            reserva.estado = 'agendado'
            if self.guardar_cambios(reserva):
                # recargar el listado
                self.cargar_listado(treeview)
                self.mostrar_error(mensaje="Reserva Agendada", title="Éxito")
    
    def cancelar(self, treeview):
        reserva = self.buscar_de_treeview(treeview)
        if not reserva:
            return
        if reserva.estado != 'agendado':
            self.mostrar_error("Solo puede confirmar servicios agendados")
        else:
            reserva.estado = 'cancelado'
            if self.guardar_cambios(reserva):
                # recargar el listado
                self.cargar_listado(treeview)
                self.mostrar_error(mensaje="Reserva Cancelada", title="Éxito")
    
    def completar(self, treeview):
        reserva = self.buscar_de_treeview(treeview)
        if not reserva:
            return
        if reserva.estado != 'agendado':
            self.mostrar_error("Solo puede marcar como completados los serivicios agendados")
        else:
            reserva.estado = 'realizado'
            if self.guardar_cambios(reserva):
                # recargar el listado
                self.cargar_listado(treeview)
                self.mostrar_error(mensaje="Servicio Realizado", title="Éxito")
    
    def pagar(self, treeview):
        reserva = self.buscar_de_treeview(treeview)
        if not reserva:
            return
        if reserva.estado != 'realizado':
            self.mostrar_error("Solo puede marcar como pagos servicios realizados")
        else:
            reserva.estado = 'pagado'
            if self.guardar_cambios(reserva):
                # recargar el listado
                self.cargar_listado(treeview)
                self.mostrar_error(mensaje="Servicio Pagado", title="Éxito")

    def buscar_de_treeview(self, treeview):
        try:
            indice = treeview and treeview.item(treeview.focus())['values'][0]
        except IndexError:
            self.mostrar_error("Debe seleccionar una reserva")
            return
        try:
            reserva = Reserva.buscar(indice)
        except EntidadException:
            self.mostrar_error("Fallo en objeto")
        return reserva

    def guardar_cambios(self, reserva):
        try:
            reserva.guardar()
            return True
        except EntidadException:
            self.mostrar_error(mensaje="ERROR: No se pueden guardar los cambios.")
            return False

    def abrir_formulario(self, treeview, nuevo=True):
        """Muestra el popup con el formulario de reservas.
        Recibe treeview el objeto tree  y nuevo un booleano para decir si es un objeto nuevo
        o no"""
        if nuevo:
            # si es nuevo generar una nueva instancia
            reserva = Reserva()
        else:
            reserva = self.buscar_de_treeview(treeview)
        if not reserva:
            return
        # abrir el popup relacionarlo con la ventana raiz existente
        # y guardarlo en una propiedad de la clase
        self.formulario = tk.Toplevel(self.root)
        # utilizar el título recibido
        self.formulario.title("Formulario reserva")
        # determinar el tamaño de la ventana
        self.formulario.geometry('300x300')
        # cambiar el ícono
        self.formulario.iconbitmap('./assets/rocket_space_icon_185991.ico')
        # guardar las variables en un diccionario 
        formulario = {
            'nombre': tk.StringVar(),
            'fecha': tk.StringVar(),
            'cliente': None, #combobox item
            'empleado': None, #combobox item
            'servicio': None, #combobox item
            'estado': None, #combobox item
        }
        
        # campo y etiqueta para campo nombre
        label_1 = ttk.Label(self.formulario, text='Nombre')
        label_1.grid(row=0, column=0, padx=10, pady=5)
        entry_1 = ttk.Entry(self.formulario, textvariable=formulario['nombre'])
        entry_1.grid(row=0, column=1, padx=10, pady=5)
        
        # campo y etiqueta para campo costo unitario
        label_2 = ttk.Label(self.formulario, text='Fecha')
        label_2.grid(row=1, column=0, padx=10, pady=5)
        entry_2 = ttk.Entry(self.formulario, textvariable=formulario['fecha'])
        entry_2.grid(row=1, column=1, padx=10, pady=5)
        
        # campo y etiqueta para campo cliente
        label_3 = ttk.Label(self.formulario, text='Cliente')
        label_3.grid(row=2, column=0, padx=10, pady=5)
        entry_3 = ttk.Combobox(self.formulario)
        entry_3['values'] = [el.nombre for el in Cliente.buscar()]
        entry_3.grid(row=2, column=1, padx=10, pady=5)
        formulario['cliente'] = entry_3

        # campo y etiqueta para campo empleado
        label_4 = ttk.Label(self.formulario, text='Responsable')
        label_4.grid(row=3, column=0, padx=10, pady=10)
        entry_4 = ttk.Combobox(self.formulario)
        entry_4['values'] = [el.nombre for el in Empleado.buscar()]
        entry_4.grid(row=3, column=1, padx=10, pady=5)
        formulario['empleado'] = entry_4

        # campo y etiqueta para campo Servicio
        label_5 = ttk.Label(self.formulario, text='Servicio')
        label_5.grid(row=4, column=0, padx=10, pady=5)
        entry_5 = ttk.Combobox(self.formulario)
        entry_5['values'] = [el.nombre for el in Servicio.buscar()]
        entry_5.grid(row=4, column=1, padx=10, pady=5)
        formulario['servicio'] = entry_5

        # campo y etiqueta para campo estado
        label_6 = ttk.Label(self.formulario, text='Estado')
        label_6.grid(row=5, column=0, padx=10, pady=10)
        entry_6 = ttk.Combobox(self.formulario)
        entry_6['values'] = Reserva.dar_estados()
        entry_6.grid(row=5, column=1, padx=10, pady=5)
        formulario['estado'] = entry_6

        # botón guardar --- llama a self.guardar_reserva al 
        # recibir un clic
        guardar_button = ttk.Button(self.formulario, text="Guardar", command=lambda: self.guardar_reserva(reserva, formulario, treeview))
        guardar_button.grid(row=6, column=0, columnspan=2)
        # boton cancelar
        cancelar_button = ttk.Button(self.formulario, text="Cancelar", command=lambda: self.formulario.destroy())
        cancelar_button.grid(row=7, column=0, columnspan=2)
        # cargar los valores de la reserva en la vista
        self.cargar_formulario(reserva, formulario)

    def cargar_formulario(self, entidad, formulario):
        super().cargar_formulario(entidad, formulario)
        print(repr(entidad.id))
        print(repr(entidad.nombre))
        if entidad.id is None:
            formulario['nombre'].set('RES-%s' % (datetime.now().strftime('%Y/%m/%d_%H:%M')))
            formulario['fecha'].set(datetime.now().strftime('%Y/%m/%d %H:%M:%S'))

    def guardar_reserva(self, reserva, formulario, treeview):
        """Lee los valores en el formulario y los guarda en el
        objeto y luego lo guarda en el disco"""
        reserva.actualizar({
            # tomar valor del campo entry con un StringVal
            'nombre': formulario['nombre'].get(),
            # tomar valor del campo entry con un StringVal
            'fecha': formulario['fecha'].get(),
            # tomar valor del campo entry con un Combobox
            'cliente': formulario['cliente'].get(),
            # tomar valor del campo entry con un Combobox
            'empleado': formulario['empleado'].get(),
            # tomar valor del campo entry con un Combobox
            'servicio': formulario['servicio'].get(),
            # tomar valor del campo entry con un Combobox
            'estado': formulario['estado'].get(),
        })
        try:
            reserva.guardar()
            # recargar el listado
            self.cargar_listado(treeview)
            # cerrar ventana de formulario
            self.formulario.destroy()
        except EntidadException:
            self.mostrar_error(mensaje="ERROR: No se pueden guardar los cambios.")
 
    def cargar_listado(self, treeview):
        """Recarga el listado a mostrar en la vista de clientes.
        Recibe la vista tree en donde se muestran
        """
        # primero quitar todos los objetos de la vista
        # recorrer los hijos (filas) uno por uno
        for i in treeview.get_children():
            # remover la fila dada
            treeview.delete(i)
        # cargar los clientes del archivo
        try:
            reserva = Reserva.buscar()
        except EntidadException:
            self.mostrar_error(mensaje="Error: No hay datos para este módulo")
            reserva = None
        if not reserva:
            return
        # iterar sobre el listado de reserva
        for el in reserva:
            # generar una fila en la vista tree
            treeview.insert(
                "",
                tk.END,
                values=(
                    el.id,
                    el.nombre,
                    el.fecha_creacion,
                    el.fecha,
                    el.cliente,
                    el.empleado,
                    el.servicio,
                    el.estado,
                )
            )
        # agregar tres filas de padding
        treeview.insert("",tk.END, values=("","","","","","","","","",))
        treeview.insert("",tk.END, values=("","","","","","","","","",))
        treeview.insert("",tk.END, values=("","","","","","","","","",))
    