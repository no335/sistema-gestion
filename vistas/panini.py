
import numpy 

def compra_sobre(N=10, S=4):
    """
    Devuelve S numeros aleatorios entre 0 y N-1
    # N :  Láminas en total
    # S :  Láminas por sobre
    """
    return [numpy.random.random_integers(0, N - 1) for i in range(0, S)]

def llenar_album(N=10, S=4, P=1, limit=None):
    """
    Repite compra de sobres aleatorios de tamaño S hasta 
        - llenar el album  cuando limit is None
        - llegar al límite de compra cuando limit es un entero
    N :  Láminas en total
    S :  Láminas por sobre
    P :  Proporcion de láminas objetivo. En rango  [0, 1]  (P=.33, para terminar cuando se llegue al 33% p. ejemplo) 
    limit: Limite sobres
    """
    # iniciar álbum como array de numpy
    album = numpy.zeros(N)
    #inicializar láminas conseguidas --- para condición de salida
    láminas_conseguidas = 0
    #inicializar sobres comprados --- para promedio
    sobres_comprados = 0
    #inicializar  cuenta repetidas --- para promedio
    repetidas = 0
    # repetir hasta que llegue al límite inicado o
    #    las láminas nuevas conseguidas cubran todas las requeridas por el corte
    while  láminas_conseguidas < N*P if limit is None else sobres_comprados<limit:
        # contar sobre nuevo
        sobres_comprados += 1
        # conseguir laminas
        sobre = compra_sobre(N, S)
        # contar las nuevas en el álbum
        for i in sobre:
            # si es nueva contarla
            if album[i] == 0:
                láminas_conseguidas += 1
            else:
                # si no contar en repetidas
                repetidas += 1
            # marcar como obtenida / agregar a cuenta
            album[i] += 1
    return (
        sobres_comprados, 
        repetidas,
    )

def experimento_albumes(n_experimentos, N=100, S=4, P=1, limit=None, titulo=False):
    """
    Realiza n_experimentos intentos de llenar un album con 
    # N :  Láminas en total
    # S :  Láminas por sobre
    # P :  Proporcion de láminas objetivo. En rango  [0, 1]
    # limit: Limite sobres

    # titulo: Dice si imprimir el titulo de la tabla
    """
    # iniciar cuenta sobres
    avg_sobres = 0
    # iniciar cuenta repetidas
    avg_repetidas = 0
    # realizar n_experimentos pruebas
    for i in range(0, n_experimentos):
        # obtener totales de sobres y repetidas
        s, r = llenar_album(N=N, S=S, P=P, limit=limit)
        # agregar a los totales
        avg_sobres += s
        avg_repetidas += r
    # dividir por n_experimentos para obtener promedio
    avg_sobres /= n_experimentos
    avg_repetidas /= n_experimentos
    if titulo:
        print(f" # Exp     |      N |   %  |  N * %  | S |        AVG(S) |        AVG(R) |   AVG(S)*S | AVG(R)/(N*%) ")
    # numero de ensayos
    print(f"{n_experimentos:10.0f}", end=" | ")
    # total de láminas del álbum
    print(f"{N:6.0f}", end=" | ")
    # proporcion de láminas en corte
    print(f"{P:4.2f}", end=" | ")
    # número de láminas en corte
    print(f"{P*N:7.0f}", end=" | ")
    # tamaño de sobre
    print(f"{S}", end=" | ")
    # promedio de sobres requeridos
    print(f"{avg_sobres:13.2f}", end=" | ")
    # promedio de repetidas reunidas
    print(f"{avg_repetidas:13.2f}", end=" | ")
    # promedio de láminas reunidas nuevas y repetidas
    print(f"{avg_sobres*S:10.2f}", end=" | ")
    # proporcion de láminas que son repetidas
    print(f"{(avg_repetidas)/(P*N)*100:10.2f} ")

# numero de láminas
N = 12*4*20+20
# cortes 
Q = 20
# tamaño sobre
S = 7

for i in range(1, Q+1):
    experimento_albumes(1000, N=N, S=S, P=(1/Q) * i, titulo=i==1)

