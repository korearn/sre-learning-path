# tests/test_app.py - VERSIÓN PARA GITHUB ACTIONS
import sys
import os

# Agregar el directorio correcto al path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

try:
    from advanced_log_analyzer import leer_archivo_log, analizar_niveles_log
except ImportError:
    # Fallback para estructura diferente
    import sys

    sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
    from src.advanced_log_analyzer import leer_archivo_log, analizar_niveles_log


def test_leer_archivo_log():
    """Test que verifica la lectura de archivos de log"""
    # Test con archivo existente (usar ruta relativa)
    import os

    if os.path.exists("src/app.log"):
        lineas = leer_archivo_log("src/app.log")
        assert len(lineas) > 0, "Debería leer líneas del archivo"
    else:
        print("⚠️  src/app.log no encontrado, saltando test de archivo real")

    # Test con archivo no existente
    lineas = leer_archivo_log("archivo_inexistente.log")
    assert lineas == [], "Debería retornar lista vacía para archivos no existentes"


def test_analizar_niveles_log():
    """Test que verifica el análisis de niveles de log"""
    lineas_ejemplo = [
        "2024-01-18 08:00:00 INFO - Application started",
        "2024-01-18 08:00:05 ERROR - Database connection failed",
        "2024-01-18 08:00:10 WARNING - High memory usage",
        "2024-01-18 08:00:15 INFO - Service healthy",
    ]

    resultado = analizar_niveles_log(lineas_ejemplo)

    assert resultado["INFO"] == 2, f"Debería contar 2 INFO, obtuvo {resultado['INFO']}"
    assert (
        resultado["ERROR"] == 1
    ), f"Debería contar 1 ERROR, obtuvo {resultado['ERROR']}"
    assert (
        resultado["WARNING"] == 1
    ), f"Debería contar 1 WARNING, obtuvo {resultado['WARNING']}"
    assert (
        resultado["DEBUG"] == 0
    ), f"Debería contar 0 DEBUG, obtuvo {resultado['DEBUG']}"


def test_estructura_analysis():
    """Test que verifica la estrcutura del análisis"""
    lineas = [
        "2025-09-30 08:00:00 INFO - Test message",
        "2025-09-30 08:00:01 ERROR - Test error",
    ]

    resultado = analizar_niveles_log(lineas)

    # Verificar que tiene las keys esperadas
    expected_keys = ["ERROR", "INFO", "WARNING", "DEBUG"]
    for key in expected_keys:
        assert key in resultado, f"El resultado debería contener la key {key}"

    # Verificar que los valores son enteros
    for value in resultado.values():
        assert isinstance(value, int), "Los valores del análisis deberían ser enteros"
