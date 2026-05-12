from base.modelo_entidad import Entidad

class Servicio(Entidad):
    _nombre_entidad = "servicio"
    
    def __init__(self, descripcion=None, costo=None, responsable=None, activo=None, **kwargs):
        super().__init__(kwargs)
        self.descripcion = descripcion
        self.costo = costo
        self.responsable = responsable
        self.activo = activo

Servicio.agregar_columnas('descripcion', 'costo', 'responsable', 'activo')
