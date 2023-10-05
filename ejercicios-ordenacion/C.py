def ssiff(A):
    """
    Encuentra el número máximo de películas que se pueden ver.

    Args:
        A: Lista de horarios de las películas.

    Returns:
        Número máximo de películas.
    """

    n = len(A)
    # Ordenar los horarios de las películas.
    A.sort()

    # Inicializar el contador de películas.
    num_peliculas = 0

    # Iterar sobre los horarios de las películas.
    for i in range(n):
        # Si la película actual termina antes de que empiece la siguiente,podemos verla.
        if A[i][1] < A[i + 1][0]:
            num_peliculas += 1
        else:
            pass

    return num_peliculas