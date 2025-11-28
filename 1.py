class PersonaDAAC:
    def __init__(self, nombreDAAC, edadDAAC):
        self.nombreDAAC = nombreDAAC
        self.edadDAAC = edadDAAC

    def saludarDAAC(self):
        print(f"Hola, soy {self.nombreDAAC} y tengo {self.edadDAAC} años.")

    def cumplir_aniosDAAC(self):
        self.edadDAAC += 1
        print(f"¡Feliz cumpleaños! Ahora {self.nombreDAAC} tiene {self.edadDAAC} años.")
