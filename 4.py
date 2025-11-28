class PersonaConComparacion:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __eq__(self, other):
        if not isinstance(other, PersonaConComparacion):
            return NotImplemented
        return self.nombre == other.nombre and self.edad == other.edad

p1 = PersonaConComparacion("Manuel", 40)
p2 = PersonaConComparacion("Manuel", 40)
p3 = PersonaConComparacion("Manuel", 30)

print(f"p1 == p2: {p1 == p2}")
print(f"p1 == p3: {p1 == p3}")
