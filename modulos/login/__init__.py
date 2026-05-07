# este es el modulo de login
# se llama antes que todos

# llama al módulo para los datos
from base.app_data import base_datos
# agrega la ruta para el archivo de datos de
# este módulo
base_datos['usuario'] = 'modulos/login/usuarios.csv'
