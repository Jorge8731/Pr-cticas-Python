"""1. Usando los tipos de datos y sus conversiones realizar lo siguiente. (3 ptos)
Reglas:
- Pedir por consola nombre y edad de un usuario.
- Edad tiene que ser tipo entero, para esto apoyarse de la conversión de datos
- Identificar los tipos de datos ingresados y mostrarlos en pantalla.
- Pedir los nombres y edades para dos trabajadores y finalmente
agregarlos a una lista. Mostrar la suma de las edades de los
trabajadores localizándolos por la posición en la lista."""

lista = []

for i in range(2):
    nombre = input("Ingrese el nombre del trabajador {}: ".format(i+1))
    edad = int(input("Ingrese la edad del trabajador {}: ".format(i+1)))
    lista.append((nombre, edad))

print("El tipo de dato de nombre es: {}".format(type(nombre)))
print("El tipo de dato de edad es: {}".format(type(edad)))

print("La lista es: {}".format(lista))

suma_edades = lista[0][1] + lista[1][1]

print("La suma de las edades de los trabajadores es: {}".format(suma_edades))