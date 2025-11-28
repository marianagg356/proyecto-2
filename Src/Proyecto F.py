import time
import csv
from datetime import datetime   

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
    time.sleep(5)
    print("\nBienvenido", nombre)
    print("Cargando...", end="")
    time.sleep(5)
    print(" Listo!\n")


# ==============================
# CREAR ARCHIVOS SI NO EXISTEN
# ==============================

def inicializar_archivos():

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
# FECHA AUTOMÁTICA
# ==============================

def pedir_fecha():
    ahora = datetime.now()
    dia = ahora.day
    mes = ahora.month
    anio = ahora.year
    return (dia, mes, anio)


# ==============================
# CARGAR INVENTARIO
# ==============================

def cargar_inventario():
    inventario.clear()
    try:
        archivo = open(ARCHIVO_PRODUCTOS, "r", encoding="utf-8")
        lector = csv.DictReader(archivo)
        for fila in lector:
            nombre = fila["nombre"]
            precio = float(fila["precio"])
            cantidad = int(fila["cantidad"])
            inventario[nombre] = {"precio": precio, "cantidad": cantidad}
        archivo.close()
    except FileNotFoundError:
        pass


def guardar_inventario():
    archivo = open(ARCHIVO_PRODUCTOS, "w", newline="", encoding="utf-8")
    escritor = csv.writer(archivo)
    escritor.writerow(["nombre","precio","cantidad"])
    for nombre, datos in inventario.items():
        escritor.writerow([nombre, datos["precio"], datos["cantidad"]])
    archivo.close()


# ==============================
# 1. AGREGAR PRODUCTO
# ==============================

def agregar_producto():
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))

    if nombre in inventario:
        inventario[nombre]["cantidad"] += cantidad
        print("Cantidad sumada al producto existente.\n")
    else:
        inventario[nombre] = {"precio": precio, "cantidad": cantidad}
        print("Producto agregado.\n")

    guardar_inventario()


# ==============================
# 2. MOSTRAR PRODUCTOS
# ==============================

def mostrar_productos():
    if not inventario:
        print("Inventario vacío.\n")
        return

    print("\n--- PRODUCTOS ---")
    for nombre, d in inventario.items():
        print(nombre, "| Precio:", d["precio"], "| Cant:", d["cantidad"])
    print()


# ==============================
# 3. BUSCAR PRODUCTO
# ==============================

def buscar_producto():
    nombre = input("¿Qué producto buscas?: ")

    if nombre in inventario:
        d = inventario[nombre]
        print("\nNombre:", nombre)
        print("Precio:", d["precio"])
        print("Cantidad disponible:", d["cantidad"], "\n")
    else:
        print("No existe ese producto.\n")


# ==============================
# 4. VENTAS 
# ==============================

def venta():
    print("\n*** DESPLIEGUE DE MENU DE VENTAS ***")

    dia, mes, anio = pedir_fecha()

    nombre = input("Producto vendido: ")

    if nombre not in inventario:
        print("Ese producto no existe.\n")
        return

    stock = inventario[nombre]["cantidad"]
    precio_u = inventario[nombre]["precio"]

    cantidad = int(input("Cantidad vendida: "))

    if cantidad > stock:
        print("Cantidad excedente de stock, solo hay", stock, "\n")
        return

    subtotal = precio_u * cantidad
    descuento = subtotal * DESCUENTO_MAYOREO if cantidad >= UMBRAL_MAYOREO else 0
    total = subtotal - descuento

    inventario[nombre]["cantidad"] -= cantidad
    guardar_inventario()

    print("\nVenta registrada:")
    print("Subtotal:", subtotal)
    print("Descuento:", descuento)
    print("Total:", total, "\n")

    archivo = open(ARCHIVO_VENTAS, "a", newline="", encoding="utf-8")
    escritor = csv.writer(archivo)
    escritor.writerow([dia, mes, anio, nombre,
                       cantidad, precio_u,
                       subtotal, descuento, total])
    archivo.close()


# ==============================
# 5. SALIDA MANUAL 
# ==============================

def salida_manual():
    print("\n*** DESPLIEGUE DE MENU DE SALIDAS ***")

    dia, mes, anio = pedir_fecha()

    nombre = input("Producto a dar de baja: ")

    if nombre not in inventario:
        print("No existe.\n")
        return

    cantidad = int(input("Cantidad a dar de baja: "))

    if cantidad > inventario[nombre]["cantidad"]:
        print("No puedes dar de baja más de lo existente.\n")
        return

    inventario[nombre]["cantidad"] -= cantidad
    guardar_inventario()

    archivo = open(ARCHIVO_SALIDAS, "a", newline="", encoding="utf-8")
    escritor = csv.writer(archivo)
    escritor.writerow([dia, mes, anio, nombre, cantidad])
    archivo.close()

    print("Salida registrada.\n")


# ==============================
# 6. REPORTE DE VENTAS
# ==============================

def reporte_ventas():
    print("\n--- REPORTE DE VENTAS ---")
    try:
        archivo = open(ARCHIVO_VENTAS, "r", encoding="utf-8")
        lector = csv.DictReader(archivo)
        for fila in lector:
            print(fila["dia"]+"/"+fila["mes"]+"/"+fila["anio"],
                  "|", fila["producto"],
                  "| Cant:", fila["cantidad"],
                  "| Total:", fila["total"])
        archivo.close()
    except FileNotFoundError:
        print("No hay ventas registradas.")
    print()


# ==============================
# 7. REPORTE DE SALIDAS
# ==============================

def reporte_salidas():
    print("\n--- REPORTE DE SALIDAS ---")
    try:
        archivo = open(ARCHIVO_SALIDAS, "r", encoding="utf-8")
        lector = csv.DictReader(archivo)
        for fila in lector:
            print(fila["dia"]+"/"+fila["mes"]+"/"+fila["anio"],
                  "|", fila["producto"],
                  "| Salida:", fila["cantidad_salida"])
        archivo.close()
    except FileNotFoundError:
        print("No hay salidas.")
    print()


# ==============================
# 8. CERRAR PROGRAMA
# ==============================

def cerrar_programa():
    op = input("¿Seguro que quieres salir? (si/no): ")
    if op == "si":
        print("gracias por usar el programa")
        return True
    print("Volviendo al menú...\n")
    return False


# ==============================
# MENÚ PRINCIPAL
# ==============================

def mostrar_menu():
    print("===== MENÚ =====")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Venta")
    print("5. Salida manual de stock")
    print("6. Reporte de ventas")
    print("7. Cerrar programa")
    print("8. Reporte de salidas manuales")
    print("================\n")


# ==============================
# MAIN LOOP
# ==============================

def main():
    bienvenida()
    inicializar_archivos()
    cargar_inventario()

    salir = False

    while not salir:
        mostrar_menu()
        opcion = input("Opción: ")

        if opcion == "1": agregar_producto()
        elif opcion == "2": mostrar_productos()
        elif opcion == "3": buscar_producto()
        elif opcion == "4": venta()
        elif opcion == "5": salida_manual()
        elif opcion == "6": reporte_ventas()
        elif opcion == "7": salir = cerrar_programa()
        elif opcion == "8": reporte_salidas()
        else:
            print("Opción inválida.\n")


main()