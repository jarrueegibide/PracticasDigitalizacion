# Se piden los datos al usuario
nombre = input("¿Cómo se llama el cliente? ")
cantidad = int(input("¿Cuántas entradas quiere comprar? "))
precio = float(input("¿Cuál es el precio de una entrada? "))

#1. Calcula el total a pagar (multiplicando cantidad por precio).
total = cantidad*precio
#2. Muestra por pantalla el nombre del cliente y el total a pagar.
print("Total a pagar:", total)

