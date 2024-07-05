import os
import globales
import ventas
import estadistics
os.system("cls")

def estadisticas():
    while True:
        print("1. Producto con valor más alto.")
        print("2. Producto con valor del IVA más bajo.")
        print("3. Promedio del valor de los productos.")
        print("4. Media geométrica del valor de los productos.")
        print("5. Salir")

        opcion=globales.seleccionar_opcion(3)

        if opcion==1:
            estadistics.valor_mas_alto()
        elif opcion ==2:
            estadistics.valor_mas_bajo()
        elif opcion==3:
            estadistics.promedio_productos()
        elif opcion ==4:
            estadistics.media_geometrica()
        elif opcion==5:
            menu_general()
        input()



def menu_general():
    while True:
        print("1. Asignar montos aleatorios.")
        print("2. Ver estadísticas.")
        print("3. Salir del programa.")

        opcion=globales.seleccionar_opcion(3)

        if opcion==1:
            ventas.montos_aleatorios()
        elif opcion ==2:
            estadistics()
        elif opcion==3:
            return()
        
menu_general()

    