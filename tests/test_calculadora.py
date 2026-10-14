
import pytest
from src.calculadora import sumar, dividir, multiplicar, promedio, calcular_area_rectangulo, restar, potencia, raiz_cuadrada, promedio, maximo, minimo, calcular_area_rectangulo, calcular_perimetro_rectangulo

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

def test_restar_positivos():
    # Arrange
    a, b = 10, 4
    # Act
    resultado = restar(a, b)
    # Assert
    assert resultado == 6
def test_potencia_exitoso():
    # Arrange
    base, exponente = 2, 3
    # Act
    resultado = potencia(base, exponente)
    # Assert
    assert resultado == 8
def test_raiz_cuadrada_exitoso():
    # Arrange
    valor = 9
    # Act
    resultado = raiz_cuadrada(valor)
    # Assert
    assert resultado == 3.0
def test_promedio_lista_numeros():
    # Arrange
    lista = [2, 4, 6, 8]
    # Act
    resultado = promedio(lista)
    # Assert
    assert resultado == 5.0

def test_promedio_lista_vacia_lanza_error():
    # Act & Assert
    with pytest.raises(ValueError):
        promedio([])

def test_maximo_lista():
    # Arrange
    lista = [3, 9, 2, 7]
    # Act
    resultado = maximo(lista)
    # Assert
    assert resultado == 9

def test_maximo_lista_vacia_lanza_error():
    # Act & Assert
    with pytest.raises(ValueError):
        maximo([])

def test_minimo_lista():
    # Arrange
    lista = [5, 2, 8, 10]
    # Act
    resultado = minimo(lista)
    # Assert
    assert resultado == 2

def test_minimo_lista_vacia_lanza_error():
    # Act & Assert
    with pytest.raises(ValueError):
        minimo([])

def test_calcular_area_rectangulo_positivos():
    # Arrange
    base, altura = 6, 4
    # Act
    resultado = calcular_area_rectangulo(base, altura)
    # Assert
    assert resultado == 24

def test_calcular_area_rectangulo_negativo_lanza_error():
    # Act & Assert
    with pytest.raises(ValueError):
        calcular_area_rectangulo(-2, 4)

def test_calcular_perimetro_rectangulo_positivos():
    # Arrange
    base, altura = 5, 3
    # Act
    resultado = calcular_perimetro_rectangulo(base, altura)
    # Assert
    assert resultado == 16

def test_calcular_perimetro_rectangulo_negativo_lanza_error():
    # Act & Assert
    with pytest.raises(ValueError):
        calcular_perimetro_rectangulo(5, -1)
