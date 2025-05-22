#Ejercicios de condicionales

#Ejercicio 1
"""
Escribir un programa que pregunte al usuario su edad 
y muestre por pantalla si es mayor de edad o no.

++++++++++++++++++++++++++++++++++
+   INFANTES   + [0 A 6 AÑOS]    +
++++++++++++++++++++++++++++++++++
+     NIÑEZ    + [6 A 12 AÑOS]   +
++++++++++++++++++++++++++++++++++
+ ADOLESCENCIA + [12 a 20 AÑOS]  +
++++++++++++++++++++++++++++++++++
+   JUVENTUD   + [20 A 25 AÑOS]  +
++++++++++++++++++++++++++++++++++
+   ADULTEZ    + [25 A 60 AÑOS]  +
++++++++++++++++++++++++++++++++++
+  ANCIANIDAD  + [60 AÑOS O MÁS] +
++++++++++++++++++++++++++++++++++
"""

edad = int(input("Ingrese su edad: "))

if (edad >= 0 and edad <= 6):
    print("Usted es infante") 
elif (edad >= 6 and edad <= 12 ):
    print("Usted es un nin@")
elif (edad >= 12 and edad <= 20):
    print("Usted es un adolescente")
elif (edad >= 20 and edad <= 25):
    print("Usted es un joven")
elif (edad >= 25 and edad <= 60):
    print("Usted es un adulto")
else:
    print("Usted es un anciano")

#Ejercicio 2
"""
Escribir un programa que almacene la cadena de caracteres <contraseña> en una variable, pregunte al usuario por la <contraseña> e imprima por pantalla si la contraseña introducida por el usurio
coincide con la guardada en la variable sin tener en cuenta máyuscula y minúsculas.
"""
contraseña = "contraseña"

password = input("Ingrese la contrasañe guardada: ")

if password.lower() == contraseña:
    print("La contraseña ingresada es correcta")
else:
    print("La contraseña ingresada es incorrecta")

#Ejercicio 3
"""
Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error
"""
num1 = float(input("Ingrese el primer digito: "))
num2 = float(input("Ingrese el segundo digito: "))

if num2 == 0:
    print("No se puede dividir entre cero")
else:
    division = num1 / num2
    print(f"El resultado de la division entre {num1} y {num2} es {division}")

#Ejercicio 4
"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
"""

numero = int(input("Ingrese un numero entero: "))
residuo = numero % 2

if residuo == 0 :
    print("El numero ingresado es par")
else:
    print("El numero ingresado no es par")

#Ejercicio 5
"""
Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad 
y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.
"""
edad = int(input("Ingrese su edad: "))
ingresos = int(input("Ingrese sus ingresos totales: "))

if edad >= 16 and ingresos >= 1000:
    print("Usted debe pagar impuestos por sus ingresos")
else:
    print("Usted no debe pagar impuestos por sus ingresos")


#Ejercicio 6
"""
Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con 
un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

En python se pueden comparar las letras del abecedario, como los valores numericos se pueden comparar 'M' es mayor que, o menor que 'N', esta comparación te permite obtener un 'True'
 si es verdadero o un 'False' si es falso
"""

nombre = input("Ingrese su nombre: ")
sexo = input("Ingrese su sexo (Másculino o Femenino): ")

if (sexo.upper() == 'MASCULINO' or sexo.upper() == 'M') and nombre[0:1].upper() > 'N':
    print(f"{nombre} de sexo masculino pertenece al grupo A")
elif (sexo.upper() == 'FEMENINO' or sexo.upper() == 'F') and nombre[0:1].upper() < 'M':
    print(f"{nombre} de sexo femenino pertenece al grupo A")
else:
    print(f"{nombre} de sexo {sexo} pertenece al grupo B")

#Ejercicio 7
"""
Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:

++++++++++++++++++++++++++++++++++++++++++++++++
+   Renta               +   Tipo impositivo    +
++++++++++++++++++++++++++++++++++++++++++++++++
+   Menos de 10000E     +           5%         +
++++++++++++++++++++++++++++++++++++++++++++++++
+   Entre 10000 y 20000E+           15%        +
++++++++++++++++++++++++++++++++++++++++++++++++
+   Entre 20000 y 35000E+           20%        +
++++++++++++++++++++++++++++++++++++++++++++++++
+   Entre 35000 y 60000E+           30%        +
++++++++++++++++++++++++++++++++++++++++++++++++
+   Más de 60000E       +           45%        +
++++++++++++++++++++++++++++++++++++++++++++++++

Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.
"""
renta = float(input("Ingrese su renta anual: "))

if renta < 10000:
    renta_imp_1 = renta - (renta * 0.05)
    print(f"Su renta anual de {renta} le corresponde un 5% de impuestos, equivalente a {renta_imp_1}")
elif renta >= 10000 and renta <= 20000:
    renta_imp_2 = renta - (renta * 0.15)
    print(f"Su renta anual de {renta} le corresponde un 15% de impuestos, equivalente a {renta_imp_2}")
elif renta >=20000 and renta <= 35000 :
    renta_imp_3 = renta - (renta * 0.20)
    print(f"Su renta anual de {renta} le corresponde un 20% de impuestos, equivalente a {renta_imp_3}")
elif renta >=35000 and renta <= 60000:
    renta_imp_4 = renta - (renta * 0.30)
    print(f"Su renta anual de {renta} le corresponde un 30% de impuestos, equivalente a {renta_imp_4}")
else:
    renta_imp_5 = renta - (renta * 0.45)
    print(f"Su renta anual de {renta} le corresponde un 45% de impuestos, equivalente a {renta_imp_5}")

#Ejercicio 8
"""
En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir
los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€ 
multiplicada por la puntuación del nivel.

++++++++++++++++++++++++++++++++++++
+   Nivel	       +   Puntuación  +
++++++++++++++++++++++++++++++++++++
+   Inaceptable    +	    0.0    +
++++++++++++++++++++++++++++++++++++
+   Aceptable	   +        0.4    +
++++++++++++++++++++++++++++++++++++
+   Meritorio	   +    0.6 o más  +
++++++++++++++++++++++++++++++++++++

Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario.
"""
puntuacion = float(input("Ingrese la puntuación indicada: "))

if puntuacion == 0.0:
    recompensa = 2400 * puntuacion
    print(f"Su puntuacion es de {puntuacion} con un nivel inaceptable, con una recompensa de {recompensa} euros")
elif puntuacion == 0.4:
    recompensa = 2400 * puntuacion
    print(f"Su puntuacion es de {puntuacion} con un nivel aceptable, con una recompensa de {recompensa} euros")
elif puntuacion == 0.6 or puntuacion >= 0.6:
    recompensa = 2400 * puntuacion
    print(f"Su puntuacion es de {puntuacion} con un nivel meritorio, con una recompensa de {recompensa} euros")
else: 
    print("Su puntuación debe estar en los parametros '0.0', '0.4' o '0.6'")
    
#Ejercicio 9
"""
Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. 
El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 
5€ y si es mayor de 18 años, 10€.
"""

edad = int(input("Ingrese su edad: "))

if edad < 4:
    print("La entrada es gratuita")
elif edad >=4 and edad <= 18:
    print("Le entrada tiene un valor de 5 E")
else:
    print("El valor de la entrada tiene un valor de 10 E")
    
#Ejercicio 10
"""
La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

- Ingredientes vegetarianos: Pimiento y tofu.
- Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se 
puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los 
ingredientes que lleva.
"""
print("""
          ++++++++++++++++++++++++++++++++++++++++
          +     TIPOS DE PIZZA DISPONIBLES       +
          ++++++++++++++++++++++++++++++++++++++++
          +    OPCION 1    + PIZZA VEGETARIANA   +
          ++++++++++++++++++++++++++++++++++++++++
          +    OPCION 2    + PIZZA NORMAL        +
          ++++++++++++++++++++++++++++++++++++++++  
          """)

eleccion_pizza = input("Que tipo de pizza desea ('vegetariana (vege)' o 'normal (norm)'): ")

if (eleccion_pizza.upper() == 'VEGETARIANA' or eleccion_pizza == 'VEGE' or eleccion_pizza.upper() == 'OPCION 1' or eleccion_pizza.upper() == '1'):
    print("""
          ++++++++++++++++++++++++++++++++++++++++
          + Su elección de pizza es: VEGETARIANA +
          ++++++++++++++++++++++++++++++++++++++++
          +    INGREDIENTE 1    +    PIMENTON    +
          ++++++++++++++++++++++++++++++++++++++++
          +    INGREDIENTE 2    +    TOFU        +
          ++++++++++++++++++++++++++++++++++++++++  
          """)
    
    ingrediente = input("Seleccione un ingrediente dentro de la tabla (solo un ingrediente): ")
    if (ingrediente.upper() == 'INGREDIENTE 1' or ingrediente.upper() == '1' or ingrediente.upper() == 'OPCION 1'):
        print("La pizza contiene los siguientes ingredientes: mozzarela, tomate y pimenton")
    elif ( (ingrediente.upper() == 'INGREDIENTE 2' or ingrediente.upper() == '2' or ingrediente.upper() == 'OPCION 2')):
        print("La pizza contiene los siguientes ingredientes: mozzarela, tomate y tofu")
    else:
        print("Debe ingresar una opción de ingrediente dentro de la tabla")
    
elif ( eleccion_pizza.upper() == 'NORMAL' or eleccion_pizza.upper() == 'OPCION 2' or eleccion_pizza.upper() == '2' or eleccion_pizza.upper() == 'NORM'):
    print("""
          ++++++++++++++++++++++++++++++++++++++++++++
          + Su elección de pizza es: NORMAL          +
          ++++++++++++++++++++++++++++++++++++++++++++
          +    INGREDIENTE 1    +    PEPERONI        +
          ++++++++++++++++++++++++++++++++++++++++++++
          +    INGREDIENTE 2    +    JAMON           +
          ++++++++++++++++++++++++++++++++++++++++++++
          +    INGREDIENTE 3    +    SALMÓN          +
          ++++++++++++++++++++++++++++++++++++++++++++  
          """)
    
    ingrediente = input("Seleccione un ingrediente dentro de la tabla (solo un ingrediente): ")
    if (ingrediente.upper() == 'INGREDIENTE 1' or ingrediente.upper() == '1' or ingrediente.upper() == 'OPCION 1'):
        print("La pizza normal contiene los siguientes ingredientes: mozzarela, tomate y peperoni")
    elif ( (ingrediente.upper() == 'INGREDIENTE 2' or ingrediente.upper() == '2' or ingrediente.upper() == 'OPCION 2')):
        print("La pizza normal contiene los siguientes ingredientes: mozzarela, tomate y jamon")
    elif ( (ingrediente.upper() == 'INGREDIENTE 3' or ingrediente.upper() == '3' or ingrediente.upper() == 'OPCION 3')):
        print("La pizza normal contiene los siguientes ingredientes: mozzarela, tomate y salmón")
    else:
        print("Debe ingresar una opción dentro de la tabla")

else:
    print("Debe ingresar una pizaa dentro de las opción indicadas")