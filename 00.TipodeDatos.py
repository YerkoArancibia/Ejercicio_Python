#Ejercicios de Tipos de Datos Simples

#Ejercicio 1
"""
Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!
"""
print("Hola Mundo")


#Ejercicio 2
"""
Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y 
luego muestre por pantalla el contenido de la variable.
"""
var_1 = "Hola Mundo"
print(var_1)


#Ejercicio 3 
"""
Escribir un programa que pregunte el nombre de usuario en la consola y después
de que el usuario lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!,
donde <nombre> es el nombre que el usuario haya introducido.
"""
nombre = input("imgrese su nombre: ")
print("¡Hola! ", nombre)


#Ejercicio 4
"""
Escribir un programa que muestre por pantalla el resultado de la siguiente 
operación aritmetica:

(3+2/2*5)**2
"""
suma = 3+2
multiplicacion = 5*2
division = suma / multiplicacion
potencia= division**2
print("Operación artimetca resulta en: ", potencia)


#Ejercicio 5
"""
Escribir un programa que pregunte al usuario por el número de horas trabajadas
y el costro por hora. Después debe mostrar por pantalla la paga que le corresponde.
"""
valor_hora = int(input("Ingrese la cantidad de horas trabajadas: "))
print(f'Pago por horas trabajadas, corresponde a: $ {valor_hora*15} dolares')


#Ejercicio 6
"""
Escribir un programa que lea un entero positivo,n, introducido por el usuario
y después muestre en pantalla la suma de todos los enteros desde 1 hasta n. 
La suma de los n primerosenteros positivos puede ser calculada de la siguiente 
forma:

suma = n(n+1)/2
"""

n = int(input("Ingrese un numero: "))
sum_n = ((n*(n+1))/2)
print(f"La suma total del numero ingresado desde el 1 corresponde a: {sum_n}")


#Ejercicio 7
"""
Escribir un programa que pida al usuario su peso (en Kg) y estatura (en metros), 
calcule el índice de masa corporal y lo almacene en una variable, y muestre por 
pantalla la frase "Tu indice de mada corporal es <imc> donde <imc> es el índice 
de masa corporal calculado redondeado con dos decimales"
"""
peso = float(input("Ingrese su peso (en Kg): "))
altura = float(input("Ingrese su altura (en cm): "))
altura_1= altura / 100
#IMC redondeado a 2 decimales
imc = peso/(altura_1**2)

print(f"Tu indice de masa corporal es: {round(imc,2)}")


#Ejercicio 8 
"""
Escribir un programa que pida al usuario dos números enteros y muestre por 
pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m>
son los números introducidos por el usuario, y <c> y <r> son el cociente y 
el resto de la división entera respectivamente.
""" 
num_1 = int(input("Ingrese un numero: "))
num_2 = int(input("Ingrese un segundo numero: "))

cociente = num_1 / num_2
resto = num_1 % num_2

print(f"{num_1} entre {num_2} da un cociente {round(cociente,2)} y un resto de {resto}")


#Ejercicio 9 
"""
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés 
anual y el número de años, y muestre por pantalla el capital obtenido en la
inversión.
"""
cap_ini = int(input("Capital inicial a invertir: "))
interes = float(input("Valor interes anual: "))
num_ano = int(input("Cantidad de años a invertir: "))
cap_final = cap_ini * (1 + interes)**num_ano

print(f"El capital final obtenido de la inversión sera de: {round(cap_final,2)}")


#Ejercicio 10
"""
Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas.
Suele hacer venta por correo y la empresa de logística les cobra por peso de
cada paquete así que deben calcular el peso de los payasos y muñecas que 
saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g.
Escribir un programa que lea el número de payasos y muñecas vendidos en el 
último pedido y calcule el peso total del paquete que será enviado.
""" 
payasos = int(input("Cantidad de payasos vendidos: "))
munecas = int(input("Cantidad de muñecas vendidas: "))

print(f"Peso total de payasos vendidos(kg): {round((payasos * 112)/100,2)}, Peso total de muñecas vendidas (kg): {round((munecas * 75)/100,2)}")


#Ejercicio 11
"""
Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés 
al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te 
añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience 
leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el 
usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros 
tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.
"""
cap_ini = int(input("Capital inicial a invertir: "))
cap_fin_1= cap_ini * (1 + 0.04)**1
cap_fin_2= cap_ini * (1 + 0.04)**2
cap_fin_3= cap_ini * (1 + 0.04)**3

print(f"Capital 1 año: {cap_fin_1}, Capital 2 año: {cap_fin_2},Capital 3 año: {cap_fin_3}")


#Ejercicio 12
"""
Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento
del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son 
del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento 
que se le hace por no ser fresca y el coste final total.
"""
barra_pan = int(input("Barras de pan vendidas que no son del día: "))
coste_final = barra_pan * 3.49 - ((barra_pan*3.49)*0.6)
print(f"Precio del pan normal: $3.49 euros, Descuento por barra: ${round((barra_pan+3.49)*0.6,2)} euros, Coste final del pan:${round(coste_final,2)} euros")