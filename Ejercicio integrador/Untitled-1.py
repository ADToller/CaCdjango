class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_habilidad(self):
        print(f"mi habilidad es: personear")

class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad

    def mostrar_habilidad(self):
        print(f"mi habilidad es: {self.habilidad}")

class EmpleadoArtista(Persona,Artista):
    def __init__(self, nombre, edad, habilidad, salario):
        Persona.__init__(self, nombre, edad)
        Artista.__init__(self,habilidad)
        self.salario = salario

    def mostrar_habilidad(self):
        print(f"mi habilidad es: comer")

    def presentarse(self):
        return Artista.mostrar_habilidad(self)                                                                                                                                     
    
andres = Artista("balala")

andres.presentarse() 