class EntidadBase():
    
    def __int__(self, id, nombre, fecha_creacion):
        self.id = id
        self.nombre = nombre
        self.fecha_creacion = fecha_creacion
        pass

    def desde_diccionario(dict):
        obj = EntidadBase(**dict)
        return obj