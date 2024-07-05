import globales
import random


def montos_aleatorios():
    ventas=globales.leer_archivo_json("Ventas.json")
    productos=["Café Americano","Té Chai","Croissant","Jugo Naranja","Panini de Pavo y Queso","Pastel de Zanahoria","Espresso Doble","Ba;do de Frutas","Muffin","Ensalada","Chocolate Caliente","Tarta de Frambuesa","Sándwich de Huevo","Galletas de Avena","Frappé de Caramelo"]
    for producto in productos:
        nombres=producto
        valor=random.randint(2000,10000)
        iva= valor*0.19
        
        todas_las_ventas = {
            'nombre': nombres,
            'valor': valor,
            'iva': iva
            }
        ventas.append(todas_las_ventas)
    globales.guardar_archivo_json("Ventas.json",ventas)
    print("ventas_cargadas")

montos_aleatorios()
        





