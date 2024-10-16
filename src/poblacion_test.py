from poblacion import *

def lee_poblaciones_test(ruta):
    poblaciones = lee_poblaciones(ruta)
    print("Testeando funcion lee_poblaciones...")
    print("Mostrando las tres primeras tuplass...\n")
    for poblacion in poblaciones[:3]:
        print(poblacion, "\n")


def calcula_paises_test(poblaciones):
    paises = calcula_paises(poblaciones)
    print("Testeando funcion calcula_paises...")
    print("Mostrando los paises...\n")
    for pais in paises:
        print(pais)


def filtra_por_pais_test(poblaciones, nombre_o_codigo):
    datos_pais = filtra_por_pais(poblaciones, nombre_o_codigo)
    print("Testeando funcion filtra_por_pais...")
    print("Mostrando el censo de los tres primeros años registrados...\n")
    for datos in datos_pais[:3]:
        print(datos)


def filtra_por_paises_y_año_test(poblaciones, año, paises):
    datos_año = filtra_por_paises_y_año(poblaciones, año, paises)
    print("\tTesteando funcion filtra_por_paises_y_año...")
    print(f"\t ---> Mostrando los los datos del año {año} de los paises proporcionados...\n")
    for dato in datos_año:
        print(dato, "\n")


def muestra_evolucion_poblacion_test(poblaciones, nombre_o_codigo):
    muestra_evolucion_poblacion(poblaciones, nombre_o_codigo)


def muestra_comparativa_paises_año_test(poblaciones, año, paises):
    muestra_comparativa_paises_año(poblaciones, año, paises)


if __name__ == "__main__":
    poblaciones = lee_poblaciones("data/population.csv")
    # lee_poblaciones_test("data\population.csv")
    # calcula_paises_test(poblaciones)
    # filtra_por_pais_test(poblaciones, "spain")
    # filtra_por_pais_test(poblaciones, "ESP")
    # filtra_por_paises_y_año_test(poblaciones, 1960, {"Spain", "Germany", "Georgia", "Arab World"})
    # muestra_evolucion_poblacion_test(poblaciones, "ESP")
    muestra_comparativa_paises_año_test(poblaciones, 1960, {"Spain", "Germany", "Georgia", "Arab World"})