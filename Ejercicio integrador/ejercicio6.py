#Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los
#siguientes métodos para la clase:
# - Un constructor, donde los datos pueden estar vacíos.
# - Los setters y getters para cada uno de los atributos. Hay que validar las entradas de
#   datos.
# - mostrar(): Muestra los datos de la persona.
# - Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad


class Persona():
    def __init__(self,nombre="",edad=0,dni=""):
        self._nombre = nombre
        self._edad = edad
        self._dni = dni

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def set_nombre(self, nuevo_nombre):
        if nuevo_nombre.isalpha():
            self._nombre = nuevo_nombre
        else:
            print("El dato ingresado es incorrecto")

    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def set_edad(self, edad):
        if int(edad) >= 0:
            self._edad = edad
        else:
            print("El dato ingresado es incorrecto")


    @property
    def dni(self):
        return self._dni
    
    @dni.setter
    def set_dni(self, dni):
        if len(dni) == 8:
            self._dni = dni
        else:
            print("El dato ingresado es incorrecto")

    def mostrar(self):
        print(f"Nombre: {self._nombre}, Edad: {self._edad}, DNI: {self._dni}")

    def es_mayor_de_edad(self):
        return self._edad >= 18    
        

# Crear una instancia de la clase sin proporcionar valores
persona_vacia = Persona()

# Establecer valores utilizando los métodos setters
persona_vacia.set_nombre("Juan")
persona_vacia.set_edad("30")
persona_vacia.set_dni("12345678")

# Mostrar los datos de la instancia utilizando los métodos getters
persona_vacia.mostrar()

# Verificar si es mayor de edad
if persona.es_mayor_de_edad():
    print("Es mayor de edad.")
else:
    print("No es mayor de edad.")