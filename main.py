# Ejercicio10: repetir el ejercicio de clase 13 pidiendo la lista por teclado con un  bucle infinito hasta que se
# introduzca como dato fin. Los elementos de la lista han de ser float.
import statistics

import stats_data as sd
lista_numeros = []
while True:
    numeros = input("Dime numeros: ")
    if numeros == "fin":
        break
    numeros = float(numeros)
    lista_numeros.append(numeros)

res = sd.StatsData(lista_numeros)
print("Lista números: ", res.l_data)
print("Media: ", res.mean)
print("Mediana: ", res.median)
print("Varianza: ", res.variance)