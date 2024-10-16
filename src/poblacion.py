from collections import namedtuple
import csv
import matplotlib.pyplot as plt

RegistroPoblacion = namedtuple('RegistroPoblacion', 'pais, codigo, año, censo')

def lee_poblaciones(ruta_fichero):
    '''Función que devuelve una lista de tuplas de tipo RegistroPoblacion

    :param ruta_fichero: ruta del archivo csv
    :type ruta_fichero: str
    :return: lista de tuplas con todos los datos de las poblaciones
    :rtype: list
    '''
    
    poblaciones = []
    
    with open(ruta_fichero, newline="", encoding="utf-8") as f:
        lector = csv.reader(f)
        
        for pais, codigo, año, censo in lector:
            año = int(año)
            censo = int(censo)
            poblacion = RegistroPoblacion(pais, codigo, año, censo)
            poblaciones.append(poblacion)

    return poblaciones


def calcula_paises(poblaciones):
    '''Función que devuelve todos los paises que estan registrados

    :param poblaciones: lista de tuplas con todos los datos
    :type poblaciones: list
    :return: lista con todos los paises
    :rtype: list
    '''
    
    paises_filtrados = list(set(poblacion.pais for poblacion in poblaciones))
    return sorted(paises_filtrados)

def filtra_por_pais(poblaciones, nombre_o_codigo):
    '''Función que toma una lista de tuplas de tipo RegistroPoblacion,
        y el nombre o código de un país, y devuelve una lista de tuplas con los datos del país.

    :param poblaciones: lista de tuplas de las poblaciones
    :type poblaciones: list
    :param nombre_o_codigo: nombre o codigo del pais
    :type nombre_o_codigo: str
    :return: lista de tuplas con los datos del pais
    :rtype: list
    '''

    datos_pais = []
    
    for poblacion in poblaciones:
        if poblacion.pais.lower() == nombre_o_codigo.lower() or poblacion.codigo == nombre_o_codigo:
            dato = (poblacion.año, poblacion.censo)
            datos_pais.append(dato)
    
    return datos_pais


def filtra_por_paises_y_año(poblaciones, año, paises):
    ''' toma una lista de tuplas de tipo RegistroPoblacion, un año y un
        conjunto de nombres de países, y devuelve una lista de tuplas con los datos del año

    :return: lista de tuplas con los datos
    :rtype: list
    '''
    
    datos_poblaciones = []
    
    for poblacion in poblaciones:
        if poblacion.pais in paises and poblacion.año == año:
            datos_pais = (poblacion.pais, poblacion.censo)
            datos_poblaciones.append(datos_pais)

    return datos_poblaciones


def muestra_evolucion_poblacion(poblaciones, nombre_o_codigo):
    '''Función que  toma una lista de tuplas de tipo RegistroPoblacion y
        el nombre o código de un país, y genera una gráfica con la curva
        de evolución de la población del país dado

    :param poblaciones: lista de tuplas con las poblaciones
    :type poblaciones: list
    :param nombre_o_codigo: nombre o codigo del pais
    :type nombre_o_codigo: str
    '''
    
    datos_poblacion = filtra_por_pais(poblaciones, nombre_o_codigo)
    lista_años, lista_habitantes = zip(*datos_poblacion)
    
    plt.title(f"EVOLUCION DE LA POBLACION DE {nombre_o_codigo}")
    plt.plot(lista_años, lista_habitantes)
    plt.show()


def muestra_comparativa_paises_año(poblaciones, año, paises):
    '''Función que  toma una lista de tuplas de tipo RegistroPoblacion,
        un año y un conjunto de nombres de países y genera una gráfica
        de barras con la población de esos países en el año dado.
    '''
    
    datos_año = filtra_por_paises_y_año(poblaciones, año, paises)
    lista_paises, lista_habitantes = zip(*datos_año)
    nombres_paises = ", ".join(list(lista_paises))
    
    plt.title(f"Comparativa de {nombres_paises} en el año {año}")
    plt.bar(lista_paises, lista_habitantes)
    plt.show()
    