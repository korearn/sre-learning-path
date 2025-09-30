import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from advanced_log_analyzer import leer_archivo_log, analizar_niveles_log

def test_leer_archivo_log():
    """Test que verifica la lectura de archivos log"""
    # Test con archivo existente
    lineas = leer_archivo_log('src/app.log')
    assert len(lineas) > 0, "Debería leer líneas del archivo"

    # Test con archivo inexistente
    lineas = leer_archivo_log('archivo_inexistente.log')
    assert lineas == [], "Debería retornar lista vacía para archivo inexistente"

    def test_analizar_niveles_log():
        """Test que verifica el análisis de niveles de log"""
        lineas_ejemplo = [
        "2024-01-18 08:00:00 INFO - Application started",
        "2024-01-18 08:00:05 ERROR - Database connection failed",
        "2024-01-18 08:00:10 WARNING - High memory usage",
        "2024-01-18 08:00:15 INFO - Service healthy"
    ]
        
        resultado = analizar_niveles_log(lineas_ejemplo)

        assert resultado['INFO'] == 2, "Debería contar 2 mensajes INFO"
        assert resultado['ERROR'] == 1, "Debería contar 1 mensaje ERROR"
        assert resultado['WARNING'] == 1, "Debería contar 1 mensaje WARNING"
        assert resultado['DEBUG'] == 0, "Debería contar 1 mensaje DEBUG"

def test_estructura_analysis():
    """Test que verifica la estrcutura del análisis"""
    lineas = [
        "2025-09-30 08:00:00 INFO - Test message",
        "2025-09-30 08:00:01 ERROR - Test error"
    ]

    resultado = analizar_niveles_log(lineas)

    # Verificar que tiene las keys esperadas
    expected_keys = ['ERROR', 'INFO', 'WARNING', 'DEBUG']
    for key in expected_keys:
        assert key in resultado, f"El resultado debería contener la key {key}"

    # Verificar que los valores son enteros
    for value in resultado.values():
        assert isinstance(value, int), "Los valores del análisis deberían ser enteros"