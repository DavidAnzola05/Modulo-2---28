from abc import ABC, abstractmethod
import math


class FormaGeometricaDAAC(ABC):

    @abstractmethod
    def calcular_area_DAAC(self):
        pass

    @abstractmethod
    def calcular_perimetro_DAAC(self):
        pass

    @abstractmethod
    def nombre_DAAC(self):
        pass

    def __str__(self):
        return f"{self.nombre_DAAC()} | Área: {round(self.calcular_area_DAAC(), 2)} | Perímetro: {round(self.calcular_perimetro_DAAC(), 2)}"

    def __repr__(self):
        return f"{self.nombre_DAAC()}(area={self.calcular_area_DAAC()}, perimetro={self.calcular_perimetro_DAAC()})"


class CirculoDAAC(FormaGeometricaDAAC):

    def __init__(self, radio_DAAC):
        self.radio_DAAC = radio_DAAC

    @property
    def radio_DAAC(self):
        return self._radio_DAAC

    @radio_DAAC.setter
    def radio_DAAC(self, valor):
        if valor <= 0:
            raise ValueError("Radio inválido")
        self._radio_DAAC = valor

    def calcular_area_DAAC(self):
        return math.pi * (self.radio_DAAC ** 2)

    def calcular_perimetro_DAAC(self):
        return 2 * math.pi * self.radio_DAAC

    def nombre_DAAC(self):
        return "CírculoDAAC"

    @classmethod
    def desde_diametro_DAAC(cls, diametro):
        return cls(diametro / 2)

    @staticmethod
    def es_radio_valido_DAAC(valor):
        return valor > 0


class RectanguloDAAC(FormaGeometricaDAAC):

    def __init__(self, base_DAAC, altura_DAAC):
        self.base_DAAC = base_DAAC
        self.altura_DAAC = altura_DAAC

    @property
    def base_DAAC(self):
        return self._base_DAAC

    @base_DAAC.setter
    def base_DAAC(self, valor):
        if valor <= 0:
            raise ValueError("Base inválida")
        self._base_DAAC = valor

    @property
    def altura_DAAC(self):
        return self._altura_DAAC

    @altura_DAAC.setter
    def altura_DAAC(self, valor):
        if valor <= 0:
            raise ValueError("Altura inválida")
        self._altura_DAAC = valor

    def calcular_area_DAAC(self):
        return self.base_DAAC * self.altura_DAAC

    def calcular_perimetro_DAAC(self):
        return 2 * (self.base_DAAC + self.altura_DAAC)

    def nombre_DAAC(self):
        return "RectánguloDAAC"


class TrianguloDAAC(FormaGeometricaDAAC):

    def __init__(self, a_DAAC, b_DAAC, c_DAAC):
        self.a_DAAC = a_DAAC
        self.b_DAAC = b_DAAC
        self.c_DAAC = c_DAAC

    @staticmethod
    def validar_lados_DAAC(a, b, c):
        return a + b > c and a + c > b and b + c > a

    @property
    def a_DAAC(self):
        return self._a_DAAC

    @a_DAAC.setter
    def a_DAAC(self, valor):
        if valor <= 0:
            raise ValueError("Lado inválido")
        if hasattr(self, "_b_DAAC") and hasattr(self, "_c_DAAC"):
            if not self.validar_lados_DAAC(valor, self._b_DAAC, self._c_DAAC):
                raise ValueError("Lados no válidos")
        self._a_DAAC = valor

    @property
    def b_DAAC(self):
        return self._b_DAAC

    @b_DAAC.setter
    def b_DAAC(self, valor):
        if valor <= 0:
            raise ValueError("Lado inválido")
        if hasattr(self, "_a_DAAC") and hasattr(self, "_c_DAAC"):
            if not self.validar_lados_DAAC(self._a_DAAC, valor, self._c_DAAC):
                raise ValueError("Lados no válidos")
        self._b_DAAC = valor

    @property
    def c_DAAC(self):
        return self._c_DAAC

    @c_DAAC.setter
    def c_DAAC(self, valor):
        if valor <= 0:
            raise ValueError("Lado inválido")
        if hasattr(self, "_a_DAAC") and hasattr(self, "_b_DAAC"):
            if not self.validar_lados_DAAC(self._a_DAAC, self._b_DAAC, valor):
                raise ValueError("Lados no válidos")
        self._c_DAAC = valor

    def calcular_perimetro_DAAC(self):
        return self.a_DAAC + self.b_DAAC + self.c_DAAC

    def calcular_area_DAAC(self):
        s = self.calcular_perimetro_DAAC() / 2
        return math.sqrt(s * (s - self.a_DAAC) * (s - self.b_DAAC) * (s - self.c_DAAC))

    def nombre_DAAC(self):
        return "TriánguloDAAC"


if __name__ == "__main__":
    f1_DAAC = CirculoDAAC(10)
    f2_DAAC = RectanguloDAAC(5, 12)
    f3_DAAC = TrianguloDAAC(7, 8, 9)
    f4_DAAC = CirculoDAAC.desde_diametro_DAAC(20)

    formas_DAAC = [f1_DAAC, f2_DAAC, f3_DAAC, f4_DAAC]
    formas_ordenadas_DAAC = sorted(formas_DAAC, key=lambda x: x.calcular_area_DAAC())

    for f in formas_ordenadas_DAAC:
        print(f)
