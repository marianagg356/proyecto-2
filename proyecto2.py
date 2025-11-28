
#   PROGRAMA PARA CONTROL DE INVENTARIO Y VENTAS

import time
from datetime import datetime
import csv

# ==============================
# ARCHIVOS DEL SISTEMA
# ==============================

ARCHIVO_PRODUCTOS = "productos.csv"
ARCHIVO_VENTAS = "ventas.csv"
ARCHIVO_SALIDAS = "salidas.csv"
ARCHIVO_SISTEMA = "archivo_sistema.txt"   

inventario = {}

UMBRAL_MAYOREO = 10
DESCUENTO_MAYOREO = 0.10

# ==============================
# 1. BIENVENIDA + CARGA
# ==============================

def bienvenida():
    nombre = input("Ingresa tu nombre: ")
    print("\nBienvenido", nombre)
    print("Cargando...", end="")
    time.sleep(5)
    print(" Listo!\n")

# ==============================
# FECHA AUTOMÁTICA
# ==============================

def pedir_fecha():
    ahora = datetime.now()
    dia = ahora.day
    mes = ahora.month
    anio = ahora.year
    return (dia, mes, anio)


# ==============================
# CREAR ARCHIVOS SI NO EXISTEN
# ==============================

def iniciar_archivos():

    try:
        open(ARCHIVO_PRODUCTOS, "r")
    except FileNotFoundError:
        archivo = open(ARCHIVO_PRODUCTOS, "w", newline="", encoding="utf-8")
        escritor = csv.writer(archivo)
        escritor.writerow(["nombre", "precio", "cantidad"])
        archivo.close()

    try:
        open(ARCHIVO_VENTAS, "r")
    except FileNotFoundError:
        archivo = open(ARCHIVO_VENTAS, "w", newline="", encoding="utf-8")
        escritor = csv.writer(archivo)
        escritor.writerow(["dia","mes","anio",
                           "producto","cantidad",
                           "precio_u","subtotal",
                           "descuento","total"])
        archivo.close()

    try:
        open(ARCHIVO_SALIDAS, "r")
    except FileNotFoundError:
        archivo = open(ARCHIVO_SALIDAS, "w", newline="", encoding="utf-8")
        escritor = csv.writer(archivo)
        escritor.writerow(["dia","mes","anio",
                           "producto","cantidad_salida"])
        archivo.close()

    try:
        open(ARCHIVO_SISTEMA, "r")
    except FileNotFoundError:
        archivo = open(ARCHIVO_SISTEMA, "w", encoding="utf-8")
        archivo.write("ARCHIVO DEL SISTEMA - INTERNOS\n")
        archivo.close()


# ==============================
# CARGAR INVENTARIO
# ==============================

inventario = {}

def cargar_inventario():
    # leer productos.csv y meterlos al diccionario
    pass


def guardar_inventario():
    # guardar el diccionario en productos.csv
    pass


# ==============================
# 1. AGREGAR PRODUCTO
# ==============================

def agregar_producto():
    pass


# ==============================
# 2. MOSTRAR PRODUCTOS
# ==============================

def mostrar_productos():
    pass


# ==============================
# 3. BUSCAR PRODUCTO
# ==============================

def buscar_producto():
    pass

# ==============================
# 4. VENTAS 
# ==============================

# pedir cantidad, checar stock,
# si se pasa: "Cantidad excedente de stock solo hay X"
# calcular subtotal, descuento y total
# y guardarlo en ventas.csv

def venta():
    pass


# ==============================
# 5. SALIDA MANUAL 
# ==============================

# baja de stock 
# guardar fecha, producto y cantidad en salidas.csv

def salida_manual():
    pass


# ==============================
# 6. REPORTE DE VENTAS
# ==============================

# leer ventas.csv y mostrar info

def reporte_ventas():
    pass

# ==============================
# 7. REPORTE DE SALIDAS
# ==============================

# leer salidas.csv

def reporte_salidas():
    pass


# ==============================
# 8. CERRAR PROGRAMA
# ==============================

# si dice que sí -> "gracias por usar el programa"
# si no -> regresa al menú

def cerrar_programa():
    pass


# ==============================
# MENÚ PRINCIPAL
# ==============================

def mostrar_menu():
    print("\n=========== MENÚ PRINCIPAL ===========")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Venta")
    print("5. Salida manual")
    print("6. Reporte de ventas")
    print("7. Cerrar programa")
    print("8. Reporte de salidas")
    print("======================================\n")


# ==============================
# MAIN LOOP
# ==============================

def main():

    bienvenida()
    crear_archivos()
    cargar_inventario()

    salir = False

    while not salir:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            buscar_producto()
        elif opcion == "4":
            venta()
        elif opcion == "5":
            salida_manual()
        elif opcion == "6":
            reporte_ventas()
        elif opcion == "7":
            salir = cerrar_programa()
        elif opcion == "8":
            reporte_salidas()
        else:
            print("Esa opción no existe.\n")


main()

#si se puede 
