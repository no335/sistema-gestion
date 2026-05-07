from ..login.modelo_usuario import Usuario

class Cliente(Usuario):
    nombre_modelo = 'cliente'

    def __init__(self, direccion=None, telefono=None, bloqueado=None, tipo=None, **kwargs):
        # definir columnas nuevas
        self.direccion = direccion
        self.telefono = telefono
        self.bloqueado = bloqueado
        self.tipo = tipo

        super().__init__(**kwargs)

# Agregar columnas especificas de clietne
# para escribir
Cliente.columnas.extend(['direccion', 'telefono', 'bloqueado', 'tipo'])