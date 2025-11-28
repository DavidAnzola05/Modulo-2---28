class PersonaConRepresentacionDAAC:
    def __init__(self, nombreDAAC, edadDAAC):
        self.nombreDAAC = nombreDAAC
        self.edadDAAC = edadDAAC

    def __str__(self):
        return f"Persona(Nombre: {self.nombreDAAC}, Edad: {self.edadDAAC})"

    def __repr__(self):
        return f"PersonaConRepresentacionDAAC('{self.nombreDAAC}', {self.edadDAAC})"


pDAAC = PersonaConRepresentacionDAAC("Elena", 28)

print(pDAAC)
print(str(pDAAC))
print(repr(pDAAC))

