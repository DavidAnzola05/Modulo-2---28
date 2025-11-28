import json
import pickle


class PersonaDAAC:
    def __init__(self, nombre_DAAC, edad_DAAC):
        self.nombre_DAAC = nombre_DAAC
        self.edad_DAAC = edad_DAAC

    def to_dict_DAAC(self):
        return {
            "nombre_DAAC": self.nombre_DAAC,
            "edad_DAAC": self.edad_DAAC
        }

    @classmethod
    def from_dict_DAAC(cls, data):
        return cls(data["nombre_DAAC"], data["edad_DAAC"])

    def __str__(self):
        return f"{self.nombre_DAAC}, {self.edad_DAAC}"


class ArchivoTextoDAAC:
    def __init__(self, ruta_DAAC):
        self.ruta_DAAC = ruta_DAAC

    def escribir_DAAC(self, contenido_DAAC):
        try:
            with open(self.ruta_DAAC, "w", encoding="utf-8") as archivo_DAAC:
                archivo_DAAC.write(contenido_DAAC)
        except FileNotFoundError:
            print("Ruta inválida")
        except PermissionError:
            print("Sin permisos")

    def leer_DAAC(self):
        try:
            with open(self.ruta_DAAC, "r", encoding="utf-8") as archivo_DAAC:
                return archivo_DAAC.read()
        except FileNotFoundError:
            print("Archivo no encontrado")
        except PermissionError:
            print("Sin permisos")


class ArchivoJSON_DAAC:
    def __init__(self, ruta_DAAC):
        self.ruta_DAAC = ruta_DAAC

    def guardar_personas_DAAC(self, lista_personas_DAAC):
        data = [p.to_dict_DAAC() for p in lista_personas_DAAC]
        try:
            with open(self.ruta_DAAC, "w", encoding="utf-8") as archivo_DAAC:
                json.dump(data, archivo_DAAC, ensure_ascii=False, indent=4)
        except PermissionError:
            print("Sin permisos")

    def cargar_personas_DAAC(self):
        try:
            with open(self.ruta_DAAC, "r", encoding="utf-8") as archivo_DAAC:
                data = json.load(archivo_DAAC)
                return [PersonaDAAC.from_dict_DAAC(p) for p in data]
        except FileNotFoundError:
            print("Archivo JSON no encontrado")
        except json.JSONDecodeError:
            print("JSON corrupto")
        except PermissionError:
            print("Sin permisos")


class ArchivoPickle_DAAC:
    def __init__(self, ruta_DAAC):
        self.ruta_DAAC = ruta_DAAC

    def guardar_DAAC(self, objeto_DAAC):
        try:
            with open(self.ruta_DAAC, "wb") as archivo_DAAC:
                pickle.dump(objeto_DAAC, archivo_DAAC)
        except PermissionError:
            print("Sin permisos")

    def cargar_DAAC(self):
        try:
            with open(self.ruta_DAAC, "rb") as archivo_DAAC:
                return pickle.load(archivo_DAAC)
        except FileNotFoundError:
            print("Archivo Pickle no encontrado")
        except PermissionError:
            print("Sin permisos")
        except pickle.UnpicklingError:
            print("Pickle corrupto")


if __name__ == "__main__":
    p1 = PersonaDAAC("Juan", 25)
    p2 = PersonaDAAC("María", 30)
    p3 = PersonaDAAC("Luis", 20)

    personas_DAAC = [p1, p2, p3]

    texto_DAAC = ArchivoTextoDAAC("personas.txt")
    texto_DAAC.escribir_DAAC("\n".join(str(p) for p in personas_DAAC))

    json_DAAC = ArchivoJSON_DAAC("personas.json")
    json_DAAC.guardar_personas_DAAC(personas_DAAC)
    cargadas_DAAC = json_DAAC.cargar_personas_DAAC()

    pickle_DAAC = ArchivoPickle_DAAC("personas.pkl")
    pickle_DAAC.guardar_DAAC(personas_DAAC)
    rec_pickle_DAAC = pickle_DAAC.cargar_DAAC()

    for p in cargadas_DAAC:
        print("JSON:", p)

    for p in rec_pickle_DAAC:
        print("PICKLE:", p)
