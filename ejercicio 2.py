nombres = []
precios = []
cantidades = []

nombre = input("Ingrese el nombre del producto: ")
precio = float(input("Ingrese el precio del producto: "))
cantidad = 0
nombres.append(nombre)
precios.append(precio)
cantidades.append(cantidad)

if nombre in nombres:
    cantidad = float(input("Ingrese la cantidad vendida: "))
    indice = nombres.index(nombre)
    precio = precios[indice]
    cantidades[indice] += cantidad
    print(
        f"La información de la venta es: lleva la cantidad de {cantidad} del artículo {nombre}. \n El total a pagar es: ${cantidad * precio}")
else:
    print("El artículo no existe")