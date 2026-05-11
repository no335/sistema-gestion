from .modelo_cliente import Cliente

def prueba_actualizar_cliente(diccionario):
    cliente = Cliente.buscar(diccionario['id'])
    cliente.actualizar(diccionario)

def prueba_creacion_error():
    cliente = Cliente.desde_diccionario({
        'nombre': 'new client',
        'usuario': '@usuario',
        'contraseña': 'uno dos tres',
        'fecha_creacion': '2025-01-01T12:22:22',
        'direccion': 'KR 123 CL 123-123', 
        'telefono': '123123123',
        'bloqueado': False,
        'tipo': 'nuevo',
    })
    temp = Cliente._nombre_entidad
    Cliente._nombre_entidad = 'abcd'
    print("----Prueba creación [mala configuracion]")
    try:
        cliente.guardar()
        print("Creación exitosa")
    except Exception as e:
        print("Hubo un error al guardar:", e)
    finally:
        Cliente._nombre_entidad = temp


def prueba_creacion():
    cliente = Cliente.desde_diccionario({
        'nombre': 'new client',
        'usuario': '@usuario',
        'clave': 'uno dos tres',
        'fecha_creacion': '2025-01-01T12:22:22',
        'direccion': 'KR 123 CL 123-123', 
        'telefono': '123123123',
        'bloqueado': False,
        'tipo': 'nuevo',
    })
    print("----Prueba creación")
    try:
        cliente.guardar()
        print("Creación exitosa")
    except Exception as e:
        print("Hubo un error al guardar:", e)

def prueba_actualizacion():
    clientes = Cliente.buscar()
    cliente = clientes[-1]
    cliente.nombre = 'NEW CLIENT'
    print("----Prueba actualización")
    try:
        cliente.guardar()
        print("Actualizacion exitosa")
    except Exception as e:
        print("Hubo un error en la actualización: ", e)

def prueba_actualizacion_error():
    clientes = Cliente.buscar()
    cliente = clientes[-1]
    print("----Prueba actualización [Mala propiedad]")
    try:
        cliente.actualizar({
            'nombre': 'NEW__CLIENT',
            'contraseña': '123123',
        })
        print("Actualizacion exitosa")
    except Exception as e:
        print("Hubo un error en la actualización: ", e)
    cliente.guardar()

