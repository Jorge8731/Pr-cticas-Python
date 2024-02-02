"""3. Teniendo presente el uso y concepto de diccionarios en Python, realizar un
programa con los siguientes requerimientos (4 ptos)
Reglas:
- Crear un diccionario con los keys de nombre, apellidos, edad y dni.
- Pedir por consola los valores para estos keys.
- Mostrar en pantalla sólo los values del diccionario
- Agregar un key adicional con el nombre de “profesion” y un valor para este key
nuevo.
- Eliminar el key dni y mostrar el nuevo diccionario."""

diccionario = {}

diccionario['nombre'] = input('Ingrese el nombre: ')
diccionario['apellidos'] = input('Ingrese los apellidos: ')
diccionario['edad'] = int(input('Ingrese la edad: '))
diccionario['dni'] = int(input('Ingrese el dni: '))

print("Los values son:")
for value in diccionario.values():
    print(value)

diccionario['profesión'] = input('Ingrese la profesión: ')

print("El diccionario creado es: {}".format(diccionario))

del diccionario['dni']

print("El diccionario actualizado es: {}".format(diccionario))