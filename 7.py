class AnimalDAAC:
    def __init__(self, nombreDAAC):
        self.nombreDAAC = nombreDAAC

    def hacer_sonidoDAAC(self):
        print(f"{self.nombreDAAC} hace un sonido")

class PerroDAAC(AnimalDAAC):
    def ladrarDAAC(self):
        print(f"{self.nombreDAAC}: ¡Guau!")
