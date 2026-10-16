#Pruebas Unitarias (DevOps)

Repositorio dedicado a la aplicación de Desarrollo de pruebas unitarias AAA, detección y corrección de bugs lógicos, pruebas con simulación (*mocking*) e integración continua (CI/CD) utilizando Python.

---

## Tecnologías y Herramientas
* **Lenguaje:** Python 3.13
* **Pruebas y Cobertura:** `pytest`, `pytest-cov`
* **Simulación:** `unittest.mock` (`patch`, `mock_open`)
* **Automatización (CI/CD):** GitHub Actions

---

## Módulos Elegidos
1. **`calculadora.py`**: Operaciones aritméticas, estadísticas sobre listas y geometría con validación de excepciones.
2. **`descuentos.py`**: Reglas comerciales, descuentos por volumen, acumulativos, apilados y cálculo de impuestos.
3. **`utils.py`**: Conversiones termométricas, cálculo de IMC, validación de años bisiestos, números primos, MCD y MCM.
4. **`csv_parser.py`**: Parsing de líneas CSV, manejo de comillas y desincronización de columnas con pruebas mediante *mocking*.

---

## Resultados Clave
* **Bugs Identificados y Corregidos:** 7 fallos lógicos críticos solucionados (cálculo de mínimos, raíz cuadrada de negativos, orden de impuestos, límites de descuentos al 100%, signos en MCM y parsing de CSV).
* **Cobertura de Código:** **97% de cobertura global** verificada mediante `pytest-cov`.
* **Automatización:** Pipeline de CI/CD configurado en `.github/workflows/pytest.yml` para ejecutar la suite de pruebas automáticamente en cada `push`.

---

## Informe Completo
Para consultar el desarrollo detallado del proyecto, el análisis por módulo, las tablas de errores y las evidencias de ejecución, puedes revisar el documento oficial:

👉 **[Ver Informe Completo del Taller (PDF)](TallerDevops.pdf)**
