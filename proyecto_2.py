#   PROGRAMA PARA CONTROL DE INVENTARIO Y VENTAS

import time     # para la espera del mensaje de bienvenida
import csv      # para guardar y leer archivos CSV
from datetime import datetime  

# Archivos donde se guarda todo
ARCHIVO_PRODUCTOS = "productos.csv"
ARCHIVO_VENTAS = "ventas.csv"
ARCHIVO_SALIDAS = "salidas.csv"
ARCHIVO_SISTEMA = "archivo_sistema.txt" 

# ==============================
# 1. BIENVENIDA + CARGA
# ==============================
def main():
    """
    Aquí va el flujo principal:
    - pedir nombre
    - mensaje de bienvenida con 5 segundos
    - cargar productos desde CSV
    - mostrar menú en un ciclo
    """
    # Aquí va el código del programa principal
    # cargar inventario, menú, opciones, etc.
    ...


def solicitar_nombre():
    """
    Pide el nombre del usuario y lo regresa.
    """
    # Aquí va el input() del nombre
    ...


def mensaje_bienvenida(nombre):
    """
    Manda un mensaje de bienvenida y espera 5 segundos.
    """
    # print(), time.sleep(5), etc.  #el time.sleep es necesario no esta a discusión 
    … 


def mostrar_menu_principal():
    """
    Muestra el menú principal:
    1. agregar producto
    2. mostrar productos
    3. buscar producto
    4. venta
    5. salida manual
    6. reporte de ventas
    7. cerrar programa
    8. reporte de salidas
    """
    # imprimir menú y pedir opción con input()
    ...


def capturar_fecha():
# forma 1:
    from datetime import date, datetime

# Solo la fecha (día, mes, año)
hoy = date.today()
print("Fecha de hoy:", hoy
    """
#    Pide la fecha (dd/mm/aaaa) y la regresa como tupla.

    """
    # validar formato y convertir a tupla
    ...


def cargar_productos_csv():
    """
    Carga los productos desde productos.csv.
    Regresa un diccionario tipo:
    { "coca": {"precio": 20.0, "cantidad": 5}, ... }
    """
    # abrir CSV, leer líneas y llenar diccionario
    ...


def guardar_productos_csv(inventario):
    """
    Guarda todo el inventario en el archivo productos.csv.
    """
    # abrir productos.csv en modo escritura y guardar todo
    ...


def agregar_producto(inventario):
    """
    Agrega un producto nuevo o suma cantidad si ya existe.
    Actualiza el archivo CSV después.
    """
    # pedir nombre, precio, cantidad y actualizar inventario
    ...


def mostrar_productos(inventario):
    """
    Muestra todos los productos con precio y cantidad.
    """
    # recorrer inventario e imprimir todo
    ...


def buscar_producto(inventario):
    """
    Pregunta: '¿Qué producto buscas perro?'
    Si existe lo muestra; si no, avisa que no está.
    """
    # input(), buscar en inventario, mostrar datos
    ...


def menu_ventas(inventario):
    """
    Todo lo de ventas:
    - pedir fecha
    - pedir producto
    - pedir cantidad
      * si no hay suficientes, cancelar
    - calcular total
    - aplicar descuento por mayoreo
    - actualizar inventario
    - guardar venta en ventas.csv
    """
    # lógica de venta completa
    ...


def guardar_venta_csv(fecha, producto, cantidad, precio, subtotal, descuento, total):
    """
    Guarda una venta nueva en ventas.csv.
    """
    # abrir CSV en modo append y escribir la venta
    ...


def salida_manual(inventario):
    """
    Restar manualmente cantidades del inventario:
    - pedir fecha
    - pedir producto
    - pedir cantidad
    - actualizar inventario
    - guardar salida en salidas.csv
    """
    # lógica de salida manual
    ...


def guardar_salida_csv(fecha, producto, cantidad):
    """
    Guarda una salida manual en el archivo salidas.csv.
    """
    # write en CSV
    ...


def reporte_ventas():
    """
    Permite ver ventas:
    - por día
    - por mes
    - por año
    leyendo ventas.csv
    """
    # leer CSV y filtrar según lo que el usuario pida
    ...


def reporte_salidas():
    """
    Permite ver salidas:
    - por día
    - por mes
    - por año
    leyendo salidas.csv
    """
    # leer CSV y mostrar según filtro
    ...


def cerrar_programa():
    """
    Pregunta si se quiere cerrar.
    si = muestra 'gracias por usar el programa puto'
    no = regresa al menú
    """
    # input(), decisión del usuario
    ...

    main()

#vamos equipo #fuerzaleona 

#si se puede 
