from base.modelo_entidad import Entidad

class Compra(Entidad):
    _nombre_entidad = "compra"

    def __init__(self, costo_unidad=None, cantidad=None, costo=None, responsable=None, estado=None, **kwargs):
        super().__init__(**kwargs)
        # definir columnas nuevas
        self.costo_unidad = costo_unidad
        self.cantidad = cantidad
        self.costo = costo
        self.responsable = responsable
        self.estado = estado

# Agregar columnas especificas de compra
# para escribir

Compra.columnas = Entidad.columnas[:]
Compra.columnas.extend(['costo_unidad', 'cantidad', 'costo', 'responsable', 'estado'])
