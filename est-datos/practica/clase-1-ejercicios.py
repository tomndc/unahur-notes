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

def main():
    repetir_palabra()

if __name__ == "__main__":
    main()