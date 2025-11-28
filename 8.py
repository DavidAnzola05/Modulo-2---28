class AnimalDAAC:
    def __init__(self, nombreDAAC, edadDAAC):
        self.nombreDAAC = nombreDAAC
        self.edadDAAC = edadDAAC

    def dormirDAAC(self):
        print(f"{self.nombreDAAC} está durmiendo")

    def comerDAAC(self):
        print(f"{self.nombreDAAC} está comiendo")

class PerroDAAC(AnimalDAAC):
    def ladrarDAAC(self):
        print(f"{self.nombreDAAC}: ¡Guau guau!")

    def jugarDAAC(self):
        print(f"{self.nombreDAAC} está jugando con una pelota")

mi_perroDAAC = PerroDAAC("Buddy", 3)
mi_perroDAAC.dormirDAAC()
mi_perroDAAC.comerDAAC()
mi_perroDAAC.ladrarDAAC()
mi_perroDAAC.jugarDAAC()
print(f"Mi perro se llama {mi_perroDAAC.nombreDAAC} y tiene {mi_perroDAAC.edadDAAC} años")
