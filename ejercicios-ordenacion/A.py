def pasar_lista(A):
    """
    Pasa lista de alumnos y devuelve el número de alumnos únicos.

    Args:
        A: Lista de identificadores de alumnos.

    Returns:
        Número de alumnos únicos.
    """

    n = len(A)
    # Ordenar la lista de identificadores.
    A.sort()

    # Inicializar el contador de alumnos únicos a 0.
    num_alumnos_unicos = 1

    # Iterar sobre la lista de identificadores.
    for i in range(1, n):
        # Si el identificador actual es igual al anterior,no es un alumno único.
        if A[i] == A[i - 1]:
            continue

        # Si el identificador actual es diferente del anterior,es un alumno único.
        num_alumnos_unicos += 1

    return num_alumnos_unicos
