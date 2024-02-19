""" programa que calcule la estatura promedio de los estudiantes a partir de una Lista de estaturas. """

estudiantes_altura = input("Ingrese las alturas de los estudiantes: ").split()

for n in range(0, len(estudiantes_altura)):
    estudiantes_altura[n] = int(estudiantes_altura[n])

total_altura = 0

for alturas in estudiantes_altura:
    total_altura += alturas
# print(total_altura)

numero_de_estudiantes = 0
for estudiantes in estudiantes_altura:
    numero_de_estudiantes += 1
# print(numero_de_estudiantes)

promedio_altura = round(total_altura / numero_de_estudiantes)
print(promedio_altura)
