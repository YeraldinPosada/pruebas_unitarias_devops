import pytest
from src.descuentos import (
    aplicar_descuento,
    calcular_descuento,
    calcular_precio_final,
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
def test_calcular_precio_final_exitoso():
    # Arrange & Act
    resultado = calcular_precio_final(100.0, 19.0, 10.0)
    # Assert
    assert isinstance(resultado, float)

def test_calcular_precio_final_errores():
    with pytest.raises(ValueError):
        calcular_precio_final(-100.0, 19.0, 10.0)
    with pytest.raises(ValueError):
        calcular_precio_final(100.0, -5.0, 10.0)
    with pytest.raises(ValueError):
        calcular_precio_final(100.0, 19.0, 120.0)

def test_descuento_por_volumen_otros_rangos():
    # Menos de 10 unidades (sin descuento)
    assert descuento_por_volumen(5, 10.0) == 50.0
    # Rango 10-19 (5%)
    assert descuento_por_volumen(10, 100.0) == 950.0
    # Rango 20-49 (10%)
    assert descuento_por_volumen(20, 100.0) == 1800.0
    # Rango 50-99 (15%)
    assert descuento_por_volumen(50, 100.0) == 4250.0

def test_descuento_por_volumen_errores():
    with pytest.raises(ValueError):
        descuento_por_volumen(-2, 10.0)
    with pytest.raises(ValueError):
        descuento_por_volumen(10, -10.0)

def test_descuento_cumulativo_vacio_y_errores():
    # Lista vacía retorna el precio intacto
    assert descuento_cumulativo(150.0, []) == 150.0
    # Porcentaje inválido dentro de la lista
    with pytest.raises(ValueError):
        descuento_cumulativo(100.0, [10.0, 150.0])
    with pytest.raises(ValueError):
        descuento_cumulativo(-50.0, [10.0])

def test_descuento_apilado_exitoso_y_errores():
    # Lista vacía retorna el precio original
    assert descuento_apilado(200.0, []) == 200.0
    # Suma de descuentos (10% + 20% = 30%)
    resultado = descuento_apilado(100.0, [10.0, 20.0])
    assert resultado == 70.0
    # Precio negativo lanza error
    with pytest.raises(ValueError):
        descuento_apilado(-10.0, [10.0])
def test_calcular_precio_final_bug_impuesto():
    # Arrange: Precio 100, 10% de descuento (queda en 90) y 20% de impuesto.
    # El código con bug calcula el impuesto sobre 100 (100 * 0.20 = 20), dando un resultado incorrecto de 110.0
    resultado = calcular_precio_final(100.0, 20.0, 10.0)
    assert resultado == 108.0


def test_descuento_apilado_bug_exceder_100():
    # Bug 2: El descuento total puede exceder el 100% sin control.
    # Arrange: Descuentos que suman 110% (60% + 50%).
    # Lógica correcta: Un descuento total superior al 100% no debería dar un precio negativo 
    # (haciendo que la tienda "le pague" al cliente) o debería lanzar un error.
    resultado = descuento_apilado(100.0, [60.0, 50.0])
    assert resultado >= 0.0
