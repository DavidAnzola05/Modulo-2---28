class PersonaConPropiedadDAAC:
    def __init__(self, nombreDAAC, edadDAAC):
        self._nombreDAAC = nombreDAAC
        self._edadDAAC = edadDAAC

    @property
    def nombreDAAC(self):
        return self._nombreDAAC

    @nombreDAAC.setter
    def nombreDAAC(self, nuevo_nombreDAAC):
        if not isinstance(nuevo_nombreDAAC, str) or len(nuevo_nombreDAAC) == 0:
            raise ValueError("El nombre debe ser una cadena no vacía.")
        self._nombreDAAC = nuevo_nombreDAAC

    @property
    def edadDAAC(self):
        return self._edadDAAC

    @edadDAAC.setter
    def edadDAAC(self, nueva_edadDAAC):
        if not isinstance(nueva_edadDAAC, int) or nueva_edadDAAC < 0:
            raise ValueError("La edad debe ser un entero positivo.")
        self._edadDAAC = nueva_edadDAAC


pDAAC = PersonaConPropiedadDAAC("Sofía", 22)
print(f"Nombre: {pDAAC.nombreDAAC}, Edad: {pDAAC.edadDAAC}")
pDAAC.edadDAAC = 23
print(f"Nueva edad: {pDAAC.edadDAAC}")

try:
    pDAAC.nombreDAAC = ""
except ValueError as eDAAC:
    print(f"Error al cambiar nombre: {eDAAC}")
