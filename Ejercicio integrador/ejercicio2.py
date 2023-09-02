#Escribir una función que calcule el mínimo común múltiplo entre dos números
def mcd(n1, n2):
    
    while n2:
        resto = n1 % n2 
        n1 = n2
        n2 = resto
    return n1

def mcm(n1, n2):
    return (n1*n2)/mcd(n1,n2)


print("Ingrese un numero:")
a = int(input())
print("Ingrese otro numero")
b = int(input())

print("El mcm es: ", mcm(a,b))