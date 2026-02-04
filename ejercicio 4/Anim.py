class Animales:
    def __init__(self, nombre, color, patas):
        self.nombre=nombre
        self.color=color
        self.patas=patas


class Conejo(Animales):
    def sonido(self):
        print("Sinif, Snif")

    def caract(self):
        print(f"Hola, mi conejo se llama {self.nombre}, su color es {self.color} y tiene {self.patas} patas")

class Ornitorrinco(Animales):
    def __init__(self, nombre, color, patas, pico):
        super().__init__(nombre, color, patas)
        self.pico=pico
    def sonido(self):
        print("Greerrrr")

    def caract(self):
        print(f"Mi ornito se llama {self.nombre}, es color {self.color}, tiene {self.patas} patas y su pico mide {self.pico} cm.")

class Dinosaurio(Animales):
    tipo = "dinosaurio"
    
    def sonido(self):
        print("Rugido de Godzilla")

    def caracteristicas(self):
        print(f"mi dino se llama {self.nombre}, es color {self.color}, tiene {self.patas} patas y es un {Dinosaurio.tipo}")