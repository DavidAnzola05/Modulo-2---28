from datetime import datetime
import uuid

class CuentaBancaria:
    def __init__(self, titular, tipo_cuenta):
        self.titular = titular
        self.tipo_cuenta = tipo_cuenta
        self.fecha_apertura = datetime.now()
        self.__saldo = 0.0
        self.__historial = []
        self.__numero_cuenta = self.__generar_numero_cuenta()

    def depositar(self, monto):
        if not self.__validar_monto(monto):
            return "Monto inválido"
        self.__saldo += monto
        self.__registrar_transaccion("DEPÓSITO", monto)
        return f"Depósito exitoso. Nuevo saldo: {self.__saldo}"

    def retirar(self, monto):
        if not self.__validar_monto(monto):
            return "Monto inválido"
        if monto > self.__saldo:
            return "Fondos insuficientes"
        self.__saldo -= monto
        self.__registrar_transaccion("RETIRO", monto)
        return f"Retiro exitoso. Nuevo saldo: {self.__saldo}"

    def consultar_saldo(self):
        return self.__saldo

    def obtener_historial(self):
        return self.__historial

    def transferir(self, monto, otra_cuenta):
        if not isinstance(otra_cuenta, CuentaBancaria):
            return "Cuenta destino inválida"
        if not self.__validar_monto(monto):
            return "Monto inválido"
        if monto > self.__saldo:
            return "Fondos insuficientes"
        self.__saldo -= monto
        otra_cuenta.__saldo += monto
        self.__registrar_transaccion("TRANSFERENCIA ENVIADA", monto, otra_cuenta.__numero_cuenta)
        otra_cuenta.__registrar_transaccion("TRANSFERENCIA RECIBIDA", monto, self.__numero_cuenta)
        return "Transferencia exitosa"

    def __validar_monto(self, monto):
        return isinstance(monto, (int, float)) and monto > 0

    def __registrar_transaccion(self, tipo, monto, cuenta_relacionada=None):
        transaccion = {
            "tipo": tipo,
            "monto": monto,
            "cuenta_relacionada": cuenta_relacionada,
            "fecha": datetime.now()
        }
        self.__historial.append(transaccion)

    def __generar_numero_cuenta(self):
        return str(uuid.uuid4())[:12]

c1 = CuentaBancaria("Daniel", "Ahorros")
c2 = CuentaBancaria("María", "Corriente")

print(c1.depositar(500))
print(c1.retirar(200))
print(c1.transferir(100, c2))
print("Saldo C1:", c1.consultar_saldo())
print("Saldo C2:", c2.consultar_saldo())
print("Historial C1:", c1.obtener_historial())
