"""
MINIRETO: CLASIFICACIÓN DE JUGADORES

Completa los huecos ___ para:
- Crear una lista de puntuaciones
- Recorrerla con un bucle for
- Clasificar a los jugadores
"""

print("=== TORNEO DE VIDEOJUEGO ===")

# 1. CREAR LISTA DE PUNTUACIONES
puntuaciones = [30, 20, 10, 5, 25]

# 2. MOSTRAR TODOS LOS JUGADORES
print("\n--- JUGADORES Y PUNTUACIONES ---")
numero_jugador = 1
for puntos in puntuaciones:
    print("Jugador", numero_jugador, "- Puntos:", puntos)
    numero_jugador = numero_jugador + 1

# 3. CLASIFICAR JUGADORES
print("\n--- CLASIFICACIÓN ---")
for puntos in puntuaciones:
    if puntos > 20:
        print(puntos, "puntos - ¡CLASIFICADO!")
    else:
        print(puntos, "puntos - Eliminado")

# 4. CALCULAR PUNTUACIÓN TOTAL
print("\n--- ESTADÍSTICAS ---")
total = 0
for puntos in puntuaciones:
    total = total + puntos
print("Puntuación total del torneo:", total)
