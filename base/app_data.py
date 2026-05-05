import json

objects = {
    'clientes': 'data/clientes.json',
    'compras': 'data/compras.json',
    'empleados': 'data/empleados.json',
    'servicios': 'data/servicios.json',
    'ventas': 'data/ventas.json',
}

def read(object):
    ## pendiente try catch si recibe objeto equivocado
    with open(objects.get(object), 'r') as data_file:
        ## devolver listado de diccionarios
        ## {'id': ---, 'nombre': ---}
        pass
        

def write(object):
    ## pendiente try catch si recibe objeto equivocado
    with open(objects.get(object), 'w') as data_file:
        ## pendiente try catch si no puede escribir
        json.dump(objects, data_file)
        pass
  

def test_write():
    clientes = read('clientes')
    for i in clientes[0:3]:
        print(i)
    compras = read('compras')
    for i in clientes[0:3]:
        print(i)
    empleados = read('empleados')
    for i in empleados[0:3]:
        print(i)
    servicios = read('servicios')
    for i in servicios[0:3]:
        print(i)
    ventas = read('ventas')
    for i in ventas[0:3]:
        print(i)
