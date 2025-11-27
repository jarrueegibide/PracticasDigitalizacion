"""
MINIRETO: CONTROL DE VIDEOJUEGO

Estás programando un videojuego simple. Completa los huecos ___ para que:
- Muestre los niveles del 1 al 5
- Cada nivel da 100 puntos de experiencia
- Clasifique los niveles por dificultad
"""

print("=== VIDEOJUEGO - CONTROL DE NIVELES ===")

# 1. MOSTRAR TODOS LOS NIVELES
print("\n--- NIVELES DISPONIBLES ---")
for i in range(1, ___):
    print("Nivel", i)

# 2. CALCULAR EXPERIENCIA POR NIVEL
print("\n--- EXPERIENCIA POR NIVEL ---")
for i in range(1, 6):
    experiencia = i * ___
    print("Nivel", i, "- Experiencia:", experiencia)

# 3. CLASIFICAR DIFICULTAD
print("\n--- DIFICULTAD ---")
for i in range(1, 6):
    if i > ___:
        print("Nivel", i, "- DIFÍCIL")
    else:
        print("Nivel", i, "- FÁCIL")
