'''Determinar si un alumno aprueba a reprueba un curso, sabiendo que aprobara si su
promedio de tres calificaciones es mayor o igual a 70; reprueba en caso contrario.'''

calif1 = int(input("Ingrese calificacion 1: "))
calif2 = int(input("Ingrese calificacion 2: "))
calif3 = int(input("Ingrese calificacion 3: "))

prom = (calif1 + calif2 + calif3)/3
if prom>=70:
    print(f"El alumno aprueba el curso, con una calificacion de {prom}")
else:
    print(f"El alumno reprueba el curso, con una calificacion de {prom}")