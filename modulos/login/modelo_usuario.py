# base para los usuarios
# utilizado por cliente y por empleado
# utlilza entidad como base
from base.modelo_entidad import Entidad
# requiere utilizar la "base de datos"
from base import app_data

# hereda de Entidad que define los campos
# compartidos por todos y los métodos de
# leer y escribir
class Usuario(Entidad):

    # agrega los campos usuario y clave e ignora el resto
    def __init__(self, usuario, clave, **kwargs):
        # llama al inicializador de la Entidad
        super().__init__(**kwargs)
        self.usuario = usuario
        self.clave = clave
        # extiende las columnas del objeto para guardado
        self.columnas.extend(['usuario', 'clave'])

    # metodo de clase para iniciar sesión
    @classmethod
    def iniciar_sesion(cls, usuario, clave):
        # busca si existe el usuario doad
        usuario = app_data.encontrar_campo(cls.nombre_modelo, 'usuario', usuario)
        if not usuario:
            # si no existe falla
            return False
        if usuario['clave'] != clave:
            # si existe pero la clave es diferente falla
            return False
        # si no tiene éxito
        return True