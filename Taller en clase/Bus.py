


from vehiculos import Vehiculos

class Bus(Vehiculos):
    def __init__(self, placa, marca, capacidad):
        super().__init__(placa, marca)
        self.__capacidad = capacidad

    def mostrar_capacidad(self):
        return self.__capacidad
    
    def mostrar_info(self):
        return print(f"- Placa: {self.__placa}\n- Marca: {self.__marca}\n- Capacidad: {self.__capacidad}")
    


