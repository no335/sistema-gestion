from base.modelo_entidad import Entidad
from base import app_data

class Usuario(Entidad):

    def __init__(self, usuario, clave, **kwargs):
        super().__init__(**kwargs)
        self.usuario = usuario
        self.clave = clave

        self.columnas.extend(['usuario', 'clave'])

    @classmethod
    def iniciar_sesion(cls, usuario, clave):
        usuario = app_data.encontrar_campo(cls.nombre_modelo, 'usuario', usuario)
        if not usuario:
            return False
        if usuario['clave'] != clave:
            return False
        return True