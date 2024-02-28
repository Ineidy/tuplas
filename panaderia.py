menu_general = {
    "pan_dulce": {
        "productos": [
            {"nombre": "Croissant de almendra", "precio": 6500},
            {"nombre": "Donas glaseadas", "precio": 3500},
            {"nombre": "Conchas de vainilla", "precio": 4200},
            {"nombre": "Pan de pasas", "precio": 4800},
            {"nombre": "Berlines rellenos de crema", "precio": 5500},
            {"nombre": "Palmeritas de chocolate", "precio": 6000},
            {"nombre": "Roles de canela", "precio": 5300},
            {"nombre": "Trenza de frutas", "precio": 7000},
            {"nombre": "Bollo de chocolate", "precio": 4800},
            {"nombre": "Muffin de arándanos", "precio": 4200}
        ],
        "promociones": [
            {"codigo": 1, "nombre": "Descuento del 15%", "precio": 2600},
            {"codigo": 2, "nombre": "3 por 2", "precio": 8400}
        ]
    },
    "pan_salado": {
        "productos": [
            {"nombre": "Baguette de ajo", "precio": 8500},
            {"nombre": "Pan integral con semillas", "precio": 9000},
            {"nombre": "Fougasse de olivas", "precio": 9500},
            {"nombre": "Pretzel de queso", "precio": 7500},
            {"nombre": "Pan de centeno", "precio": 8000},
            {"nombre": "Panecillos de cebolla", "precio": 7000},
            {"nombre": "Pita de trigo", "precio": 6000},
            {"nombre": "Bollos suizos", "precio": 7200},
            {"nombre": "Pan de avena", "precio": 8500},
            {"nombre": "Panecillos de aceitunas", "precio": 9200}
        ],
        "promociones": [
            {"codigo": 3, "nombre": "Descuento del 10%", "precio": 6750},
            {"codigo": 4, "nombre": "2 por 1", "precio": 16000}
        ]
    },
    "postres": {
        "productos": [
            {"nombre": "Tiramisú", "precio": 15000},
            {"nombre": "Cheesecake de fresa", "precio": 10000},
            {"nombre": "Mousse de chocolate", "precio": 30000},
            {"nombre": "Pastel de tres leches", "precio": 7100},
            {"nombre": "Profiteroles", "precio": 5500},
            {"nombre": "Tarta de frutas", "precio": 8200},
            {"nombre": "Crepes rellenos", "precio": 20000},
            {"nombre": "Helado artesanal", "precio": 3500},
            {"nombre": "Flan de caramelo", "precio": 8000},
            {"nombre": "Coulant de chocolate", "precio": 6500}
        ],
        "promociones": [
            {"codigo": 5, "nombre": "2 por 1, lleve 2 por tan solo", "precio": 16400},
            {"codigo": 6, "nombre": "Descuento del 20%", "precio": 16000}
        ]
    }
}

print("¿Qué vas a pedir hoy?:\n1) Pan Dulce\n2) Pan Salado\n3) Postres")
opcion = int(input("Ingrese la opción que desea (1, 2 o 3): "))

if opcion == 1:
    categoria = "pan_dulce"
elif opcion == 2:
    categoria = "pan_salado"
elif opcion == 3:
    categoria = "postres"
else:
    print("Opción no válida. Por favor, ingrese 1, 2 o 3.")
    exit()

print(f"La opción elegida es: {categoria}")

print(f"Productos en la categoría {categoria}:")
for producto in menu_general[categoria]["productos"]:
    print(f'{producto["nombre"]}: {producto["precio"]} pesos')

opcion_producto = int(input("Ingrese el número del producto que desea comprar: "))
producto_seleccionado = menu_general[categoria]["productos"][opcion_producto]
nombre_producto = producto_seleccionado["nombre"]
precio_producto = producto_seleccionado["precio"]

dinero = int(input("Ingrese la cantidad de dinero disponible: "))
vueltos = dinero - precio_producto

if dinero >= precio_producto:
    print(f'Usted compró el producto {nombre_producto} con un valor de {precio_producto} pesos, y sus vueltos son {vueltos} pesos.')
else:
    print(f'Lo siento, no tiene suficiente dinero para comprar el producto {nombre_producto}. Le falta un total de {-vueltos} pesos.')
