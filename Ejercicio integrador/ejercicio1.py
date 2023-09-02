# Escribir una función que calcule el máximo común divisor entre dos números.

def mcd(n1, n2):
    
    while n2:
        resto = n1 % n2 
        n1 = n2
        n2 = resto
    return n1



print("Ingrese un numero:")
a = int(input())
print("Ingrese otro numero:")
b = int(input())

print("el MCD es:", mcd(a,b))
