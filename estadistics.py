import globales
import os
import math


def valor_mas_alto():
    todos_las_ventas=globales.leer_archivo_json("ventas")
    productos= ["Café Americano","Té Chai","Croissant","Jugo Naranja","Panini de Pavo y Queso","Pastel de Zanahoria","Espresso Doble","Ba;do de Frutas","Muffin","Ensalada","Chocolate Caliente","Tarta de Frambuesa","Sándwich de Huevo","Galletas de Avena","Frappé de Caramelo"]
    valores_ordenados=sorted(todos_las_ventas,key=lambda x:x['valor'],reverse=True)

    for venta in valores_ordenados[:1]:
        nombre_producto=""
        for producto in productos:
            if producto == venta["Ventas"]:
                nombre_producto=f"{producto}"
        print(f"El valor mas alto es {venta} de {nombre_producto}")

def valor_mas_bajo():
    todos_las_ventas=globales.leer_archivo_json("ventas")
    productos= ["Café Americano","Té Chai","Croissant","Jugo Naranja","Panini de Pavo y Queso","Pastel de Zanahoria","Espresso Doble","Ba;do de Frutas","Muffin","Ensalada","Chocolate Caliente","Tarta de Frambuesa","Sándwich de Huevo","Galletas de Avena","Frappé de Caramelo"]
    valores_ordenados=sorted(todos_las_ventas,key=lambda x:x['valor'],reverse=False)

    for iva in valores_ordenados[:1]:
        nombre_producto=""
        for producto in productos:
            if producto == iva["iva"]:
                nombre_producto=f"{producto}"
        print(f"El valor mas Bajo es {iva} de {nombre_producto}")

def promedio_productos():
    todos_las_ventas=globales.leer_archivo_json("ventas")
    suma_ventas=0
    cantidad_productos=0

    for venta in todos_las_ventas["valor"]:
        suma_ventas=+venta
        cantidad_productos+=1

        promedio_productos=suma_ventas/cantidad_productos
    print(f"El promedio de las ventas es ${promedio_productos}")

def media_geometrica():
    todos_las_ventas=globales.leer_archivo_json("ventas")
    suma_ventas=0
    cantidad_productos=0

    for venta in todos_las_ventas["valor"]:
        suma_ventas=+ math.log(venta)
        cantidad_productos+=1

        media_geometrica=math.exp(suma_ventas/cantidad_productos)
    print(f"La media geometrica de las ventas es ${media_geometrica}")
             
