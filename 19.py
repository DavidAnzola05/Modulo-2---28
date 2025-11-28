class PersonaDAAC:
    def __init__(self, nombre_DAAC, edad_DAAC):
        self.nombre_DAAC = nombre_DAAC
        self.edad_DAAC = edad_DAAC

    def __str__(self):
        return f"{self.nombre_DAAC} - {self.edad_DAAC}"


class ColeccionPersonasDAAC:
    def __init__(self):
        self._datos_DAAC = []

    def agregar_DAAC(self, persona_DAAC):
        self._datos_DAAC.append(persona_DAAC)

    def __len__(self):
        return len(self._datos_DAAC)

    def __getitem__(self, indice_DAAC):
        return self._datos_DAAC[indice_DAAC]

    def __setitem__(self, indice_DAAC, valor_DAAC):
        self._datos_DAAC[indice_DAAC] = valor_DAAC

    def __iter__(self):
        return IteradorPersonasDAAC(self._datos_DAAC)


class IteradorPersonasDAAC:
    def __init__(self, datos_DAAC):
        self.datos_DAAC = datos_DAAC
        self.pos_DAAC = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.pos_DAAC >= len(self.datos_DAAC):
            raise StopIteration
        valor_DAAC = self.datos_DAAC[self.pos_DAAC]
        self.pos_DAAC += 1
        return valor_DAAC


class DiccionarioPersonasDAAC:
    def __init__(self):
        self._mapa_DAAC = {}

    def agregar_DAAC(self, clave_DAAC, persona_DAAC):
        self._mapa_DAAC[clave_DAAC] = persona_DAAC

    def __getitem__(self, clave_DAAC):
        return self._mapa_DAAC[clave_DAAC]

    def __setitem__(self, clave_DAAC, valor_DAAC):
        self._mapa_DAAC[clave_DAAC] = valor_DAAC

    def __len__(self):
        return len(self._mapa_DAAC)

    def __iter__(self):
        for clave_DAAC in self._mapa_DAAC:
            yield clave_DAAC


def generador_edades_DAAC(personas_DAAC):
    for p in personas_DAAC:
        yield p.edad_DAAC


if __name__ == "__main__":
    p1_DAAC = PersonaDAAC("Ana", 21)
    p2_DAAC = PersonaDAAC("Luis", 30)
    p3_DAAC = PersonaDAAC("Carlos", 18)

    coleccion_DAAC = ColeccionPersonasDAAC()
    coleccion_DAAC.agregar_DAAC(p1_DAAC)
    coleccion_DAAC.agregar_DAAC(p2_DAAC)
    coleccion_DAAC.agregar_DAAC(p3_DAAC)

    print(len(coleccion_DAAC))
    print(coleccion_DAAC[1])

    coleccion_DAAC[1] = PersonaDAAC("María", 25)

    for persona_DAAC in coleccion_DAAC:
        print(persona_DAAC)

    mapa_DAAC = DiccionarioPersonasDAAC()
    mapa_DAAC.agregar_DAAC("A1", p1_DAAC)
    mapa_DAAC.agregar_DAAC("B2", p2_DAAC)

    print(mapa_DAAC["A1"])

    for clave_DAAC in mapa_DAAC:
        print(clave_DAAC, mapa_DAAC[clave_DAAC])

    edades_DAAC = generador_edades_DAAC(coleccion_DAAC)
    for e in edades_DAAC:
        print(e)
