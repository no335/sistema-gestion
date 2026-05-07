# popup principal para clientes
import tkinter as tk
from tkinter import ttk
from base.vista_popup import BasePopup
# utliliza objetos de tipo cliente
from .modelo_cliente import Cliente

# hereda de BasePopup
# que define el método abrir y el constructor
class ClientePopup(BasePopup):
    
    # metodo para abrir el popup
    def abrir(self):
        """Genera el popup para ver los clientes"""
        # llama a la superclase para generar la ventana
        # con titulo Cliente
        super().abrir(title="Cliente")
        self.popup.geometry('600x600')
        # genera un recuadro para meter la vista tree
        frame = ttk.Frame(self.popup)
        # genera una etiqueta para la vista tree
        label_total = ttk.Label(frame, text='Clientes')
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
                'direccion',
                'telefono',
                'tipo',
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
        treeview.heading('direccion',  text='direccion')
        treeview.heading('telefono',  text='telefono')
        treeview.heading('tipo',  text='tipo')
        treeview.heading('bloqueado',  text='bloqueado')
        # configurar las columnas
        treeview.column('id',  width=50)
        treeview.column('nombre',  width=150)
        treeview.column('fecha_creacion',  width=150)
        treeview.column('usuario',  width=150)
        treeview.column('direccion',  width=150)
        treeview.column('telefono',  width=150)
        treeview.column('tipo',  width=150)
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

        # agregar boton para nuevo cliente
        crear_button = ttk.Button(self.popup, text="Nuevo cliente", command=lambda: self.abrir_formulario(treeview, nuevo=True))
        crear_button.pack(pady=5, padx=5)
        # agregar boton para actualizar cliente
        actualizar_button = ttk.Button(self.popup, text="Actualizar cliente", command=lambda: self.abrir_formulario(treeview, nuevo=False))
        actualizar_button.pack(pady=5, padx=5)
        # agregar boton para bloquear cliente
        bloquear_button = ttk.Button(self.popup, text="Bloquear cliente", command=lambda: self.bloquear(treeview))
        bloquear_button.pack(pady=5, padx=5)
        # agregar boton para desbloquear cliente
        desbloquear_button = ttk.Button(self.popup, text="Desbloquear cliente", command=lambda: self.desbloquear(treeview))
        desbloquear_button.pack(pady=5, padx=5)
    
    def bloquear(self, treeview):
        """Cambia el estado de bloqueado de un cliente a 1"""
        # si recibe el objeto tree y tiene una selección
        if treeview and treeview.focus():
            # si es una fila con el id definido
            if treeview.item(treeview.focus())['values'][0] != '':
                # buscar el objeto por el id en la primera columna (la 0)
                cliente_obj = Cliente.buscar(treeview.item(treeview.focus())['values'][0])
                # cambiar el valor de bloquado
                cliente_obj.bloqueado = 1
                # guardar los cambios
                cliente_obj.guardar()
                # recargar la vista tree
                self.cargar_listado(treeview)

    def desbloquear(self, treeview):
        """Cambia el estado de bloqueado de un cliente a 0"""
        # si recibe el objeto tree y tiene una selección
        if treeview and treeview.focus():
            # si es una fila con el id definido
            if treeview.item(treeview.focus())['values'][0] != '':
                # buscar el objeto por el id en la primera columna (la 0)
                cliente_obj = Cliente.buscar(treeview.item(treeview.focus())['values'][0])
                # cambiar el valor de bloquado
                cliente_obj.bloqueado = 0
                # guardar los cambios
                cliente_obj.guardar()
                # recargar la vista tree
                self.cargar_listado(treeview)

    def abrir_formulario(self, treeview=None, nuevo=False):
        """Muestra el popup con el formulario de cliente.
        Recibe treeview el objeto tree  y nuevo un booleano para decir si es un objeto nuevo
        o no"""
        if nuevo:
            # si es nuevo generar una nueva instancia
            cliente = Cliente()
        elif treeview and treeview.item(treeview.focus())['values'][0] != '':
            #si no es nuevo revisar qué 
            # 1 - esta seleccionado
            # 2 - tiene el id definido en la primera columna la 0
            # buscar el cliente con ese id
            cliente = Cliente.buscar(treeview.item(treeview.focus())['values'][0])
        else:
            # si no no hacer nada
            return
        # abrir el popup relacionarlo con la ventana raiz existente
        # y guardarlo en una propiedad de la clase
        self.formulario = tk.Toplevel(self.root)
        # utilizar el título recibido
        self.formulario.title("Formulario Cliente")
        # determinar el tamaño de la ventana
        self.formulario.geometry('300x300')
        # cambiar el ícono
        self.formulario.iconbitmap('./assets/rocket_space_icon_185991.ico')
        # guardar las variables en un diccionario 
        formulario = {
            'nombre': tk.StringVar(),
            'usuario': tk.StringVar(),
            'telefono': tk.StringVar(),
            'direccion': tk.StringVar(),
            'bloqueado': tk.BooleanVar(),
        }    
        
        # campo y etiqueta para campo nombre
        label_1 = ttk.Label(self.formulario, text='Nombre')
        label_1.grid(row=0, column=0, padx=10, pady=5)
        entry_1 = ttk.Entry(self.formulario, textvariable=formulario['nombre'])
        entry_1.grid(row=0, column=1, padx=10, pady=5)
        
        # campo y etiqueta para campo usuario
        label_2 = ttk.Label(self.formulario, text='Usuario')
        label_2.grid(row=1, column=0, padx=10, pady=5)
        entry_2 = ttk.Entry(self.formulario, textvariable=formulario['usuario'])
        entry_2.grid(row=1, column=1, padx=10, pady=5)
        
        # campo y etiqueta para campo telefono
        label_3 = ttk.Label(self.formulario, text='Teléfono')
        label_3.grid(row=2, column=0, padx=10, pady=5)
        entry_3 = ttk.Entry(self.formulario, textvariable=formulario['telefono'])
        entry_3.grid(row=2, column=1, padx=10, pady=5)
        
        # campo y etiqueta para campo direccion
        label_4 = ttk.Label(self.formulario, text='Dirección')
        label_4.grid(row=3, column=0, padx=10, pady=5)
        entry_4 = ttk.Entry(self.formulario, textvariable=formulario['direccion'])
        entry_4.grid(row=3, column=1, padx=10, pady=5)

        # campo y etiqueta para campo tipo
        label_5 = ttk.Label(self.formulario, text='Tipo')
        label_5.grid(row=4, column=0, padx=10, pady=5)
        entry_5 = ttk.Combobox(self.formulario)
        entry_5['values'] = ['persona', 'empresa']
        entry_5.grid(row=4, column=1, padx=10, pady=5)
        formulario['tipo'] = entry_5

        # campo y etiqueta para campo bloqueado
        label_6 = ttk.Label(self.formulario, text='Bloqueado')
        label_6.grid(row=5, column=0, padx=10, pady=10)
        entry_6 = ttk.Checkbutton(self.formulario, variable=formulario['bloqueado'])
        entry_6.grid(row=5, column=1, padx=10, pady=10)

        # botón guardar --- llama a self.guardar_cliente al 
        # recibir un clic
        guardar_button = ttk.Button(self.formulario, text="Guardar", command=lambda: self.guardar_cliente(cliente, formulario, treeview))
        guardar_button.grid(row=6, column=0, columnspan=2)
        # boton cancelar
        cancelar_button = ttk.Button(self.formulario, text="Cancelar", command=lambda: self.formulario.destroy())
        cancelar_button.grid(row=7, column=0, columnspan=2)
        
        # inicializar valores en el formulario
        # tomándolos del objeto cliente
        if cliente.nombre:
            formulario['nombre'].set(cliente.nombre)
        if cliente.usuario:
            formulario['usuario'].set(cliente.usuario)
        if cliente.telefono:
            formulario['telefono'].set(cliente.telefono)
        if cliente.direccion:
            formulario['direccion'].set(cliente.direccion)
        if cliente.tipo:
            formulario['tipo'].set(cliente.tipo)
        formulario['bloqueado'].set(cliente.bloqueado)

    def guardar_cliente(self, cliente, formulario, treeview):
        """Lee los valores en el formulario y los guarda en el
        objeto y luego lo guarda en el disco"""
        # tomar valor del campo entry con un StringVal
        cliente.nombre = formulario['nombre'].get()
        # tomar valor del campo entry con un StringVal
        cliente.usuario = formulario['usuario'].get()
        # tomar valor del campo entry con un StringVal
        cliente.telefono = formulario['telefono'].get()
        # tomar valor del campo entry con un StringVal
        cliente.direccion = formulario['direccion'].get()
        # tomar valor del campo combobox 
        cliente.tipo = formulario['tipo'].get()
        # tomar valor del campo checkbox 1 si está lleno y 0 si está vacío
        cliente.bloqueado = 1 if formulario['bloqueado'].get() else 0
        # escribir en el disco
        cliente.guardar()
        # recargar el listado
        self.cargar_listado(treeview)
        # cerrar ventana de formulario
        self.formulario.destroy()

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
        clientes = Cliente.buscar()
        # iterar sobre el listado de clientes
        for el in clientes:
            # generar una fila en la vista tree
            treeview.insert(
                "",
                tk.END,
                values=(
                    el.id,
                    el.nombre,
                    # muestra los valores formateados con 0 o 2 decimales según el tipo
                    el.fecha_creacion,
                    el.usuario,
                    el.direccion,
                    el.telefono,
                    el.tipo,
                    # Mostrar el texto bloqueado si el cliente está bloqueado o - si no
                    'Bloqueado' if el.bloqueado else '-',
                )
            )
        # agregar tres filas de padding
        treeview.insert("",tk.END, values=("","","","","","","","","",))
        treeview.insert("",tk.END, values=("","","","","","","","","",))
        treeview.insert("",tk.END, values=("","","","","","","","","",))
        
