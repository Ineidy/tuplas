productos = tuple((
    "Coca-Cola", 
    "Pepsi", 
    "Sprite", 
    "Fanta", 
    "7UP", 
    "Mountain Dew", 
    "Dr Pepper", 
    "Schweppes", 
    "Mirinda", 
    "Lift"))
precios = tuple((
    4500, 
    3750, 
    3000, 
    3600, 
    5250, 
    6000, 
    5400, 
    3900, 
    4200, 
    4800))
print("MENU DE SELECCION DE PRODUCTOS")
for i,val in enumerate(productos):
    print(f"""      {i}. {val} ${precios[i]} """)
opcion = int(input())
print(f'Usuario, usted selecciono el productos {productos[opcion]} con un valor de ${precios[opcion]}')

dinero = int(input("INGRESE LA CANTIDAD DE DINERO DISPONIBLE: "))
vueltos = dinero - precios[opcion]
if dinero >= precios[opcion]:
    print(f'Usuario, usted compro el producto {productos[opcion]} con un valor de ${precios[opcion]}, y sus vueltos son ${vueltos}')
else:
    print(f'Usuario, EL producto que desea comprar {productos[opcion]} con un valor de ${precios[opcion]}, le falta un total de ${-vueltos}')