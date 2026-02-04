from Escuela import *

alumno1 = Alumno("Renata Rangel", 34214213)
alumno2 = Alumno("Marco Serrano", 39283)
alumno3 = Alumno("Alfredo Gaspar", 12314)
alumno4 = Alumno("Marco Antonio", 4392334)
alumno5 = Alumno("Jose Alfredo", 12314)

alumno1.agregar_calificacion(95)
alumno1.agregar_calificacion(90)

alumno2.agregar_calificacion(95)
alumno2.agregar_calificacion(70)
alumno2.agregar_calificacion(98)

alumno3.agregar_calificacion(65)
alumno3.agregar_calificacion(72)
alumno3.agregar_calificacion(61)
alumno3.agregar_calificacion(65)

alumno4.agregar_calificacion(82)
alumno4.agregar_calificacion(23)
alumno4.agregar_calificacion(75)
alumno4.agregar_calificacion(48)

alumno5.agregar_calificacion(90)
alumno5.agregar_calificacion(46)
alumno5.agregar_calificacion(97)
alumno5.agregar_calificacion(54)

print(f"La alumna {alumno1.nombre} tiene promedio de: {alumno1.calcular_promedio()}")
print(f"La alumna {alumno2.nombre} tiene promedio de: {alumno2.calcular_promedio()}")
print(f"La alumna {alumno3.nombre} tiene promedio de: {alumno3.calcular_promedio()}")
print(f"La alumna {alumno4.nombre} tiene promedio de: {alumno4.calcular_promedio()}")
print(f"La alumna {alumno5.nombre} tiene promedio de: {alumno5.calcular_promedio()}")

grupo1=Grupo("Progra")
grupo1.agregar_alumno(alumno1)
grupo1.agregar_alumno(alumno2)
grupo1.agregar_alumno(alumno3)
grupo1.agregar_alumno(alumno4)
grupo1.agregar_alumno(alumno5)
print(grupo1.mostrar_promedios())
print(grupo1.mejor_alumno())
