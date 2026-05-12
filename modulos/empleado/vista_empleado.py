# popup principal para clientes
import tkinter as tk
from tkinter import ttk
from base.vista_popup import BasePopup
from .empleado_modelo import Empleado
from base.modelo_entidad import EntidadException

# logger para guardar mensajes del sistema
import logging
# se crea o se obtiene una instancia de logger
# relacionada con el nombre del módulo
logger = logging.getLogger(__name__)

class EmpleadoPopup(BasePopup):
    
    def abrir(self):
        """Genera el popup para ver los empleados"""
        # llama a la superclase para generar la ventana
        # con titulo Cliente
        super().abrir(title="Empleado")
        self.popup.geometry('600x600')
        # genera un recuadro para meter la vista tree
        frame = ttk.Frame(self.popup)
        # genera una etiqueta para la vista tree
        label_total = ttk.Label(frame, text='Empleados')
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
                'usuario',
                'tipo',
                'jefe_inmediato',
                'bloqueado',
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
        treeview.heading('usuario',  text='usuario')
        treeview.heading('tipo',  text='tipo')
        treeview.heading('jefe_inmediato',  text='jefe_inmediato')
        treeview.heading('bloqueado',  text='bloqueado')

        # configurar las columnas
        treeview.column('id',  width=50)
        treeview.column('nombre',  width=150)
        treeview.column('fecha_creacion',  width=150)
        treeview.column('usuario',  width=150)
        treeview.column('tipo',  width=150)
        treeview.column('jefe_inmediato',  width=150)
        treeview.column('bloqueado',  width=150)

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
        crear_button = ttk.Button(frame_1, text="Nuevo empleado", command=lambda: self.abrir_formulario(treeview, nuevo=True))
        crear_button.pack(pady=5, padx=5, fill="x")
        # agregar boton para actualizar cliente
        actualizar_button = ttk.Button(frame_1, text="Actualizar empleado", command=lambda: self.abrir_formulario(treeview, nuevo=False))
        actualizar_button.pack(pady=5, padx=5, fill="x")
        # agregar boton para bloquear cliente
        clave_button = ttk.Button(frame_2, text="Cambiar contraseña", command=lambda: self.mostrar_error("Se envió correo de cambio de contraseña", title="Cambio clave"))
        clave_button.pack(pady=5, padx=5, fill="x")
        # agregar boton para desbloquear cliente
        desactivar_button = ttk.Button(frame_2, text="Desactivar", command=lambda: self.desactivar(treeview))
        desactivar_button.pack(pady=5, padx=5, fill="x")
        # agregar boton para bloquear cliente
        activar_button = ttk.Button(frame_2, text="Reactivar", command=lambda: self.reactivar(treeview))
        activar_button.pack(pady=5, padx=5, fill="x")
        # agregar boton para bloquear cliente
    
    def buscar_de_treeview(self, treeview):
        try:
            indice = treeview and treeview.item(treeview.focus())['values'][0]
        except IndexError:
            self.mostrar_error("Debe seleccionar una empleado")
            return
        try:
            empleado = Empleado.buscar(indice)
        except EntidadException:
            self.mostrar_error("Fallo en objeto")
        return empleado

    def guardar_cambios(self, empleado):
        try:
            empleado.guardar()
            return True
        except EntidadException:
            self.mostrar_error(mensaje="ERROR: No se pueden guardar los cambios.")
            return False

    def desactivar(self, treeview):
        empleado = self.buscar_de_treeview(treeview)
        if not empleado:
            return
        if empleado.bloqueado:
            self.mostrar_error("Solo puede bloquear usuarios activos")
        else:
            empleado.bloqueado = 1
            self.mostrar_error(mensaje="Empleado Desactivado", title="Éxito")
            if self.guardar_cambios(empleado):
                # recargar el listado
                self.cargar_listado(treeview)
                # cerrar ventana de formulario
                self.formulario.destroy()
        
    def reactivar(self, treeview):
        empleado = self.buscar_de_treeview(treeview)
        if not empleado:
            return
        print(empleado)
        if not empleado.bloqueado:
            self.mostrar_error("Solo puede activar bloqueados")
        else:
            empleado.bloqueado = 0
            if self.guardar_cambios(empleado):
                # recargar el listado
                self.cargar_listado(treeview)
                self.mostrar_error(mensaje="Empleado Activado", title="Éxito")

    def abrir_formulario(self, treeview, nuevo=True):
        """Muestra el popup con el formulario de compras.
        Recibe treeview el objeto tree  y nuevo un booleano para decir si es un objeto nuevo
        o no"""
        if nuevo:
            # si es nuevo generar una nueva instancia
            empleado = Empleado()
        else:
            try:
                indice = treeview and treeview.item(treeview.focus())['values'][0]
            except IndexError:
                self.mostrar_error("Debe seleccionar una empleado")
                return
            #si no es nuevo revisar qué 
            # 1 - esta seleccionado
            # 2 - tiene el id definido en la primera columna la 0
            # buscar el cliente con ese id
            try:
                empleado = Empleado.buscar(indice)
            except EntidadException:
                empleado = None
        if not empleado:
            self.mostrar_error(mensaje="ERROR: No se puede editar empleado")
            return
        # abrir el popup relacionarlo con la ventana raiz existente
        # y guardarlo en una propiedad de la clase
        self.formulario = tk.Toplevel(self.root)
        # utilizar el título recibido
        self.formulario.title("Formulario Empleado")
        # determinar el tamaño de la ventana
        self.formulario.geometry('300x300')
        # cambiar el ícono
        self.formulario.iconbitmap('./assets/rocket_space_icon_185991.ico')
        # guardar las variables en un diccionario 
        formulario = {
            'nombre': tk.StringVar(),
            'usuario': tk.StringVar(),
            'tipo': None, #combobox item,
            'jefe_inmediato': None, #combobox item
            'bloqueado': tk.BooleanVar(),
        }
        
        # campo y etiqueta para campo nombre
        label_1 = ttk.Label(self.formulario, text='Nombre')
        label_1.grid(row=0, column=0, padx=10, pady=5)
        entry_1 = ttk.Entry(self.formulario, textvariable=formulario['nombre'])
        entry_1.grid(row=0, column=1, padx=10, pady=5)
        
        # campo y etiqueta para campo costo usuario
        label_2 = ttk.Label(self.formulario, text='Usuario')
        label_2.grid(row=1, column=0, padx=10, pady=5)
        entry_2 = ttk.Entry(self.formulario, textvariable=formulario['usuario'])
        entry_2.grid(row=1, column=1, padx=10, pady=5)

        # campo y etiqueta para campo tipo
        label_3 = ttk.Label(self.formulario, text='Tipo')
        label_3.grid(row=2, column=0, padx=10, pady=5)
        entry_3 = ttk.Combobox(self.formulario)
        entry_3['values'] = Empleado.ver_tipos()
        entry_3.grid(row=2, column=1, padx=10, pady=5)
        formulario['tipo'] = entry_3

        # campo y etiqueta para campo comprado
        label_4 = ttk.Label(self.formulario, text='Jefe Inmediato')
        label_4.grid(row=3, column=0, padx=10, pady=10)
        entry_4 = ttk.Combobox(self.formulario)
        entry_4['values'] = [el.nombre for el in Empleado.buscar()]
        entry_4.grid(row=3, column=1, padx=10, pady=5)
        formulario['jefe_inmediato'] = entry_4

        # campo y etiqueta para campo bloqueado
        label_5 = ttk.Label(self.formulario, text='Bloqueado')
        label_5.grid(row=4, column=0, padx=10, pady=10)
        entry_5 = ttk.Checkbutton(self.formulario, variable=formulario['bloqueado'])
        entry_5.grid(row=4, column=1, padx=10, pady=10)

        # botón guardar --- llama a self.guardar_empleado al 
        # recibir un clic
        guardar_button = ttk.Button(self.formulario, text="Guardar", command=lambda: self.guardar_empleado(empleado, formulario, treeview))
        guardar_button.grid(row=5, column=0, columnspan=2)
        # boton cancelar
        cancelar_button = ttk.Button(self.formulario, text="Cancelar", command=lambda: self.formulario.destroy())
        cancelar_button.grid(row=6, column=0, columnspan=2)
        # cargar los valores de la empleado en la vista
        self.cargar_formulario(empleado, formulario)

    def guardar_empleado(self, empleado, formulario, treeview):
        """Lee los valores en el formulario y los guarda en el
        objeto y luego lo guarda en el disco"""
        empleado.actualizar({
            # tomar valor del campo entry con un StringVal
            'nombre': formulario['nombre'].get(),
            # tomar valor del campo entry con un IntVal
            'usuario': formulario['usuario'].get(),
            # tomar valor del campo entry con un IntVal
            'tipo': formulario['tipo'].get(),
            # tomar valor del campo entry con un IntVal
            'jefe_inmediato': formulario['jefe_inmediato'].get(),
            # tomar valor del campo entry con un Combobox
            'bloqueado': formulario['bloqueado'].get(),
        })
        if self.guardar_cambios(empleado):
            # recargar el listado
            self.cargar_listado(treeview)
            self.formulario.destroy()

    def cargar_listado(self, treeview):
        """Recarga el listado a mostrar en la vista de empleados.
        Recibe la vista tree en donde se muestran
        """
        # primero quitar todos los objetos de la vista
        # recorrer los hijos (filas) uno por uno
        for i in treeview.get_children():
            # remover la fila dada
            treeview.delete(i)
        # cargar los empleados del archivo
        try:
            empleados = Empleado.buscar()
        except EntidadException:
            self.mostrar_error(mensaje="Error: No hay datos para este módulo")
            empleados = None
        if not empleados:
            return
        # iterar sobre el listado de empleados
        for el in empleados:
            # generar una fila en la vista tree
            treeview.insert(
                "",
                tk.END,
                values=(
                    el.id,
                    el.nombre,
                    el.fecha_creacion,
                    el.usuario,
                    el.tipo,
                    el.jefe_inmediato if el.jefe_inmediato else '',
                    'SI' if el.bloqueado else 'NO',
                )
            )
        # agregar tres filas de padding
        treeview.insert("",tk.END, values=("","","","","","","","","",))
        treeview.insert("",tk.END, values=("","","","","","","","","",))
        treeview.insert("",tk.END, values=("","","","","","","","","",))
    

