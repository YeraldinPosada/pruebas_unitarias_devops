
import pytest
from src.calculadora import sumar, dividir, multiplicar, promedio, calcular_area_rectangulo

def test_sumar_positivos():
    # Arrange
    a, b = 7, 5
    # Act
    resultado = sumar(a, b)
    # Assert
    assert resultado == 12

def test_dividir_por_cero_lanza_error():
    # Act & Assert
    with pytest.raises(ValueError):
        dividir(10, 0)

def test_multiplicar_negativos():
    # Arrange
    a, b = -4, -3
    # Act
    resultado = multiplicar(a, b)
    # Assert
    assert resultado == 12

def test_promedio_lista_numeros():
    # Arrange
    lista = [2, 4, 6, 8]
    # Act
    resultado = promedio(lista)
    # Assert
    assert resultado == 5.0

def test_calcular_area_rectangulo_positivos():
    # Arrange
    base, altura = 6, 4
    # Act
    resultado = calcular_area_rectangulo(base, altura)
    # Assert
    assert resultado == 24

