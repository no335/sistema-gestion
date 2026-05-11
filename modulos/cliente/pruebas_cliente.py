from .modelo_cliente import Cliente
import logging
logger = logging.getLogger(__name__)

def prueba_actualizar_cliente(diccionario):
    # gernerar un cliente 
    cliente = Cliente.buscar(diccionario['id'])
    cliente.actualizar(diccionario)

def prueba_creacion_error():
    # gernerar un cliente pero probar una mala configuracion de
    # el nombre del archivo para leer
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
    logger.debug("_nombre entidad cambia a valor invalido")
    Cliente._nombre_entidad = 'abcd'
    print("----Prueba creación [mala configuracion]")
    logger.info("----Prueba creación [mala configuracion]")
    try:
        cliente.guardar()
        print("Creación exitosa")
        logger.info("Creación exitosa")
    except Exception as e:
        print("Hubo un error al guardar:", e)
        logger.error("Hubo un error al guardar:", e)
    finally:
        logger.debug("_nombre entidad cambia a valor valido")
        Cliente._nombre_entidad = temp


def prueba_creacion():
    # gernerar un cliente pero probar una mala configuracion de
    # el nombre del archivo para leer
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
    logger.info("----Prueba creación")
    try:
        cliente.guardar()
        print("Creación exitosa")
        logger.info("Creación exitosa")
    except Exception as e:
        print("Hubo un error al guardar:", e)
        logger.error("Hubo un error al guardar:", e)

def prueba_actualizacion():
    # actualizar un cliente
    # buscar un listado de todos
    clientes = Cliente.buscar()
    # tomar el último
    cliente = clientes[-1]
    # actualizar un campo
    cliente.nombre = 'NEW CLIENT'
    print("----Prueba actualización")
    logger.info("----Prueba actualización")
    try:
        # guardar
        cliente.guardar()
        print("Actualizacion exitosa")
        logger.info("Actualizacion exitosa")
    except Exception as e:
        # si falla mostrar error
        print("Hubo un error en la actualización: %s " % e)
        logger.error("Hubo un error en la actualización: %s" % e)

def prueba_actualizacion_error():
    clientes = Cliente.buscar()
    cliente = clientes[-1]
    print("----Prueba actualización [Mala propiedad]")
    logger.info("----Prueba actualización [Mala propiedad]")
    try:
        cliente.actualizar({
            'nombre': 'NEW__CLIENT',
            'contraseña': '123123',
        })
        print("Actualizacion exitosa")
        logger.info("Actualizacion exitosa")
    except Exception as e:
        print("Hubo un error en la actualización: % s" % e)
        logger.error("Hubo un error en la actualización:  % s" % e)
    cliente.guardar()

