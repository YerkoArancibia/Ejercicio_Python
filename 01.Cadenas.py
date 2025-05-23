#Ejercicios de Cadenas

#Ejericicio 1
"""
Escribir un programa que pregunte el nombre del usuario en la consola y un número entero
e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el 
número introducido.
"""
nombre = input("Ingrese su nombre completo: ")
numero = int(input("Ingrese un numero: "))

print((nombre +'\n') * numero)


#Ejercicio 2
"""
Escribir un programa que pregunte el nombre completo del usuario en la consola y después 
muestre por pantalla el nombre completo del usuario tres veces, una con todas las letras 
minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra del 
nombre y de los apellidos en mayúscula. El usuario puede introducir su nombre combinando 
mayúsculas y minúsculas como quiera.
"""

nombre = input("Ingrese su Nombre Completo: ")
print(nombre.lower(),'\n', nombre.upper(), '\n', nombre.title() )


#Ejercicio 3
"""
Escribir un programa que pregunte el nombre del usuario en la consola y después de que el 
usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el 
nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre
"""
nombre = input("Ingrese su Nombre completo: ")
print(f"Su nombre: {nombre.upper()}, tiene {len((nombre))} caracteres")


#Ejercicio 4
"""
Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el
prefijo es el código del país +34, y la extensión tiene dos dígitos (por ejemplo 
+34-913724710-56). Escribir un programa que pregunte por un número de teléfono con este 
formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.
"""
celular = input("Ingrese su numero telefonico (Ej:  +34-913724710-56)")
print(f"Su numero telefonico es el siguiente : {celular[4:-3]}")

#Ejercicio 5
"""
Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre 
por pantalla la frase invertida.
"""
frase = input("Ingrese una frase: ")
print(f"La frase invertida es: {frase[:-1]}")

#Ejercicio 6
"""
Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal,
y después muestre por pantalla la misma frase pero con la vocal reemplazando a un vocal de la
frase en mayúscula.
"""
palabra = input("Ingrese una palabra: ")
vocal = input("Ingrese una vocal: ")

print(f"{palabra}{vocal.upper()}")

#Ejercicio 7
"""
Escribir un programa que pregunte el correo electrónico del usuario en la consola y 
muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la 
arroba @) pero con dominio ceu.es.
"""
email = input("Ingrese su correo electronico(@gmail): ")
EXTENSION_GMAIL = email[ :email.find("@")]
print(f"{EXTENSION_GMAIL}" + "@edu.es")

#Ejercicio 8
"""
Escribir un programa que pregunte por consola el precio de un producto en euros con dos 
decimales y muestre por pantalla el número de euros y el número de céntimos del precio 
introducido.
"""
precio = float(input("Ingrese el valor del producto en euros: "))
euros = precio[None : precio.find(".")]
centimos = precio[precio.find(".") + 1 : +1]
print(f"La cantidad de euros son {int(euros)} y la cantidad de centimos son {int(centimos)}")

#Ejercicio 9
"""
Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato 
dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior 
para que también funcione cuando el día o el mes se introduzcan con un solo carácter.
"""
fecha = input("Ingrese la fehca actual (DD/MM/AAAA)")
sep_fecha_dia = fecha[0:2]
sep_fecha_mes = fecha[3:5]
sep_fecha_ano = fecha[6:10]
print(f"Usted nacio el día {sep_fecha_dia} en el mes {sep_fecha_mes} del año {sep_fecha_ano}")

#Ejercicio 10
"""
Escribir un programa que pregunte por consola por los productos de una cesta de la compra, 
separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.
"""
produc_cesta = input("Ingrese todos los productos de una cesta (separe los productos con una ','): ")
print("\n".join(produc_cesta.split(",")))

#Ejercicio 11
"""
Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades
y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario 
con 6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total 
con 8 dígitos enteros y 2 decimales.
"""
producto = input("Ingrese el nombre del producto: ")
precio = float(input("Ingrese el precio del producto: "))
unidades = int(input("Ingrese la cantidad de unidades: "))

print(f"Producto: {producto} | Precio: {round(precio)}, | Valor total: {precio * unidades}")