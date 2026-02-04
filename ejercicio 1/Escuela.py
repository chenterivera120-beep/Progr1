class Alumno():
    def __init__(self, nombre, matricula, calif):
        self.nombre=nombre
        self.matricula=matricula
        self.calif = []

    def agregar_calificacion(self.calificacion):
        self.calif.append(calificacion)
        
    def calcular_promedio(self):
        return sum(self.calificacion)
        
    def estado_final(self):
        promedio = self.calcular_promedio()
        return "Aprovado" if promedio >=70 else "Reprovado"
        
class Grupo:
    def __init__(self, nombre_grupo):
        self.nombre_grupo = nombre_grupo
        self.alumnos = []

    def agregar_alumno(self):
        self.alumnos.append(alumno)

    def mostrar_promedio(self):
        print(f"Promedio del grupo {self.nombre_grupo}:")
        for alumno in self.alumnos:
            promeido = alumno.calcular_promedio()
            estado = alumno.estado_final()
            print(f"{alumno-nombre} ({alumno.matrucula}): Promedio = {promedio:.2f}, Estado = {estado}")

    def mejor_alumno(self):
        if not self.alumnos:
            print("No hay alumnos en el grupo.")
            mejor = max(self.alumnos, key=lambda alumno: alumno.calcular_promedio())
            print(f"El mejor alumno es {mejor.nombre} ({mejor.matricula}) con un promedio de {mejor.calcular_promedio():.2f}.")
        


