"""2.Usando el concepto y funciones de listas, realizar un programa con
las siguiente características (3 ptos):
Reglas:
- Crear una lista con 10 valores random o aleatorios (Pista: Usar el método
append y for)
- Llenar otra lista con sus cubos.
- Llenar una lista nueva con sus cuadrados.
- Mostrar de manera inversa la suma de ambas listas creadas."""

lista = []

for i in range(10):
    valor = int(input("El valor {} de la lista es: ".format(i+1)))
    lista.append(valor)

cubo = [valor ** 3 for valor in lista]
cuadrado = [valor ** 2 for valor in lista]

print("Lista de valores:", lista)
print("Lista de cubos:", cubo)
print("Lista de cuadrados:", cuadrado)

cubo.reverse()
cuadrado.reverse()

suma_listas = []

for i in range(len(lista)):
    suma_listas.append(cubo[i] + cuadrado[i])

print("La suma inversa de ambas listas es:", suma_listas)