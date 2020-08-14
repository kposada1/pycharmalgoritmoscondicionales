'''Un obrero necesita calcular su salario semanal, el cual se obtiene de la sig. manera:
Si trabaja 40 horas o menos se le paga $16 por hora
Si trabaja mas de 40 horas se le paga $16 por cada una de las primeras 40 horas y
$20 por cada hora extra.'''

ht = int(input("Ingrese las horas trabajadas: "))

if ht>40:
    he = ht-40
    ss = he*20+40*16
else:
    ss = ht * 16

print(f"Su salario semanal es: {ss}")