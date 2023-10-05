def prevencion_riesgos(A, x):
    """
    Encuentra el número mínimo de góndolas necesarias para los niños.

    Args:
        A: Lista de pesos de los niños.
        x: Peso máximo por góndola.

    Returns:
        Número mínimo de góndolas.
    """

    n = len(A)
    # Ordenar la lista de pesos.
    A.sort()

    # Inicializar el contador de góndolas.
    num_gondolas = 0

    # Iterar sobre los niños.
    for i in range(n):
        # Si el peso del niño actual es menor o igual al peso máximo,podemos meterlo en la góndola actual.
        if A[i] <= x:
            num_gondolas += 1
        else:
            # Si el peso del niño actual es mayor que el peso máximo,necesitamos una nueva góndola.
            num_gondolas += 2

    return num_gondolas