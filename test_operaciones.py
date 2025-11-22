import pytest
from operaciones import sumar_elementos, promedio, contar_mayores_a_limite


def test_sumar_elementos():
    assert sumar_elementos([1.5, 2.5, 3.0]) == 7.0
    assert sumar_elementos([-1, 1]) == 0
    assert sumar_elementos([]) == 0


def test_promedio():
    assert promedio([2.0, 4.0, 6.0]) == 4.0
    assert promedio([10]) == 10
    assert promedio([]) == 0.0


def test_contar_mayores_a_limite():
    assert contar_mayores_a_limite([1, 5, 10, 2], 4) == 2
    assert contar_mayores_a_limite([0, -1, -5], 0) == 0
    assert contar_mayores_a_limite([10, 20, 30], 5) == 3
