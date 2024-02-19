""" Programa que convierte porcentajes en calificaciones. """

escore_estudiantes = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

calificaciones_estudiantes = {}

for student in escore_estudiantes:
    score = escore_estudiantes[student]
    if score > 90:
        calificaciones_estudiantes[student] = "Outstanding"
    elif score > 80:
        calificaciones_estudiantes[student] = "Exceeds Expectations"
    elif score > 70:
        calificaciones_estudiantes[student] = "Acceptable"
    else:
        calificaciones_estudiantes[student] = "Fail"


print(calificaciones_estudiantes)
