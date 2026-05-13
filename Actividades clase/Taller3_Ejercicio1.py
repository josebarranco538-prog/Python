

class Estudiante: #Iniciamos creando el objeto en este caso "Estudiante"

    def __init__(self, nombre, codigo): #Definimos las caracteristicas del objeto estudiante: nombre, codigo
       self.nombre = nombre
       self.codigo = codigo
       self.cursos = []

    def matricular_curso(self, curso):
        self.cursos.append(curso)

    def mostrar_info(self):
        print(f"Nombre: {self.nombre} - Codigo: {self.codigo}")
        for c in self.cursos:
            print(f"Carrera")




