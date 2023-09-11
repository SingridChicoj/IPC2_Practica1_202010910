from lista_piezas import lista_piezas


mi_tablero = lista_piezas()
jump = "---------------Coloréalo---------------"

def configuracion_tablero():
    filas = input("Ingrese el ancho del tablero: ")
    columnas = input("Ingrese el alto del tablero: ")
    # Creo todas las piezas de mi tablero
    mi_tablero.inicializar_tablero(int(filas), int(columnas))
    mi_tablero.filas = int(filas)
    mi_tablero.columnas = int(columnas)
    # Verificamos que mi tablero se haya creado correctamente
    #mi_tablero.imprimir_tablero_consola()
    # Sentinela de agregar nueva pieza
    print(jump)
    nueva_pieza = True
    while nueva_pieza:
        print("Por favor elija su color", "\n",
              "* BLUE", "\n",
              "* RED", "\n",
              "* GREEN", "\n",
              "* VIOLET", "\n",
              "* ORANGE", "\n",)
        print()
        print("Por favor ingrese la fila en que desea colocar la pieza")
        fila = input("Fila: ")
        print("Por favor ingrese la columna en que desea colocar la pieza")
        columna = input("Columna: ")
        color = input("Color: ")
        print(color, ":")
        mi_tablero.actualizar_pieza(int(fila), int(columna), color)
        print("")
        print("")
        mi_tablero.imprimir_tablero_consola()
        # Preguntamos si desea agregar otra pieza
        respuesta = input("Desea agregar otra pieza S/N: ")
        print("")
        print("")
        if respuesta == "N" or respuesta == "n":
            nueva_pieza = False
    print(jump)
    mi_tablero.imprimir_tablero_consola()
    print(jump)
    print("")
    print("")
    # Deberiamos graficar
    mi_tablero.graficar()


def menu():
    print("")
    print("")
    print(jump)
    print("1. Crear tablero")
    print("2. Mostrar datos del estudiante")
    print("3. Salir")
    entrada = input("Ingrese una opción válida del menú: ")
    if entrada == "3":
        print("Adios, regresa pronto")
        quit()
    else:
        while entrada != "3":
            if entrada == "1":
                print("")
                print(jump)
                entrada = ""
                configuracion_tablero()
                menu()
            elif entrada == "2":
                print("")
                print(jump)
                print("Datos del estudiante: ")
                print(" * Singrid Cristabel Chicoj Martinez", "\n",
                      "* 202010910",  "\n",
                      "* Introduccion a la Programacion y", "\n", "  Computacion 2", "\n",
                      "* Seccion D", "\n",
                      "* 4to Semestre y Parte del 5to Semeste :c")
                entrada = ""
                print("")
                menu()
            else:
                print("")
                print("Seleccione una opcion correcta")
                entrada = ""
                print("")
                menu()

menu()
