
#EJERCICIO 1
"""
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        print("Sonido generico")


class Perro(Animal):
    
    def hacer_sonido(self):
        print(f"{self.nombre} esta ladrando")

class Gato(Animal):

    def hacer_sonido(self):
        print(f"{self.nombre} esta maullando")

Animales = [
    Perro("Lucas"),
    Gato("Michi"),
    Perro("Roky")
]

for a in Animales:
    a.hacer_sonido()

"""

#EJERCICIO 2
"""
class Vehiculo:
    def __init__(self, velocidad_max, marca):
        self.velocidad_max = velocidad_max
        self.marca = marca

    def mover(self):
        print("vehiculo en movimiento")

class Auto(Vehiculo):

    def mover(self):
        print(f"El auto, con marca {self.marca} circula por la carretera a una velocidad {self.velocidad_max} Km/h")
    
    def encender_ac(self):
        print(f"El auto esta encendido")

class Moto(Vehiculo):

    def mover(self):
        print(f"La moto, con marca {self.marca} esta acelerando a una velocidad {self.velocidad_max} Km/h")
    
    def hacer_caballito(self):
        print("La moto esta realizando la acrobacia llamada caballito")

Vehiculos = [
    Auto(30, "Ford"),
    Moto(45, "Suzuki")
]


Vehiculos[0].encender_ac()

for m in Vehiculos:
    m.mover()

Vehiculos[1].hacer_caballito()

"""
