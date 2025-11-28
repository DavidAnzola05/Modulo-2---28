class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

    def cumplir_anios(self):
        self.edad += 1
        print(f"¡Feliz cumpleaños! Ahora {self.nombre} tiene {self.edad} años.")
