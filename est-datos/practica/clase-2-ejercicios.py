# Ejercicio 1
def hola_mundo():
    '''
    Escribir un procedimiento que muestre por pantalla la cadena “Hola mundo!!!” cada
    vez que se la invoque
    '''
    print("Hola mundo!")

# Ejercicio 2
def imprimir_nombre(nombre):
    '''
    Escribir un procedimiento que se le pase por parámetros una cadena <nombre> y
    muestre por pantalla: “Hola <nombre>!!!”
    '''
    print(f"Hola {nombre}!!!")

# Ejercicio 3
def factorial(numero):
    '''
    Escribir una función que calcule y retorne el factorial de un numero natural
    '''
    
    if numero < 0:
        return "Error: El número debe ser un número natural (entero no negativo)."
    
    if numero == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, numero + 1):
            resultado *= i
        return resultado

#Ejercicio 4
def factura_total(importe, iva=21): # Esto es un parámetro con valor por defecto. :B
    '''
    Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función
    debe recibir el importe sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la
    factura. 
    Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.
    '''
    iva_total = iva / 100
    importe_total = importe + iva_total
    return importe_total


# Main
def main():
    factura_total(200)
    factura_total(200, 50,1)

if __name__ == "__main__":
    main()
