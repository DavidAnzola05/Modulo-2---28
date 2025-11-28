class PersonaConPropiedad:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        if not isinstance(nuevo_nombre, str) or len(nuevo_nombre) == 0:
            raise ValueError("El nombre debe ser una cadena no vacía.")
        self._nombre = nuevo_nombre

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, nueva_edad):
        if not isinstance(nueva_edad, int) or nueva_edad < 0:
            raise ValueError("La edad debe ser un entero positivo.")
        self._edad = nueva_edad

p = PersonaConPropiedad("Sofía", 22)
print(f"Nombre: {p.nombre}, Edad: {p.edad}")
p.edad = 23
print(f"Nueva edad: {p.edad}")

try:
    p.nombre = ""
except ValueError as e:
    print(f"Error al cambiar nombre: {e}")
