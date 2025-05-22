#Ejercicio 1
"""
Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
"""
palabra = 'Pelota'

for i in range(1,11):
    print(i,' ',palabra)
    
#Ejercicio 2
"""
Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
"""
edad = int(input("Ingrese su edad: "))

for i in range(1,edad + 1):
    print(f"Su edad es : {i}")

#Ejercicio 3
"""
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
"""
numero = int(input("Ingrese un numero entero: "))

for i in range(1, numero+1):
    residuo = i % 3
    if residuo >= 0:
        print(i, end=", ")


#Ejercicio 4
"""
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
"""
numero = int(input("Ingrese un numero entero positivo: "))

for i in range(0, numero +1):
    regresion = numero - i
    print(regresion, end=", ")

#Ejercicio 5
"""
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en
la inversión cada año que dura la inversión.
"""
CI = float(input("Ingrese la cantidad a invertir: "))
IA = float(input("Ingrese el interes anual: "))
ANO = int(input("Ingre la cantidad de años: "))

for i in range(i , ANO+1):
    CF = CI *(1 + IA)**i
    print(f"El capital obtenido el año : {i}, sera de {round(CF,2)}")


#Ejercicio 6
"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.
"""
numero = int(input("Ingrese un numero entero positivo: "))

for i in range(1, numero +1):
    triangulo = "*" * i
    print(triangulo)

#Ejercicio 7
"""
Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
"""
factor = int(input("Ingrese un factor para la multiplicacion: "))

for i in range(1,11):
    multiplo= factor * i
    print(f"{factor} * {i} = {multiplo}")

#Ejercicio 8
"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.
"""

numero = int(input("Ingrese un numero entero: "))

for i in range(1, numero+1, 2):
    for j in range(i, 0, -2):
        print(j, end=" ")
    print("")

#Ejercicio 9
"""
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
"""
clave = "contraseña"


#Ejercicio 10
"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.
"""

#Ejercicio 11
"""
Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
"""

#Ejercicio 12
"""
Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.
"""

#Ejercicio 13
"""
Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.
"""