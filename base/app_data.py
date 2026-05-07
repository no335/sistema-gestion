# este modulo se encarga de manejar los datos
# utiliza la librería csv para leer archivos
# en formarto csv (comma separated values o valores separados por coma)
import csv
# usar la librería de fechas para la fecha de creacion
from datetime import datetime

# tiene un diccionario principal para guardar la localización de cada
# tipo de objeto.
# la clave es el tipo de objeto y el valor es la ruta del archivo
base_datos = {}

# cargar los datos de un modelo dado
def cargar(nombre_modelo):
    """
    Recibe el nombre del modelo ('cliente', 'usuario')
    y devuelve los datos que están en el archivo asociado en 
    el diccionario base_datos"""
    ## **pendiente** MANEJO EXCEPCION si recibe objeto equivocado
    # abrir el archivo para lectura
    with open(base_datos.get(nombre_modelo), 'r') as data_file:
        # utilizar la librería csv para cargar el archivo
        # como un list de diccionarios de python
        csv_reader = csv.DictReader(data_file)
        # poner todos los objetos en un list 
        # utilizando la sintaxis para la generación 
        # de un list a partir de un iterable
        ## devolver list de diccionarios
        ## [{'id': ---, 'nombre': ---}, {...}, ...]
        return [el for el in csv_reader]
        pass

# encontrar un objeto en particular de un modelo dado
def encontrar_campo(nombre_modelo, campo, valor):
    """Devuelve un diccionario {'id': ..., 'nombre': ...} 
    con el primer objeto en el archivo asociado a ese nombre_modelo ('cliente', 'usuario', ...)
    que tenga el valor recibido en el campo dado
    -Supone que todos los valores son str-
    """
    ## **pendiente** MANEJO EXCEPCION si el campo dado no existe
    ## en eltipo de objeto dado

    # carga los objetos un list
    diccionarios = cargar(nombre_modelo)
    # itera en el list
    for i in diccionarios:
        # revisa el campo
        if i[campo] == str(valor):
            return i

# encontrar objeto por id
def encontrar_id(nombre_modelo, id):
    """Similar a encontrar_campo en este caso busca
    el objeto por el valor en el campo id"""
    return encontrar_campo(nombre_modelo, campo='id', valor=id)

# actualizar un objeto existente
def actualizar(nombre_modelo, diccionario, columnas):
    """Escribe los cambios realizados en un objeto 
    dado en el archivo asociado.
    Recibe el nombre del modelo"""
    # carga un diccionarios de diccionarios
    diccionarios = cargar(nombre_modelo)
    idx = None
    # itera sobre los objetos enumerados con i
    for i, datos in enumerate(diccionarios):
        # si encuentra uno con el id en el diccionario recibido guarda 
        # el indice asociado
        if datos['id'] == diccionario['id']:
            idx = i
            # salir del for
            break
    # si encontró un objeto con ese id
    if idx is not None:
        # reemplaza el valor en el diccionario dado
        diccionarios[idx] = diccionario
    # escribe el list en el archivo dado
    guardar(nombre_modelo, diccionarios, columnas)

# crear un nuevo objeto
def agregar(nombre_modelo, diccionario, columnas):
    """Escribe en el disco los cambios a un archivo asociado
    a un modelo dado, agregando el diccionario dado"""
    # carga el lsit de objetos del disco
    diccionarios = cargar(nombre_modelo)
    # busca el último id registrado para 
    # agregar uno diferente
    # --supone que los ids estan ordenados
    if len(diccionarios) > 0:
        diccionario['id'] = int(diccionarios[-1]['id']) + 1
        diccionario['fecha_creacion'] = datetime.now().isoformat()
    else:
        # si no hay nada empieza a contar en 1
        diccionario['id'] = 1
    # agrega el objeto al diccionario
    diccionarios.append(diccionario)
    # escribe en el disco
    guardar(nombre_modelo, diccionarios, columnas)

# escribir los diccionarios recibidos en el disco
def guardar(nombre_modelo, listado, columnas):
    """Escribe en el archivo asociado a nombre_modelo en 
    base_datos el listado recibido de diccionarios"""
    
    ## pendiente MANEJO EXCEPCION si recibe objeto equivocado
    with open(base_datos.get(nombre_modelo), 'w') as data_file:
        ## pendiente MANEJO EXCEPCION si no puede escribir
        # utilizar el escritor de diccionarios en la librería csv
        # enviar el archivo para escribir, las columnas para escribir y 
        # el terminador de línea para evitar saltos dobles
        csv_writer = csv.DictWriter(data_file, fieldnames=columnas, lineterminator="\n")
        # generar titulos de columna
        csv_writer.writeheader()
        # iterar sobre el listado
        for row in listado:
            # escribir la fila
            csv_writer.writerow(row)
  
# prueba lectura
def prueba_lectura():
    clientes = cargar('clientes')
    for i in clientes[0:3]:
        print(i)
    compras = cargar('compras')
    for i in clientes[0:3]:
        print(i)
    empleados = cargar('empleados')
    for i in empleados[0:3]:
        print(i)
    servicios = cargar('servicios')
    for i in servicios[0:3]:
        print(i)
    ventas = cargar('ventas')
    for i in ventas[0:3]:
        print(i)

