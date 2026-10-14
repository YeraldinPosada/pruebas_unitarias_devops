import pytest
from src.descuentos import (
    aplicar_descuento,
    calcular_descuento,
    descuento_por_volumen,
    descuento_cumulativo,
    descuento_apilado
)

def test_aplicar_descuento_exitoso():
    # Arrange
    precio, porcentaje = 200.0, 20.0
     # Act
    resultado = aplicar_descuento(precio, porcentaje)
    # Assert
    assert resultado == 160.0

def test_aplicar_descuento_precio_negativo_lanza_error():
    # Arrange
    precio_negativo, porcentaje = -50.0, 10.0
    # Act & Assert
    with pytest.raises(ValueError):
        aplicar_descuento(precio_negativo, porcentaje)

def test_descuento_por_volumen_rango_alto():
    # Arrange
    cantidad, precio_unitario = 100, 10.0
    # Act
    resultado = descuento_por_volumen(cantidad, precio_unitario)
    # Assert
    assert resultado == 800.0

def test_descuento_cumulativo_multiples():
    # Arrange
    precio = 100.0
    descuentos = [10.0, 20.0]
    # Act
    resultado = descuento_cumulativo(precio, descuentos)
    # Assert
    assert resultado == 72.0

def test_descuento_porcentaje_invalido_lanza_error():
    # Arrange
    precio, porcentaje_invalido = 100.0, 150.0
    # Act & Assert
    with pytest.raises(ValueError):
        calcular_descuento(precio, porcentaje_invalido)
