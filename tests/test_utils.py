import pytest
from src.utils import (
    celsius_a_fahrenheit,
    fahrenheit_a_celsius,
    celsius_a_kelvin,
    kelvin_a_celsius,
    calcular_imc,
    categorizar_imc,
    calcular_edad,
    es_bisiesto,
    dias_en_mes,
    es_primo,
    mcd,
    mcm
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

def test_conversiones_temperatura_adicionales():
    assert fahrenheit_a_celsius(77.0) == 25.0
    assert celsius_a_kelvin(0.0) == 273.15
    assert kelvin_a_celsius(273.15) == 0.0

def test_calcular_imc_errores():
    with pytest.raises(ValueError):
        calcular_imc(-70.0, 1.75)
    with pytest.raises(ValueError):
        calcular_imc(70.0, 0.0)

def test_categorizar_imc_rangos():
    assert categorizar_imc(17.0) == "Bajo peso"
    assert categorizar_imc(22.0) == "Normal"
    assert categorizar_imc(27.0) == "Sobrepeso"
    assert categorizar_imc(32.0) == "Obesidad"

def test_calcular_edad_error():
    with pytest.raises(ValueError):
        calcular_edad(2030, 2026)

def test_es_bisiesto_variaciones():
    assert es_bisiesto(2023) is False  # No divisible por 4
    assert es_bisiesto(1900) is False  # Divisible por 100 pero no por 400
    assert es_bisiesto(2000) is True   # Divisible por 400

def test_dias_en_mes_casos():
    assert dias_en_mes(1, 2026) == 31
    assert dias_en_mes(4, 2026) == 30
    assert dias_en_mes(2, 2024) == 29  # Bisiesto
    assert dias_en_mes(2, 2023) == 28  # No bisiesto
    with pytest.raises(ValueError):
        dias_en_mes(13, 2026)

def test_es_primo_variaciones():
    assert es_primo(1) is False
    assert es_primo(4) is False

def test_mcd_y_mcm():
    assert mcd(48, 18) == 6
    assert mcm(4, 6) == 12

def test_mcm_bug_evidencia():
    # Prueba para evidenciar el comportamiento anómalo o bug en MCM ante entradas límites (ej. ceros o negativos)
    # Matemáticamente mcm(0, 5) debería ser 0, pero con divisiones enteras o ausencia de validación puede fallar o lanzar excepción.
    resultado = mcm(-4, 6)
    assert resultado == 0
