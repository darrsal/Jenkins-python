def sumar_elementos(numeros: list[float]) -> float:
    """
    Recibe un arreglo de números decimales y regresa la sumatoria.
    """
    return sum(numeros)


def promedio(numeros: list[float]) -> float:
    """
    Recibe un arreglo de números decimales y regresa el promedio.
    """
    if len(numeros) == 0:
        return 0.0
    return sum(numeros) / len(numeros)


def contar_mayores_a_limite(numeros: list[float], limite: float) -> int:
    """
    Recibe un arreglo de números decimales y un límite;
    regresa la cantidad de elementos que excedan el límite.
    """
    return sum(1 for n in numeros if n > limite)


if __name__ == "__main__":
    datos = [1.5, 2.3, 5.0, 7.8, 3.1]

    print("Sumatoria:", sumar_elementos(datos))
    print("Promedio:", promedio(datos))
    print("Cantidad mayores a 4.0:", contar_mayores_a_limite(datos, 4.0))
