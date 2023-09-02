#Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una
#persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es
#opcional. Crear los siguientes métodos para la clase:
# - Un constructor, donde los datos pueden estar vacíos.
# - Los setters y getters para cada uno de los atributos. El atributo no se puede modificar
#directamente, sólo ingresando o retirando dinero.
# - mostrar(): Muestra los datos de la cuenta.
# - ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es
#negativa, no se hará nada.
# - retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números
#rojos.

class Cuenta(Persona):
    def __init__(self, nombre, edad, dni, titular, cantidad):
        super().__init__(nombre, edad, dni)
        self._titular = ""
        self._cantidad = 0

    @property
    def titular(self):
        return self._titular
    
    @titular.setter
    def set_titular(self, nuevo_titular):
        self._titular = nuevo_titular

    @property
    def cantidad(self):
        return self._cantidad

    @cantidad.setter
    def set_cantidad(self, nueva_cantidad):
        self._cantidad = nueva_cantidad

    def mostrar(self):
        print(f"Titular: {self._titular}, Cantidad: {self._cantidad}") 
    
    def ingresar(self, cantidad):
        if cantidad >= 0:
            self._cantidad += cantidad
    
    def retirar(self, cantidad):
        if cantidad >= 0:
            self._cantidad -= cantidad
        
