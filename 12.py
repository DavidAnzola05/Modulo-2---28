class PersonaConComparacionDAAC:
    def __init__(self, nombreDAAC, edadDAAC):
        self.nombreDAAC = nombreDAAC
        self.edadDAAC = edadDAAC

    def __eq__(self, otherDAAC):
        if not isinstance(otherDAAC, PersonaConComparacionDAAC):
            return NotImplemented
        return self.nombreDAAC == otherDAAC.nombreDAAC and self.edadDAAC == otherDAAC.edadDAAC


p1DAAC = PersonaConComparacionDAAC("Manuel", 40)
p2DAAC = PersonaConComparacionDAAC("Manuel", 40)
p3DAAC = PersonaConComparacionDAAC("Manuel", 30)

print(f"p1DAAC == p2DAAC: {p1DAAC == p2DAAC}")
print(f"p1DAAC == p3DAAC: {p1DAAC == p3DAAC}")
