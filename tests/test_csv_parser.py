from unittest.mock import patch, mock_open
from src.csv_parser import leer_csv_como_lista

def test_leer_csv_con_mocking():
    # 1. Creamos el texto simulado que "tendría" el archivo real
    contenido_falso = "Nombre,Edad\nCarlos,30\nAna,25"

    # 2. Usamos 'patch' para interceptar la función 'open' de Python
    # mock_open simula que el archivo 'datos.csv' se abrió y contiene 'contenido_falso'
    with patch("builtins.open", mock_open(read_data=contenido_falso)):
        
        # Simulamos la lectura de un archivo ficticio
        with open("datos.csv", "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            
        # Ejecutamos la función de nuestro módulo con el contenido simulado
        resultado = leer_csv_como_lista(contenido)

    # 3. Verificamos que el resultado sea exactamente el esperado
    esperado = [
        ["Nombre", "Edad"],
        ["Carlos", "30"],
        ["Ana", "25"]
    ]
    assert resultado == esperado
