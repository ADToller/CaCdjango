#Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con
#cada palabra que contiene y la cantidad de veces que aparece (frecuencia).

def frase_a_diccionario(texto):
    lista_de_palabras = texto.split()
    diccionario = {}
    for palabra in lista_de_palabras:
        if palabra in diccionario:
            diccionario[palabra] += 1
        else:
            diccionario[palabra] = 1
    return diccionario



print("ingrese una frase:")
frase = input()

print(frase_a_diccionario(frase))
