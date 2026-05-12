from ..login.modelo_usuario import Usuario

class Cliente(Usuario):
    _nombre_entidad = 'cliente'

    def __init__(self, direccion=None, telefono=None, bloqueado=None, tipo=None, **kwargs):
        # definir columnas nuevas
        self.direccion = direccion
        self.telefono = telefono
        self.bloqueado = bloqueado
        self.tipo = tipo

        super().__init__(**kwargs)

Cliente.agregar_columnas('direccion', 'telefono', 'bloqueado', 'tipo')
