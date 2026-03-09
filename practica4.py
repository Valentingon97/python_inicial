def bubble_sort(lista, orden="ASC"):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if orden.upper() == "ASC":
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
            elif orden.upper() == "DESC":
                if lista[j] < lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
            else:
                raise ValueError("El argumento 'orden' debe ser 'ASC' o 'DESC'")
    return lista

# Ejemplos de uso:
print(bubble_sort([5, 2, 9, 1, 5, 100], "ASC"))   # [1, 2, 5, 5, 6, 9]
print(bubble_sort([5, 2, 9, 1, 5, 100], "DESC"))  # [9, 6, 5, 5, 2, 1]


