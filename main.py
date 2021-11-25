#Ejercicio10: repetir el ejercicio de clase 13 pidiendo la lista por teclado con un  bucle infinito hasta que se introduzca como dato fin. Los elementos de la lista han de ser float.
import statistics

import stats_data as sd
lista = []
while True:
    numeros = float(input("Dime numeros: "))
    if numeros == -999:
        break
    numeros = input("Dime numeros: ")
    if numeros == "fin":
        break
    numeros = float(numeros)
    lista.append(numeros)
lista_num = sd.lista(statistics.mean, statistics.median, statistics.variance)
print(sd.mean(lista))
res = sd.StatsData(lista)
print("Lista números: ", res.l_data)
print("Media: ", res.mean)
print("Mediana: ", res.median)
print("Varianza: ", res.variance)