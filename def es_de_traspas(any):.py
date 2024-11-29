def es_de_traspas(any):
    """Retorna True si l'any és de traspàs, False en cas contrari."""
    if (any % 4 == 0 and any % 100 != 0) or (any % 400 == 0):
        return True
    else:
        return False

# Proves de la funció
anys_a_provar = [2000, 1900, 2020, 2021, 1600, 2024]

for any in anys_a_provar:
    if es_de_traspas(any):
        print(f"L'any {any} és de traspàs.")
    else:
        print(f"L'any {any} NO és de traspàs.")