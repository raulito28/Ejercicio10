#Ejercicio10: repetir el ejercicio de clase 13 pidiendo la lista por teclado con un  bucle infinito hasta que se introduzca como dato fin. Los elementos de la lista han de ser float.
import stats_data as sd
lista = []
numeros = input("Dime numeros: ")
numeros2 = input("Dime numeros: ")
while True:
    numeros = float(input("Dime numeros: "))
    numeros2 = str(input("Dime numeros: "))
    if numeros2 == "fin":
        break
    lista.append(numeros)
    lista.append(numeros2)

res = sd.StatsData(numeros)
print("Lista números: ")
print("Media: ", res.mean)
print("Mediana: ", res.median)
print("Varianza: ", res.variance)