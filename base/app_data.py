import csv

base_datos = {}

def cargar(nombre_modelo):
    print(base_datos, nombre_modelo)
    print(base_datos.get(nombre_modelo))
    print("* * *")
    ## pendiente try catch si recibe objeto equivocado
    with open(base_datos.get(nombre_modelo), 'r') as data_file:
        csv_reader = csv.DictReader(data_file)
        return [el for el in csv_reader]
        ## devolver listado de diccionarios
        ## {'id': ---, 'nombre': ---}
        pass

def encontrar_campo(nombre_modelo, campo, valor):
    listado = cargar(nombre_modelo)
    for i in listado:
        if i['id'] == str(id):
            return i

def encontrar_id(nombre_modelo, id):
    return encontrar_campo(nombre_modelo, campo='id', valor=id)

def actualizar(nombre_modelo, diccionario):
    listado = cargar(nombre_modelo)
    idx = None
    for i, datos in enumerate(listado):
        if datos['id'] == diccionario['id']:
            idx = i
            break
    if idx is not None:
        listado[idx] = diccionario
    guardar(nombre_modelo, listado)

def agregar(nombre_modelo, diccionario):
    listado = cargar(nombre_modelo)
    if len(listado) > 0:
        diccionario['id'] = listado[-1] + 1
    listado.append(diccionario)
    write(nombre_modelo, listado)

def guardar(nombre_modelo, listado):
    ## pendiente try catch si recibe objeto equivocado
    with open(base_datos.get(nombre_modelo), 'w') as data_file:
        ## pendiente try catch si no puede escribir
        json.dump(listado, data_file)
  
def prueba_escritura():
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
