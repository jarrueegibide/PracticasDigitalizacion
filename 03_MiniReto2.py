"""
La tienda tiene 5 productos, con precios del 10 al 50 (de 10 en 10).

Para cada producto, calcula el precio con descuento:

Si el precio es mayor que 30, aplica un 10% de descuento.

En caso contrario, no hay descuento.

Muestra el número del producto, el precio original y el precio final (print)
"""

# Lista los precios del 10 al 50 (de 10 en 10)
precios = [12,35,11,46,3]

# Recorre cada producto
for i in range(5):
    precio_original = precios[i]

    # Aplica descuento si el precio es mayor que ___
    if precio_original > 30:
        precio_final = precio_original * 0.9 # Aplica un ___% de descuento
    else:
        precio_final = precio_original

    # Muestra el resultado
    print("Producto", i + 1, "- Precio original:", precio_original, "- Precio final:", precio_final)
