import tkinter as tk
from tkinter import ttk
from base.vista_popup import BasePopup
from .modelo_servicio import Servicio

class ServicioPopup(BasePopup):
    
    def abrir(self):
        """Genera el popup para ver los s"""
        super().abrir(title="Servicio")
        self.popup.geometry('600x600')
        # genera un recuadro para meter la vista tree
        frame = ttk.Frame(self.popup)
        # genera una etiqueta para la vista tree
        label_total = ttk.Label(frame, text='Servicios')
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
                'descripcion',
                'costo',
                'responsable',
                'activo',
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
        treeview.heading('descripcion',  text='descripcion')
        treeview.heading('costo',  text='costo')
        treeview.heading('responsable',  text='responsable')
        treeview.heading('activo',  text='activo')

        # configurar las columnas
        treeview.column('id',  width=50)
        treeview.column('nombre',  width=150)
        treeview.column('fecha_creacion',  width=150)
        treeview.column('descripcion',  width=150)
        treeview.column('costo',  width=150)
        treeview.column('responsable',  width=150)
        treeview.column('activo',  width=150)

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
        frame_1.pack(side=tk.BOTTOM, pady=5)
        frame_2 = ttk.Frame(self.popup)
        frame_2.pack(side=tk.BOTTOM, pady=5)

        # agregar boton para nuevo cliente
        crear_button = ttk.Button(frame_1, text="Nuevo servicio", command=lambda: self.abrir_formulario(treeview, nuevo=True))
        crear_button.pack(pady=5, padx=5, fill="x")
        # agregar boton para actualizar cliente
        actualizar_button = ttk.Button(frame_1, text="Actualizar servicio", command=lambda: self.abrir_formulario(treeview, nuevo=False))
        actualizar_button.pack(pady=5, padx=5, fill="x")
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
            self.mostrar_error("Debe seleccionar un servicio")
            return

        try:
            servicio = Servicio.buscar(indice)
        except Exception:
            servicio = None

        if not servicio:
            self.mostrar_error(mensaje="ERROR: No se puede editar servicio")
            return

        return servicio
                
    def buscar_de_treeview(self, treeview):
        try:
            indice = treeview and treeview.item(treeview.focus())['values'][0]
        except IndexError:
            self.mostrar_error("Debe seleccionar un servicio")
            return

        try:
            servicio = Servicio.buscar(indice)
        except Exception:
            servicio = None

        if not servicio:
            self.mostrar_error(mensaje="ERROR: No se puede editar servicio")
            return

        return servicio

    def guardar_cambios(self, servicio):
        try:
            servicio.guardar()
            return True
        except Exception:
            self.mostrar_error(mensaje="ERROR: No se pueden guardar los cambios.")
            return False

    def desactivar(self, treeview):
        servicio = self.buscar_de_treeview(treeview)

        if not servicio:
            return

        if servicio.activo is False:
            self.mostrar_error("El servicio ya está desactivado")
        else:
            servicio.activo = False

            if self.guardar_cambios(servicio):
                self.cargar_listado(treeview)
                self.mostrar_error(mensaje="Servicio desactivado", title="Éxito")

    def reactivar(self, treeview):
        servicio = self.buscar_de_treeview(treeview)

        if not servicio:
            return

        if servicio.activo is True:
            self.mostrar_error("El servicio ya está activo")
        else:
            servicio.activo = True

            if self.guardar_cambios(servicio):
                self.cargar_listado(treeview)
                self.mostrar_error(mensaje="Servicio reactivado", title="Éxito")

    def abrir_formulario(self, treeview, nuevo=True):

        if nuevo:
            servicio = Servicio()
        else:
            try:
                indice = treeview and treeview.item(treeview.focus())['values'][0]
            except IndexError:
                self.mostrar_error("Debe seleccionar un servicio")
                return

            try:
                servicio = Servicio.buscar(indice)
            except Exception:
                servicio = None

        if not servicio:
            self.mostrar_error(mensaje="ERROR: No se puede editar servicio")
            return

        self.formulario = tk.Toplevel(self.root)

        self.formulario.title("Formulario Servicio")

        self.formulario.geometry('300x300')

        formulario = {
            'nombre': tk.StringVar(),
            'descripcion': tk.StringVar(),
            'costo': tk.IntVar(),
            'responsable': tk.StringVar(),
            'activo': tk.BooleanVar()
        }

        label_1 = ttk.Label(self.formulario, text='Nombre')
        label_1.grid(row=0, column=0, padx=10, pady=5)
        entry_1 = ttk.Entry(self.formulario, textvariable=formulario['nombre'])
        entry_1.grid(row=0, column=1, padx=10, pady=5)

        label_2 = ttk.Label(self.formulario, text='Descripción')
        label_2.grid(row=1, column=0, padx=10, pady=5)
        entry_2 = ttk.Entry(self.formulario, textvariable=formulario['descripcion'])
        entry_2.grid(row=1, column=1, padx=10, pady=5)

        label_3 = ttk.Label(self.formulario, text='Costo')
        label_3.grid(row=2, column=0, padx=10, pady=5)
        entry_3 = ttk.Entry(self.formulario, textvariable=formulario['costo'])
        entry_3.grid(row=2, column=1, padx=10, pady=5)

        label_4 = ttk.Label(self.formulario, text='Responsable')
        label_4.grid(row=3, column=0, padx=10, pady=5)
        entry_4 = ttk.Entry(self.formulario, textvariable=formulario['responsable'])
        entry_4.grid(row=3, column=1, padx=10, pady=5)

        guardar_button = ttk.Button(
            self.formulario,
            text="Guardar",
            command=lambda: self.guardar_servicio(servicio, formulario, treeview)
        )
        guardar_button.grid(row=5, column=0, columnspan=2)

        cancelar_button = ttk.Button(
            self.formulario,
            text="Cancelar",
            command=lambda: self.formulario.destroy()
        )
        cancelar_button.grid(row=6, column=0, columnspan=2)

        self.cargar_formulario(servicio, formulario)

    def guardar_servicio(self, servicio, formulario, treeview):

        servicio.actualizar({
            'nombre': formulario['nombre'].get(),
            'descripcion': formulario['descripcion'].get(),
            'costo': formulario['costo'].get(),
            'responsable': formulario['responsable'].get(),
        })

        try:
            servicio.guardar()

            self.cargar_listado(treeview)

            self.formulario.destroy()

        except Exception:
            self.mostrar_error(mensaje="ERROR: No se pueden guardar los cambios.")

    def cargar_formulario(self, entidad, formulario):

        super().cargar_formulario(entidad, formulario)

    def cargar_listado(self, treeview):

        for i in treeview.get_children():
            treeview.delete(i)

        try:
            servicios = Servicio.buscar()
        except Exception:
            self.mostrar_error(mensaje="Error: No hay datos para este módulo")
            servicios = None

        if not servicios:
            return

        for el in servicios:

            treeview.insert(
                "",
                tk.END,
                values=(
                    el.id,
                    el.nombre,
                    el.fecha_creacion,
                    el.descripcion,
                    f'$ {int(el.costo):,.0f}' if el.costo else '',
                    el.responsable,
                    el.activo,
                )
            )

        treeview.insert("", tk.END, values=("", "", "", "", "", "", ""))
        treeview.insert("", tk.END, values=("", "", "", "", "", "", ""))
        treeview.insert("", tk.END, values=("", "", "", "", "", "", ""))
