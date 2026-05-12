from ..login.modelo_usuario import Usuario

class Empleado(Usuario):
    
    def __init__(self, tipo=None, jefe_inmediato=None, bloqueado=None, **kwargs):
        super().__init__(**kwargs)
        self.tipo = tipo
        self.jefe_inmediato = jefe_inmediato
        self.bloqueado = bloqueado

Empleado.agregar_columnas('tipo', 'jefe_inmediato', 'bloqueado')
