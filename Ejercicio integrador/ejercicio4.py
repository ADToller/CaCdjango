#Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada
#palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función
#que reciba el diccionario generado con la función anterior y devuelva una tupla con la
#palabra más repetida y su frecuencia.

def frase_a_diccionario(texto):
    lista_de_palabras = texto.split()
    diccionario = {}
    for palabra in lista_de_palabras:
        if palabra in diccionario:
            diccionario[palabra] += 1
        else:
            diccionario[palabra] = 1
    return diccionario

def palabra_mas_repetida(dic_de_palabras):
    veces_repetidas = max(dic_de_palabras.values())
    for palabra, veces in dic_de_palabras.items():
        if veces == veces_repetidas:
            mas_repetida = palabra
    return mas_repetida, veces_repetidas
        

print("ingrese una frase:")
frase = input()

print(frase_a_diccionario(frase))

print("La palabra mas repetida fue:")
print(palabra_mas_repetida(frase_a_diccionario(frase)))