# popup principal para clientes
import tkinter as tk
from tkinter import ttk
from base.vista_popup import BasePopup
from .modelo_compra import Compra
from modulos.empleado.empleado_modelo import Empleado
from base.modelo_entidad import EntidadException
# logger para guardar mensajes del sistema
import logging
# se crea o se obtiene una instancia de logger
# relacionada con el nombre del módulo
logger = logging.getLogger(__name__)


class CompraPopup(BasePopup):

    def abrir(self):
        """Genera el popup para ver lascompras"""
        # llama a la superclase para generar la ventana
        # con titulo Cliente
        super().abrir(title="Compra")
        self.popup.geometry('600x600')
        # genera un recuadro para meter la vista tree
        frame = ttk.Frame(self.popup)
        # genera una etiqueta para la vista tree
        label_total = ttk.Label(frame, text='Compras')
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
                'costo_unidad',
                'cantidad',
                'costo',
                'responsable',
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
        treeview.heading('costo_unidad',  text='costo_unidad')
        treeview.heading('cantidad',  text='cantidad')
        treeview.heading('costo',  text='costo')
        treeview.heading('responsable',  text='responsable')
        treeview.heading('estado',  text='estado')

        # configurar las columnas
        treeview.column('id',  width=50)
        treeview.column('nombre',  width=150)
        treeview.column('fecha_creacion',  width=150)
        treeview.column('cantidad',  width=150, anchor=tk.E)
        treeview.column('costo_unidad',  width=150, anchor=tk.E)
        treeview.column('costo',  width=150, anchor=tk.E)
        treeview.column('responsable',  width=150)
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
        crear_button = ttk.Button(frame_1, text="Nueva compra", command=lambda: self.abrir_formulario(treeview, nuevo=True))
        crear_button.pack(pady=5, padx=5, fill="x")
        # agregar boton para actualizar cliente
        actualizar_button = ttk.Button(frame_1, text="Actualizar compra", command=lambda: self.abrir_formulario(treeview, nuevo=False))
        actualizar_button.pack(pady=5, padx=5, fill="x")
        # agregar boton para bloquear cliente
        aprobar_button = ttk.Button(frame_2, text="Aprobar compra", command=lambda: self.aprobar(treeview))
        aprobar_button.pack(pady=5, padx=5, fill="x")
        # agregar boton para desbloquear cliente
        rechazar_button = ttk.Button(frame_2, text="Rechazar compra", command=lambda: self.rechazar(treeview))
        rechazar_button.pack(pady=5, padx=5, fill="x")
        # agregar boton para bloquear cliente
        factura_button = ttk.Button(frame_2, text="Cargar Factura", command=lambda: self.cargar_factura(treeview))
        factura_button.pack(pady=5, padx=5, fill="x")
        # agregar boton para bloquear cliente
        pago_button = ttk.Button(frame_2, text="Cargar Comprobante Pago", command=lambda: self.pagar(treeview))
        pago_button.pack(pady=5, padx=5, fill="x")
    
    def buscar_de_treeview(self, treeview):
        try:
            indice = treeview and treeview.item(treeview.focus())['values'][0]
        except IndexError:
            self.mostrar_error("Debe seleccionar una compra")
            return
        try:
            compra = Compra.buscar(indice)
        except EntidadException:
            self.mostrar_error("Fallo en objeto")
        return compra
    
    def guardar_cambios(self, compra):
        try:
            compra.guardar()
            return True
        except EntidadException:
            self.mostrar_error(mensaje="ERROR: No se pueden guardar los cambios.")
            return False

    def aprobar(self, treeview):
        compra = self.buscar_de_treeview(treeview)
        if not compra:
            return
        if compra.estado != '':
            self.mostrar_error("Solo puede aprobar compras nuevas")
        else:
            compra.estado = 'aprobado'
            self.mostrar_error(mensaje="Pedido Aprobado", title="Éxito")
            if self.guardar_cambios(compra):
                # recargar el listado
                self.cargar_listado(treeview)
                # cerrar ventana de formulario
                self.formulario.destroy()
        
    def rechazar(self, treeview):
        compra = self.buscar_de_treeview(treeview)
        if not compra:
            return
        print(compra)
        if compra.estado != 'aprobado':
            self.mostrar_error("Solo puede rechazar compras aprobadas")
        else:
            compra.estado = 'rechazado'
            if self.guardar_cambios(compra):
                # recargar el listado
                self.cargar_listado(treeview)
                self.mostrar_error(mensaje="Compra Rechazada", title="Éxito")

    def cargar_factura(self, treeview):
        compra = self.buscar_de_treeview(treeview)
        if not compra:
            return
        if compra.estado != 'aprobado':
            self.mostrar_error("Solo puede facturar compras aprobadas")
        else:
            compra.estado = 'pedido'
            if self.guardar_cambios(compra):
                # recargar el listado
                self.cargar_listado(treeview)
                self.mostrar_error(mensaje="Pedido Realizado", title="Éxito")

    def pagar(self, treeview):
        compra = self.buscar_de_treeview(treeview)
        if not compra:
            return
        if compra.estado != 'pedido':
            self.mostrar_error("Solo puede pagar compras en estado 'pedido'")
        else:
            compra.estado = 'pagado'
            if self.guardar_cambios(compra):
                # recargar el listado
                self.cargar_listado(treeview)
                self.mostrar_error(mensaje="Compra pagada", title="Éxito")

    def abrir_formulario(self, treeview, nuevo=True):
        """Muestra el popup con el formulario de compras.
        Recibe treeview el objeto tree  y nuevo un booleano para decir si es un objeto nuevo
        o no"""
        if nuevo:
            # si es nuevo generar una nueva instancia
            compra = Compra()
        else:
            try:
                indice = treeview and treeview.item(treeview.focus())['values'][0]
            except IndexError:
                self.mostrar_error("Debe seleccionar una compra")
                return
            #si no es nuevo revisar qué 
            # 1 - esta seleccionado
            # 2 - tiene el id definido en la primera columna la 0
            # buscar el cliente con ese id
            try:
                compra = Compra.buscar(indice)
            except EntidadException:
                compra = None
        if not compra:
            self.mostrar_error(mensaje="ERROR: No se puede editar compra")
            return
        # abrir el popup relacionarlo con la ventana raiz existente
        # y guardarlo en una propiedad de la clase
        self.formulario = tk.Toplevel(self.root)
        # utilizar el título recibido
        self.formulario.title("Formulario Compra")
        # determinar el tamaño de la ventana
        self.formulario.geometry('300x300')
        # cambiar el ícono
        self.formulario.iconbitmap('./assets/rocket_space_icon_185991.ico')
        # guardar las variables en un diccionario 
        formulario = {
            'nombre': tk.StringVar(),
            'costo_unidad': tk.IntVar(),
            'cantidad': tk.IntVar(),
            'costo': tk.IntVar(),
            'responsable': None, #combobox item
            'estado': None # combobox item
        }
        
        # campo y etiqueta para campo nombre
        label_1 = ttk.Label(self.formulario, text='Nombre')
        label_1.grid(row=0, column=0, padx=10, pady=5)
        entry_1 = ttk.Entry(self.formulario, textvariable=formulario['nombre'])
        entry_1.grid(row=0, column=1, padx=10, pady=5)
        
        # campo y etiqueta para campo costo unitario
        label_2 = ttk.Label(self.formulario, text='Costo unidad')
        label_2.grid(row=1, column=0, padx=10, pady=5)
        entry_2 = ttk.Entry(self.formulario, textvariable=formulario['costo_unidad'])
        entry_2.grid(row=1, column=1, padx=10, pady=5)
        
        # campo y etiqueta para campo cantidad
        label_3 = ttk.Label(self.formulario, text='Cantidad')
        label_3.grid(row=2, column=0, padx=10, pady=5)
        entry_3 = ttk.Entry(self.formulario, textvariable=formulario['cantidad'])
        entry_3.grid(row=2, column=1, padx=10, pady=5)
        
        # campo y etiqueta para campo costo total
        label_4 = ttk.Label(self.formulario, text='Costo Total')
        label_4.grid(row=3, column=0, padx=10, pady=5)
        entry_4 = ttk.Entry(self.formulario, textvariable=formulario['costo'])
        entry_4.grid(row=3, column=1, padx=10, pady=5)
        entry_4.config(state="disabled")

        # campo y etiqueta para campo tipo
        label_5 = ttk.Label(self.formulario, text='Responable')
        label_5.grid(row=4, column=0, padx=10, pady=5)
        entry_5 = ttk.Combobox(self.formulario)
        entry_5['values'] = [el.nombre for el in Empleado.buscar()]
        entry_5.grid(row=4, column=1, padx=10, pady=5)
        formulario['responsable'] = entry_5

        # campo y etiqueta para campo comprado
        label_6 = ttk.Label(self.formulario, text='Estado')
        label_6.grid(row=5, column=0, padx=10, pady=10)
        entry_6 = ttk.Combobox(self.formulario)
        entry_6['values'] = ['aprobado', 'rechazado', 'pedido', 'recibido', 'pagado']
        entry_6.grid(row=5, column=1, padx=10, pady=5)
        formulario['estado'] = entry_6

        # botón guardar --- llama a self.guardar_compra al 
        # recibir un clic
        guardar_button = ttk.Button(self.formulario, text="Guardar", command=lambda: self.guardar_compra(compra, formulario, treeview))
        guardar_button.grid(row=6, column=0, columnspan=2)
        # boton cancelar
        cancelar_button = ttk.Button(self.formulario, text="Cancelar", command=lambda: self.formulario.destroy())
        cancelar_button.grid(row=7, column=0, columnspan=2)
        # cargar los valores de la compra en la vista
        self.cargar_formulario(compra, formulario)
        
        def actualizar_total(*args):
            try:
                formulario['costo'].set(str(int(entry_2.get()) * int(entry_3.get())))
            except ValueError:
                formulario['costo'].set('-')
        formulario['costo_unidad'].trace_add('write', actualizar_total)
        formulario['cantidad'].trace_add('write', actualizar_total)


    def guardar_compra(self, compra, formulario, treeview):
        """Lee los valores en el formulario y los guarda en el
        objeto y luego lo guarda en el disco"""
        compra.actualizar({
            # tomar valor del campo entry con un StringVal
            'nombre': formulario['nombre'].get(),
            # tomar valor del campo entry con un IntVal
            'costo_unidad': formulario['costo_unidad'].get(),
            # tomar valor del campo entry con un IntVal
            'cantidad': formulario['cantidad'].get(),
            # tomar valor del campo entry con un IntVal
            'costo': formulario['costo'].get(),
            # tomar valor del campo entry con un Combobox
            'responsable': formulario['responsable'].get(),
            # tomar valor del campo entry con un Combobox
            'estado': formulario['estado'].get(),
        })
        try:
            compra.guardar()
            # recargar el listado
            self.cargar_listado(treeview)
            # cerrar ventana de formulario
            self.formulario.destroy()
        except EntidadException:
            self.mostrar_error(mensaje="ERROR: No se pueden guardar los cambios.")
        
    def cargar_formulario(self, entidad, formulario):
        """Recibe una instancia de entidad y llena el formulario con los
        valores que tiene este objeto"""
        super().cargar_formulario(entidad, formulario) 

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
            compras = Compra.buscar()
        except EntidadException:
            self.mostrar_error(mensaje="Error: No hay datos para este módulo")
            compras = None
        if not compras:
            return
        # iterar sobre el listado de compras
        for el in compras:
            # generar una fila en la vista tree

            treeview.insert(
                "",
                tk.END,
                values=(
                    el.id,
                    el.nombre,
                    el.fecha_creacion,
                    f'$ {int(el.costo_unidad):,.0f}' if el.costo_unidad else '',
                    f'{int(el.cantidad):,.0f}' if el.cantidad else '',
                    f'$ {int(el.costo):,.0f}' if el.costo else '',
                    el.responsable,
                    el.estado,
                )
            )
        # agregar tres filas de padding
        treeview.insert("",tk.END, values=("","","","","","","","","",))
        treeview.insert("",tk.END, values=("","","","","","","","","",))
        treeview.insert("",tk.END, values=("","","","","","","","","",))
    