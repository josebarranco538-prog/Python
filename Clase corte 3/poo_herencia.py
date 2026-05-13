# ============================================
# Sistema simple de transporte
# Ejemplo para explicar POO en Python
# ============================================


# ==============================
# CLASE BASE: Persona
# ==============================
class Persona:
    def __init__(self, nombre, identificacion):
        # Atributos privados (encapsulamiento)
        self.__nombre = nombre
        self.__identificacion = identificacion

    # Métodos de acceso (getters)
    def get_nombre(self):
        return self.__nombre

    def get_identificacion(self):
        return self.__identificacion

    def mostrar_informacion(self):
        print(f"Nombre: {self.__nombre} | ID: {self.__identificacion}")


# ==============================
# CLASE HIJA: Conductor
# ==============================
class Conductor(Persona):
    def __init__(self, nombre, identificacion, licencia):
        # Se reutiliza el constructor de Persona
        super().__init__(nombre, identificacion)
        self.__licencia = licencia
        self.__vehiculo = None  # inicialmente no tiene vehículo

    def asignar_vehiculo(self, vehiculo):
        # Validamos si el vehículo está disponible
        if vehiculo.get_estado() == "disponible":
            self.__vehiculo = vehiculo
            vehiculo.set_estado("ocupado")
            print(f"Vehículo {vehiculo.get_placa()} asignado a {self.get_nombre()}")
        else:
            print(f"No se puede asignar, el vehículo {vehiculo.get_placa()} ya está ocupado")

    def mostrar_informacion(self):
        # Sobrescribimos el método del padre
        super().mostrar_informacion()
        print(f"Licencia: {self.__licencia}")

        if self.__vehiculo:
            print(f"Vehículo asignado: {self.__vehiculo.get_placa()}")
        else:
            print("Sin vehículo asignado")


# ==============================
# CLASE BASE: Vehiculo
# ==============================
class Vehiculo:
    def __init__(self, placa, marca):
        # Encapsulamiento
        self.__placa = placa
        self.__marca = marca
        self.__estado = "disponible"

    # Métodos de acceso
    def get_placa(self):
        return self.__placa

    def get_estado(self):
        return self.__estado

    def set_estado(self, estado):
        self.__estado = estado

    def mostrar_info(self):
        print(f"Placa: {self.__placa} | Marca: {self.__marca} | Estado: {self.__estado}")


# ==============================
# CLASE HIJA: Carro
# ==============================
class Carro(Vehiculo):
    def __init__(self, placa, marca, puertas):
        super().__init__(placa, marca)
        self.__puertas = puertas

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Puertas: {self.__puertas}")


# ==============================
# CLASE HIJA: Moto
# ==============================
class Moto(Vehiculo):
    def __init__(self, placa, marca, cilindraje):
        super().__init__(placa, marca)
        self.__cilindraje = cilindraje

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Cilindraje: {self.__cilindraje}")


# ==============================
# PROGRAMA PRINCIPAL
# ==============================

# Creación de objetos
c1 = Conductor("Juan", "123", "A1")
c2 = Conductor("Maria", "456", "B2")

v1 = Carro("ABC123", "Toyota", 4)
v2 = Carro("XYZ789", "Mazda", 2)
v3 = Moto("MTR456", "Yamaha", 150)


print("\n--- ASIGNACIÓN DE VEHÍCULOS ---")
c1.asignar_vehiculo(v1)

# Este intento debe fallar porque ya está ocupado
c2.asignar_vehiculo(v1)


print("\n--- INFORMACIÓN DE CONDUCTORES ---")
c1.mostrar_informacion()
print()
c2.mostrar_informacion()


print("\n--- INFORMACIÓN DE VEHÍCULOS ---")
v1.mostrar_info()
print()
v2.mostrar_info()
print()
v3.mostrar_info()