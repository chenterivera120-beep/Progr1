class Perro():
    tipo="Perro"
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color

    def sonidos(self):
        return "Guau, Guau"

class Gato():
    tipo="Gato"
    def __init__(self, nombre, color):
        self.nombre=nombre
        self.color = color

    def sonidos(self):
        return "Miau, Miau"
    
class Pez():
    tipo="Pez"
    def __init__(self, nombre, color):
        self.nombre=nombre
        self.color=color

    def sonidos(self):
        return "Gluglu, Gluglu"