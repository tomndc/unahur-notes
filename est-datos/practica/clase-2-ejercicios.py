#Ejercicio 14
def mayor_de_edad():
    '''
    Escribir un programa que pregunte una edad y muestre por pantalla si es mayor de edad o no.
    '''
    edad = int(input("Edad: "))
    if edad < 18:
        print("Es menor de edad.")
    else:
        print("Es mayor de edad.")

def main():
    mayor_de_edad()

if __name__ == "__main__":
    main()