#Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una
#cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero
#del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el
#ejercicio tanto de manera iterativa como recursiva.

def get_int():
    dato_correcto = False
    while not dato_correcto:
        try:
            valor = int(input("Ingrese un numero entero: "))
            return valor
        except ValueError:
            print("No es un numero entero, intente nuevamente.")
        else:
             dato_correcto = True


def get_int_recursivo():
        try:
            valor = int(input("Ingrese un numero entero: "))
            return valor
        except ValueError:
            print("No es un numero entero, intente nuevamente.")
            get_int_recursivo()



numero = get_int_recursivo()

print(numero)