# base para todos los objetos del sistema
# utiliza el app_data para leer y escribir
# en los archivos los datos generados
from base import app_data
# logger para guardar mensajes del sistema
import logging
# se crea o se obtiene una instancia de logger
# relacionada con el nombre del módulo
logger = logging.getLogger(__name__)

class EntidadException(Exception):
    pass

# define una clase
class Entidad():
    # propiedad privada de la clase
    # el campo _nombre_entidad guarda la clave en 
    # el diccionario app_data.base_datos
    _nombre_entidad = 'entidad'

    # propiedad de la clase
    # el listado de columnas se usa para
    # saber qué columnas se deben guardar en el csv
    columnas = [
        'id', 'nombre', 'fecha_creacion'
    ]
    
    # constructor -- por defecto los campos compartidos por otros
    # son id, nombre y fecha creación, puede recibir más en las subclases
    # pero se ignoran en kwargs
    def __init__(self, id=None, nombre=None, fecha_creacion=None, **kwargs):
        self.id = id
        self.nombre = nombre
        self.fecha_creacion = fecha_creacion

    # metodo de clase para generar una instancia desde un diccionario
    @classmethod
    def desde_diccionario(cls, detalle):
        """Genera una instancia utilizando el diccionario detalle"""
        ### *pendiente* MANEJO EXCEPCION cuando el diccionario tiene campos equivocados
        # generar la instancia
        obj = cls(**detalle)
        # y devolverla
        return obj
    
    # método de clase para buscar un objeto utilizando el id
    @classmethod
    def buscar(cls, id=None):
        """Busca en el archivo asociado un elemento con el id recibido
        si existe genera una instancia con ese objeto y la
        devuelve, si no devuelve none
        Si no recibe id devuelve todos los objetos del tipo en un
        list"""
        # si recibe un id buscarlo
        if id is not None:
            # buscar la fila con ese id, y obtenerla como un diccionario
            try:
                diccionario = app_data.encontrar_id(cls._nombre_entidad, id)
            except app_data.AppDataException:
                # si falla hacer un log del error y devolver un error de entidad
                logger.error(f"Entidad.buscar<{cls._nombre_entidad}>(id={id})")
                raise EntidadException("No puede leer objeto")
            if not diccionario:
                return None
            # generar una instancia a partir del diccionario
            return cls.desde_diccionario(diccionario)
        else:
            # cargar todas las filas en el archivo como un list de dict
            try:
                diccionarios = app_data.cargar(cls._nombre_entidad)
            except:
                # si falla hacer un log del error y devolver un error de entidad
                logger.error(f"Entidad.buscar<{cls._nombre_entidad}>(id={id})")
                raise EntidadException("No puede leer objeto")
            if not diccionarios:
                return
            # generar un list de instancias utilizando la sintaxis
            # compacta para generación de list
            return [cls.desde_diccionario(d) for d in diccionarios]

    # cambiar datos cliente
    def actualizar(self, diccionario):
        for el in diccionario:
            if el in self.columnas:
                setattr(self, el, diccionario[el])
            else:
                # si falla hacer un log del error y devolver un error de entidad
                logger.error(f'Entridad.actualizar: La propiedad {el} no existe en {self._nombre_entidad}')
                raise EntidadException(f"No exite la propiedad {el}")
    
    # guardar un objeto
    def guardar(self):
        """Guarda el objeto dado. Revisa si tiene un valor para id
        si lo tiene lo actualiza, si no lo agrega como nuevo"""
        # revisar si hay id
        try:
            if self.id is None:
                # agregarlo al final del archivo
                app_data.agregar(self._nombre_entidad, self.diccionario(), self.columnas)
            else:
                #si tiene id entonces reemplazarlo en la fila en que está
                app_data.actualizar(self._nombre_entidad, self.diccionario(), self.columnas)
        except app_data.AppDataException as e:
            # si falla hacer un log del error y devolver un error de entidad
            logger.error(f"Entidad.guardar<{self._nombre_entidad}>(id={id}): {e}")
            raise EntidadException("No puede escribir objeto")


    # convierte el objeto en diccionario        
    def diccionario(self):
        """Recorre todos las columnas listadas en self.columnas
        y genera un diccionario con los valores asociados a cada una"""
        # diccionario agregador
        diccionario = {}
        # iterar sobre columnas
        for col in self.columnas:
            # agregar la propiedad i-esicma como string
            if getattr(self, col):
                diccionario[col] = str(getattr(self, col))
            else:
                diccionario[col] = None
        # devolver el objeto
        return diccionario

    # metodo por defecto usado para convertir
    # el objeto a string
    def __str__(self):
        # imprime el diccionario generado 
        return f"{self._nombre_entidad}::{self.diccionario()}"