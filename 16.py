from abc import ABC, abstractmethod
import math

class Forma(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def calcular_area(self):
        pass

    @abstractmethod
    def calcular_perimetro(self):
        pass

    def __str__(self):
        return f"{self.nombre} (Área: {round(self.calcular_area(), 2)})"

    def __repr__(self):
        return f"Forma('{self.nombre}')"

    def __lt__(self, otra):
        return self.calcular_area() < otra.calcular_area()


class Circulo(Forma):
    def __init__(self, radio):
        if radio <= 0:
            raise ValueError("El radio debe ser mayor que cero.")
        super().__init__("Círculo")
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio


class Rectangulo(Forma):
    def __init__(self, base, altura):
        if base <= 0 or altura <= 0:
            raise ValueError("Base y altura deben ser mayores que cero.")
        super().__init__("Rectángulo")
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)


class Triangulo(Forma):
    def __init__(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Todos los lados deben ser mayores que cero.")
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Los lados no forman un triángulo válido.")
        super().__init__("Triángulo")
        self.a = a
        self.b = b
        self.c = c

    def calcular_area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def calcular_perimetro(self):
        return self.a + self.b + self.c


if __name__ == "__main__":
    formas = [
        Circulo(5),
        Rectangulo(4, 6),
        Triangulo(3, 4, 5),
        Circulo(2),
        Rectangulo(10, 2)
    ]

    print("=== FORMAS Y SUS ÁREAS ===")
    for f in formas:
        print(f"{f.nombre}: Área = {round(f.calcular_area(), 2)}, Perímetro = {round(f.calcular_perimetro(), 2)}")

    print("\n=== ORDENADAS POR ÁREA (MENOR A MAYOR) ===")
    formas_ordenadas = sorted(formas)
    for f in formas_ordenadas:
        print(f)
    