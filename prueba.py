producto = input("Ingrese el nombre del producto: ")
precio = float(input("Ingrese el precio del producto: "))
unidades = int(input("Ingrese la cantidad de unidades: "))

print(f"Producto: {producto} | Precio: {round(precio,2)}, | Valor total: {precio * unidades}")