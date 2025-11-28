class PersonaDAAC:
    def __init__(self, nombreDAAC, edadDAAC):
        self.nombreDAAC = nombreDAAC
        self.edadDAAC = edadDAAC

    def saludarDAAC(self):
        print(f"Hola, soy {self.nombreDAAC} y tengo {self.edadDAAC} años.")


class EstudianteDAAC:
    def __init__(self, nombreDAAC, edadDAAC, matriculaDAAC, carreraDAAC):
        self.nombreDAAC = nombreDAAC
        self.edadDAAC = edadDAAC
        self.matriculaDAAC = matriculaDAAC
        self.carreraDAAC = carreraDAAC

    def estudiarDAAC(self):
        print(f"{self.nombreDAAC} (Matrícula: {self.matriculaDAAC}) está estudiando {self.carreraDAAC}.")

    def saludarDAAC(self):
        print(f"¡Hola! Soy {self.nombreDAAC}, estudiante de {self.carreraDAAC}.")


class EmpleadoDAAC:
    def __init__(self, nombreDAAC, edadDAAC, id_empleadoDAAC, puestoDAAC, salarioDAAC):
        self.nombreDAAC = nombreDAAC
        self.edadDAAC = edadDAAC
        self.id_empleadoDAAC = id_empleadoDAAC
        self.puestoDAAC = puestoDAAC
        self.salarioDAAC = salarioDAAC

    def trabajarDAAC(self):
        print(f"{self.nombreDAAC} (ID: {self.id_empleadoDAAC}) está trabajando como {self.puestoDAAC}.")

    def reportar_salarioDAAC(self):
        print(f"El salario de {self.nombreDAAC} es ${self.salarioDAAC}.")


estudiante1DAAC = EstudianteDAAC("Laura", 20, "A001", "Ingeniería de Software")
empleado1DAAC = EmpleadoDAAC("Roberto", 35, "E101", "Desarrollador Senior", 60000)

print("\n--- Demostración de Estudiante ---")
estudiante1DAAC.saludarDAAC()
estudiante1DAAC.estudiarDAAC()

print("\n--- Demostración de Empleado ---")
empleado1DAAC.trabajarDAAC()
empleado1DAAC.reportar_salarioDAAC()
