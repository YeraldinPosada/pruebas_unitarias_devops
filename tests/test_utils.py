import pytest
from src.utils import (
    celsius_a_fahrenheit,
    calcular_imc,
    calcular_edad,
    es_bisiesto,
    es_primo
)

def test_celsius_a_fahrenheit_exitoso():
    # Arrange
    celsius = 25.0
    # Act
    resultado = celsius_a_fahrenheit(celsius)
    # Assert
    assert resultado == 77.0

def test_calcular_imc_normal():
    peso, altura = 70.0, 1.75
    # Act
    resultado = calcular_imc(peso, altura)
    # Assert
    assert round(resultado, 2) == 22.86

def test_calcular_edad_valida():
    # Arrange
    anio_nacimiento, anio_actual = 1995, 2026
    # Act
    resultado = calcular_edad(anio_nacimiento, anio_actual)
    # Assert
    assert resultado == 31

def test_es_bisiesto_afirmativo():
    # Arrange: El año 2024 es bisiesto
    anio = 2024
    # Act
    resultado = es_bisiesto(anio)
    # Assert
    assert resultado is True

def test_es_primo_con_numero_primo():
    # Arrange: El número 13 es primo
    numero = 13
    # Act
    resultado = es_primo(numero)
    # Assert
    assert resultado is True
