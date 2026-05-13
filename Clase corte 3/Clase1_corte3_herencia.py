

class Pedido:
    def __init__(self, codigo, descripcion):
        self.__codigo = codigo
        self.__descripcion = descripcion
        self.__estado = None
        self.__pedidos = []

    def get_codigo(self):
        return self.__codigo
    
    def get_descripcion(self):
        return self.__descripcion

    def set_estado(self):
        return self.__estado

    def agregar_pedido(self, pedido):
        self.__pedidos.append(pedido)
    
    def mostrar_pedido(self):
        for p in self.__pedidos:
            print(f"\nPedido #{p+1}")
            print(f"Codigo: {p.__codigo}")
            print(f"Descripcion: {p.__descripcion}")
            print(f"Estado: {p.__estado}")


class Empleado:
    def __init__(self, nombre, identificacion, salario):
        self.__nombre = nombre
        self.__identificacion = identificacion
        self.__salario = salario
    
    def get_nombre(self):
        return self.__nombre
    
    def get_identificacion(self):
        return self.__identificacion

    def mostrar_informacion(self):
        print(f"Nombre: {self.__nombre} - {self.__identificacion} - {self.__salario}")


class Mesero(Empleado):
    def __init__(self, nombre, identificacion, salario, mesas_atendidas):
        super().__init__(nombre, identificacion, salario)
        self.__mesas_atendidas = mesas_atendidas




class Cocinero(Empleado):
    def __init__(self, nombre, identificacion, salario, especialidad):
        super().__init__(nombre, identificacion, salario)
        self.especialidad = especialidad
    

m1 = Mesero("Pedro", "100001", 1600000, 3)
m2 = Mesero("Ana", "100002", 1650000, 2)

c1 = Cocinero("Maria", "100003", 1700000,)
c2 = Cocinero("Juan", "100004", 1750000,)





