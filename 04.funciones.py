#01. Funciones sin argumentos
'''
Las funciones sin argumentos estan compuestas por la definición de la función y el conjunto de instrucciones que realizara la función,
definidas las funciones procedemos a llamar a la función para visualizar su ejecución.
'''
def mensaje(): #Se declara la función
    #Cuerpo de funcion.
    print("Estamos aprendiendo Python")
    print("Estamos aprendiendo instrucciones basicas")
    print("Poco a poco iremos aprendiendo")

#Visualizar a la funcion
mensaje()

def suma():
    num1= 5
    num2= 7
    print(num1+num2)

suma()
suma()

#02. Funciones con argumentos
'''
Una función con argumentos, es la que contienen argumentos en su declaración los cuales serán operados por las instrucciones dentro de la función.
Definida la funcion, definimos los valores de cada argumento, luego llamamos a la función para visualizar el resultado.
'''
#Declaramos función y argumentos
def suma (num1, num2):
    print(num1 + num2)

#llamamos a la función y definimos el valor de los argumentos
suma(5,7)
suma(2,3)
suma(35,358)

#03. Funciones con argumentos y return
'''
Cuando se utiliza return en una función, esta sentencia hace que la ejecución de la función se detenga de forma inmediaa haciendo que se devuelva el valor
especificado dentro de la sentencia. Si el valor o resultado en return no existe o no esta definido este no mostrara nada.
Para llamar a la función, primero se debe definir los parametros y luego esta se ejecutara en base a las intrucciones contenidas, retornando el resulto especifico.
'''
def suma(num1, num2):
    return num1 + num2

#Imprimo valor de función suma
print(suma(5,14))