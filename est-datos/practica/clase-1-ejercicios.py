import math
import random

# Ejercicio 1
def hola_mundo():
    """
    Primer programa en Python. Escribir un programa que imprima por pantalla "Hola mundo".
    """
    print("Hola mundo!")

# Ejercicio 2
def hola_mundo_variable():
    """
    Escribir un programa que cargue en una variable la cadena de caracteres “Hola mundo” y luego la imprima por pantalla.
    """
    texto = "Hola mundo!"
    print(texto)

# Ejercicio 3
def operaciones_matematicas():
    """
    Escribir un programa que cree dos variables enteras, le asigne números arbitrarios (cualquiera) y muestre por pantalla: 
    - La suma
    - La resta
    - La multiplicación 
    - La división entera 
    - El resto de la división entera.
    """
    x = random.randint(1, 170)
    y = random.randint(1, 436)
    print("Suma:", x + y, "Resta:", x - y, "Multiplicación:", x * y, "División entera:", x // y, "Resto:", x % y)

# Ejercicio 4
def perimetro_area():
    """
    Implementar algoritmos que permitan:
    
    - Calcular el perímetro y el área de un rectángulo, dada su base y su altura
    - Calcular el perímetro y el área de un círculo dado su radio.
    - Declarar las variables necesarias y asignarle números arbitrarios
    """
    base = random.randint(1, 400)
    altura = random.randint(1, 200)
    radio = random.randint(1, 300)
    print("Rectángulo - Perímetro:", 2 * (base + altura), "Área:", base * altura)
    print("Círculo - Perímetro:", 2 * math.pi * radio, "Área:", math.pi * radio ** 2)

# Ejercicio 5
def celsius_a_fahrenheit():
    """
    Escribir un programa que pida una temperatura en grados Celsius al usuario. 
    Realice la transformación de grados Celsius a Fahrenheit e imprima el resultado por pantalla.
    """
    celsius = float(input("Ingresá una temperatura en Celsius: "))
    print("Temperatura en Fahrenheit:", 1.8 * celsius + 32)

# Ejercicio 6
def calcular_sueldo():
    """
    Escribir un programa que pregunte por el número de horas trabajadas y el costo por hora. 
    Después debe mostrar por pantalla el sueldo que corresponde.
    """
    horas = int(input("Ingresar horas trabajadas: "))
    costo = int(input("Ingrese costo por hora: "))
    print("Sueldo correspondiente:", horas * costo)

# Ejercicio 7
def calcular_imc():
    """
    Escribir un programa que pida un peso (en kg) y una estatura (en metros): 
    - Calcule el índice de masa corporal y lo almacene en una variable. 
    - Luego debe muestrar por pantalla la frase: "El índice de masa corporal es: <imc>". 
    - Donde <imc> es el índice de masa corporal calculado.
    """
    peso = float(input("Ingrese peso en kg: "))
    estatura = float(input("Ingrese estatura en metros: "))
    imc = peso / (estatura ** 2)
    print("El índice de masa corporal es:", round(imc, 2))

# Ejercicio 8
def calcular_inversion():
    """
    Escribir un programa que pregunte una cantidad a invertir, el interés anual y el número de año: 
    - Muestre por pantalla el capital obtenido en la inversión.
    """
    cantidad = float(input("Ingrese una cantidad a invertir: "))
    interes = float(input("Ingrese el interés anual (%): "))
    años = int(input("Ingrese cantidad de años: "))
    capital = cantidad * (1 + interes / 100) ** años
    print("Inversión final:", round(capital, 2))

# Ejercicio 9
def formatos_nombre():
    """
    Escribir un programa que pregunte un nombre completo en la consola y después muestre por pantalla ese nombre tres veces: 
    - Una con todas las letras minúsculas, 
    - Otra con todas las letras mayúsculas 
    - Y otra solo con la primera letra del nombre y de los apellidos en mayúscula. 
    Se puede introducir un nombre combinando mayúsculas y minúsculas como se quiera.
    """
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    print(nombre.lower(), apellido.lower(), nombre.upper(), apellido.upper(), nombre.capitalize(), apellido.capitalize())

# Ejercicio 10
def contar_letras_nombre():
    """
    Escribir un programa que pregunte un nombre en la consola y después muestre por pantalla: "El <NOMBRE> tiene <N> letras".
    El <NOMBRE> es el nombre ingresado todo en mayúsculas y <N> es el número de letras que tienen el nombre.
    """
    nombre = input("Nombre: ")
    print("El nombre", nombre.upper(), "tiene", len(nombre), "letras.")

# Ejercicio 11
def a_por_z():
    '''
    Escribir un programa que pida una palabra, reemplace todas las letras "a" por "z" y muestre el resultado por pantalla.
    '''
    palabra = input("Palabra: ").replace('a','z')
    print(palabra)

# Ejercicio 12
def palabras_concatenadas():
    '''
    Escribir un programa que pida dos palabras y muestre por pantalla la concatenacion de ambas.
    '''
    palabra1 = input("Palabra 1:")
    palabra2 = input("Palabra 2:")
    print(palabra1 + palabra2)

# Ejercicio 13
def repetir_palabra():
    '''
    Escribir un programa que pida una palabra y un número N y muestre por pantalla la palabra ingresada repetida N veces.
    '''
    palabra  = input("Palabra: ")
    numero = int(input("Número: "))
    print(palabra * numero)

# Ejercicio 14
def mayor_de_edad():
    '''
    Escribir un programa que pregunte una edad y muestre por pantalla si es mayor de edad o no.
    '''
    edad = int(input("Edad: "))
    if edad < 18:
        print("Es menor de edad.")
    else:
        print("Es mayor de edad.")

# Ejercicio 15
def contraseña():
    contraseña = "contraseña"
    pregunta = str(input("Ingrese contraseña: " ))
    if pregunta.lower() == contraseña.lower():
        print("Correcto")
    else:
        print("Incorrecto")

# Ejercicio 15 bis
def menor_o_mayor():
    '''
    Escribir un programa pida dos números enteros e informe por pantalla cual es menor de los dos, 
    si son iguales, indicarlo por separado.
    '''
    num1 = int(input("num 1:"))
    num2 = int(input("num 2: "))

    if num1 > num2: 
        print(f"{num2} es menor")
    else:
        print(f"{num1} es menor")

#Ejercicio 16 
def par_o_impar():
    '''
    Escribir un programa que pida un número entero e indique si dicho número es par o impar
    '''
    num = int(input("Ingrese un número entero: "))

    if num % 2 == 0:
        print(f"El número {num} es par.")
    else:
        print(f"El número {num} es impar.")

# Ejercicio 17
def pagar_impuestos():
    '''
    Para pagar un determinado impuesto se debe ser mayor de 18 años y tener unos ingresos iguales o superiores a $100000 mensuales. 
    Escribir un programa que pregunte la edad y los ingresos mensuales y muestre por pantalla si se debe pagar o no.
    '''
    edad = int(input("Edad? "))
    ingresos = int(input("Ingresos? "))
    if edad >= 18 and ingresos >= 100000:
        print("Debe pagar!")
    else:
        print("No debe pagar! woo!")

# Ejercicio 18
def semana():
    '''
    Escribir un programa que pida un número entero del 1 al 7 y muestre por pantalla el día de la semana correspondiente.
    Controlar que el número se encuentre en el rango correcto, si no es así, informar un error.
    Por ejemplo, si el número es 2 el día es martes.
    '''
    num = int(input("Ingrese un número del 1 al 7: "))

    if num == 1:
        print("El día correspondiente es Lunes.")
    elif num == 2:
        print("El día correspondiente es Martes.")
    elif num == 3:
        print("El día correspondiente es Miércoles.")
    elif num == 4:
        print("El día correspondiente es Jueves.")
    elif num == 5:
        print("El día correspondiente es Viernes.")
    elif num == 6:
        print("El día correspondiente es Sábado.")
    elif num == 7:
        print("El día correspondiente es Domingo.")
    else:
        print("Error: el número debe estar entre 1 y 7.")

# Ejercicio 19
def grupos_escuela():
    '''
    Las y los alumnas y alumnos de un curso se han dividido en dos grupos A y B de acuerdo al género y el nombre. 
    El grupo A esta formado por las personas de genero femenino con una inicial de nombre anterior a la M 
    y las personas de genero masculino con un inicial de nombre posterior a la N y el grupo B por el resto. 
    Escribir un programa que pregunte la inicial y el género, y muestre por pantalla el grupo que corresponde.
    '''
    grupo_A_femenino= {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"}
    grupo_A_masculino = {"O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"}

    inicial = input("Inicial: ").strip().upper()
    genero = input("Género (M/F): ").strip().upper()

    if (genero == "F" and inicial in grupo_A_femenino) or \
    (genero == "M" and inicial in grupo_A_masculino):
        print("Grupo A.")
    else:
        print("Grupo B.")

# Ejercicio 20
def precio_a_cliente():
    '''
    Escribir un programa para una empresa que tiene salas de juegos para todas las edades.
    Quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. 
    El programa debe preguntar la edad del cliente y mostrar el precio de la entrada. 
    Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar $5 
    y si es mayor de 18 años, $10.
    '''
    edad = int(input("Edad? "))
    if edad < 4:
        print("Gratis")
    elif edad >= 4 and edad <= 18:
        print("Precio: 5$")
    else:
        print("Precio: 10$") 

# Ejercicio 21
def uno_al_cien():
    '''
    Mostrar por pantalla todos los números enteros entre 1 y 100, 
    hacerlo usando un bucle while y tambien con un bucle for.
    '''
    num = 1
    while num <= 100:
        print(num)
        num = num + 1

# Ejercicio 21 bis
def uno_al_cien_for():
    for num in range(1, 101):
        print(num)

# Ejercicio 22
def numeros_entre():
    '''
    Escribir un programa que pida dos números enteros e imprima todos los números enteros entre ellos.
    '''
    num1 = int(input("num1: "))
    num2 = int(input("num2: "))
    while num1 != num2:
        print(num1)
        num1 = num1 + 1

#Ejercicio 23
def nombre_repetido():
    '''
    Escribir un programa que pregunte un nombre en la consola y un número entero e imprima por pantalla 
    en líneas distintas el nombre tantas veces como el número introducido.
    '''
    nombre = input("nombre: ")  
    num = int(input("num: ")) 

    for i in range(num):  
        print(nombre)  

# Ejercicio 24
def numeros_impares():
    '''
    Escribir un programa que pida un número entero positivo y muestre por pantalla 
    todos los números impares desde 1 hasta ese número.
    '''
    num = int(input("Num: "))

    if num > 0: 
        for i in range(1, num + 1, 2):
            print(i)
    else:
        print("No es positivo")

# Ejercicio 25 
def triangulo_rectángulo():
    '''
    Escribir un programa que pida un número entero y muestre por pantalla un triángulo rectángulo.
    '''
    num = int(input("Ingrese un número entero positivo: "))

    if num > 0:
        for i in range(1, num + 1):
            print("* " * i)
    else:
        print("Error: Debe ingresar un número entero positivo.")


def main():
    menor_o_mayor()

if __name__ == "__main__":
    main()