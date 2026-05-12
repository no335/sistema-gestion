# popup principal para clientes
import tkinter as tk
from tkinter import ttk
from base.vista_popup import BasePopup

from .modelo_compra import Compra
from base.modelo_entidad import EntidadException

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
                'costo',
                'responsable',
                'aprobado',
                'comprado',
                'pagado',
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
        treeview.heading('costo',  text='costo')
        treeview.heading('responsable',  text='responsable')
        treeview.heading('aprobado',  text='aprobado')
        treeview.heading('comprado',  text='comprado')
        treeview.heading('pagado',  text='pagado')

        # configurar las columnas
        treeview.column('id',  width=50)
        treeview.column('nombre',  width=150)
        treeview.column('fecha_creacion',  width=150)
        treeview.column('costo_unidad',  width=150)
        treeview.column('costo',  width=150)
        treeview.column('responsable',  width=150)
        treeview.column('aprobado',  width=150)
        treeview.column('comprado',  width=150)
        treeview.column('pagado',  width=150)

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
        aprobar_button = ttk.Button(frame_2, text="Aprobar compra", command=lambda: self.mostrar_error("aprobar_button"))
        aprobar_button.pack(pady=5, padx=5, fill="x")
        # agregar boton para desbloquear cliente
        rechazar_button = ttk.Button(frame_2, text="Rechazar compra", command=lambda: self.mostrar_error("rechazar_button"))
        rechazar_button.pack(pady=5, padx=5, fill="x")
        # agregar boton para bloquear cliente
        factura_button = ttk.Button(frame_2, text="Cargar Factura", command=lambda: self.mostrar_error("factura_button"))
        factura_button.pack(pady=5, padx=5, fill="x")
        # agregar boton para bloquear cliente
        pago_button = ttk.Button(frame_2, text="Cargar Comprobante Pago", command=lambda: self.mostrar_error("pago_button"))
        pago_button.pack(pady=5, padx=5, fill="x")

    def abrir_formulario(self, treeview, nuevo=True):
        print("Not yet")

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
                    el.costo_unidad,
                    el.costo,
                    el.responsable,
                    'SI' if el.aprobado else '',
                    'SI' if el.comprado else '',
                    'SI' if el.pagado else '',
                )
            )
        # agregar tres filas de padding
        treeview.insert("",tk.END, values=("","","","","","","","","",))
        treeview.insert("",tk.END, values=("","","","","","","","","",))
        treeview.insert("",tk.END, values=("","","","","","","","","",))
    