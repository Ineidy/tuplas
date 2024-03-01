print("ANTES DE SELECCIONAR UN PRODUCTO REVISA LA PARTE DE ABAJO DE LA LISTA!!")
print("YA QUE SI HAY ALGUNA PROMOCION VIGENTE PARA ALGUN PRODUCTO!!")
print()
print()

menu_general = dict({
    "pan_dulce": {
        "productos": list([

        
            {"nombre": "Croissant de almendra", "precio": 6500},
            {"nombre": "Donas glaseadas", "precio": 3500},
            {"nombre": "Conchas de vainilla", "precio": 4200},
            {"nombre": "Pan de pasas", "precio": 4800},
            {"nombre": "Berlines rellenos de crema", "precio": 5500},
            {"nombre": "Palmeritas de chocolate", "precio": 6000},
            {"nombre": "Roles de canela", "precio": 5300},
            {"nombre": "Trenza de frutas", "precio": 7000},
            {"nombre": "Bollo de chocolate", "precio": 4800},
            {"nombre": "Muffin de arándanos", "precio": 4200},
            {"nombre": "ATENCION! HAY UN DESCUENTO DEL 15% PARA EL PRODUCTO PALMERITAS DE CHOCOLATE", "precio": 5100},
            {"nombre": "ATENCION! HAY UNA PROMOCION DE 3 POR 2 EN EL PRODUCTO TRENZAS DE FRUTAS", "precio": 14000}
        ]),
    },
    "pan_salado": {
        "productos": list([
      
            {"nombre": "Baguette de ajo", "precio": 8500,},
            {"nombre": "Pan integral con semillas", "precio": 9000},
            {"nombre": "Fougasse de olivas", "precio": 9500},
            {"nombre": "Pretzel de queso", "precio": 7500},
            {"nombre": "Pan de centeno", "precio": 8000},
            {"nombre": "Panecillos de cebolla", "precio": 7000},
            {"nombre": "Pita de trigo", "precio": 6000},
            {"nombre": "Bollos suizos", "precio": 7200},
            {"nombre": "Pan de avena", "precio": 8500},
            {"nombre": "Panecillos de aceitunas", "precio": 9200},
            {"nombre": "ATENCION! HAY UN DESCUENTO DEL 20% PARA EL PRODUCTO PANECILLOS DE ACEITUNAS", "precio": 7350},
            {"nombre": "ATENCION! HAY UNA PROMOCION DEL 2 POR 1 PARA EL PRODUCTO PAN INTEGRAL CON SEMILLAS", "precio": 9000}

        ]),
        
    },
    "postres": {
        "productos": list([
            
            {"nombre": "Tiramisú", "precio": 15000},
            {"nombre": "Cheesecake de fresa", "precio": 10000},
            {"nombre": "Mousse de chocolate", "precio": 30000},
            {"nombre": "Pastel de tres leches", "precio": 7100},
            {"nombre": "Profiteroles", "precio": 5500},
            {"nombre": "Tarta de frutas", "precio": 8200},
            {"nombre": "Crepes rellenos", "precio": 20000},
            {"nombre": "Helado artesanal", "precio": 3500},
            {"nombre": "Flan de caramelo", "precio": 8000},
            {"nombre": "Coulant de chocolate", "precio": 6500},
            {"nombre": "ATENCION! HAY UN DESCUENTO DEL 50% PARA EL PRODUCTO MOUSSE DE CHOCOLATE", "precio": 15000},
            {"nombre": "ATENCION! HAY UN DESCUENTO DEL 15% PARA EL PRODUCTO CREPES RELLENOS", "precio": 17000}
        ]),
        
    }
})

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
for i, producto in enumerate(menu_general[categoria]["productos"]):
    print(f'{i}: {producto["nombre"]}: {producto["precio"]} pesos')

opcion_producto = int(input("Ingrese el número del producto que desea comprar: "))
producto_seleccionado = menu_general[categoria]["productos"][opcion_producto]
nombre_producto = producto_seleccionado["nombre"]
precio_producto = producto_seleccionado["precio"]

cantidad = int(input(f"Ingrese el numero de productos que desea comprar de {nombre_producto}: "))

precio_final = cantidad * precio_producto

dinero = float(input(f"Ha seleccionado el producto {nombre_producto} con un valor de {precio_producto}. Ingrese la cantidad de dinero disponible: "))
vueltos = dinero - precio_final

if vueltos >= 0:
    print(f'Usted compró el producto {nombre_producto} con un valor de {precio_final} pesos, y sus vueltos son {vueltos} pesos.')
else:
    print(f'Lo siento, no tiene suficiente dinero para comprar el producto {nombre_producto}. Le falta un total de {-vueltos} pesos.')