from base.modelo_entidad import Entidad

class Reserva(Entidad):

    _nombre_entidad = "reserva"
    
    def __init__(self, fecha=None, cliente=None, empleado=None, servicio=None, estado=None, **kwargs):
        super().__init__(**kwargs)
        self.fecha = fecha
        self.cliente = cliente
        self.empleado = empleado
        self.servicio = servicio
        self.estado = estado

Reserva.agregar_columnas('fecha', 'cliente', 'empleado', 'servicio', 'estado')
