from base.modelo_entidad import Entidad

class Compra(Entidad):
    _nombre_entidad = "compra"

    def __init__(self, costo_unidad=None, cantidad=None, costo=None, responsable=None, aprobado=None, comprado=None, pagado=None, **kwargs):
        super().__init__(**kwargs)
        # definir columnas nuevas
        self.costo_unidad = costo_unidad
        self.cantidad = cantidad
        self.costo = costo
        self.responsable = responsable
        self.aprobado = aprobado
        self.comprado = comprado
        self.pagado = pagado

# Agregar columnas especificas de compra
# para escribir
Compra.columnas.extend(['costo_unidad', 'cantidad', 'costo', 'responsable', 'aprobado', 'comprado', 'pagado'])
