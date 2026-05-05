from base import app_data

class Entidad():
    nombre_modelo = 'entidad'
    columnas = [
        'id', 'nombre', 'fecha_creacion'
    ]
    
    def __init__(self, id=None, nombre=None, fecha_creacion=None, **kwargs):
        self.id = id
        self.nombre = nombre
        self.fecha_creacion = fecha_creacion

    @classmethod
    def desde_diccionario(cls, detalle):
        print(detalle)
        obj = cls(**detalle)
        return obj
    
    @classmethod
    def buscar(cls, id=None):
        if id is not None:
            diccionario = app_data.encontrar_id(cls.nombre_modelo, id)
            return cls.desde_diccionario(diccionario)
        else:
            diccionarios = app_data.cargar(cls.nombre_modelo)
            return [cls.desde_diccionario(d) for d in diccionarios]

    def guardar(self):
        if self.id is None:
            base.agregar(self.nombre_modelo, self.diccionario())
        else:
            base.actualizar(self.nombre_modelo, self.diccionario())
        
    def diccionario(self):
        diccionario = {}
        for col in self.columnas:
            diccionario[i] = getattr(col)
        return diccionario

    def __str__(self):
        return str({ c: getattr(self, c) for c in self.columnas})
