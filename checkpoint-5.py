#Crea un bucle for de Python.

frutas = ['manzana', 'platano', 'naranja', 'limón', 'fresa']
for fruta in frutas:
    print(fruta)

#Crea una función de Python llamada suma que tome tres argumentos y devuelva la suma de los tres.

def suma(a, b, c):
    return a+ b + c

solucion = suma(1, 2, 3)

print('El resultado de la suma es:', solucion)

#Crea una función lambda con la misma funcionalidad que la función de suma que acabas de crear. 

suma_lambda = lambda a, b, c: a + b + c

solucion = suma_lambda(1, 2, 3)
print('El resultado de la suma es:', solucion)

#Utilizando la siguiente lista y variable, determina si el valor de la variable coincide o no con un valor en la lista. 

nombre = 'Enrique'
lista_nombre = 'Jessica', 'Paul', 'George', 'Henry', 'Adán'

if nombre in lista_nombre:
    print('Estás en la lista')

else:
    print('Lo siento, tu nombre no aparece en esta lista')