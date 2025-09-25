#!/usr/bin/env python3
"""
Advanced Log Analyzer - Día 2
Analiza archivos de log reales y genera reportes
"""

import sys
from collections import defaultdict

def leer_archivo_log(ruta_archivo):
    """
    Lee un archivo de log y retorna las líneas
    """
    try:
        with open(ruta_archivo, 'r') as archivo:
            lineas = archivo.readlines()
        return lineas
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {ruta_archivo}")
        return []

def analizar_niveles_log(lineas):
    """
    Analiza y cuenta los diferentes niveles de log
    """
    conteo = {'ERROR': 0, 'INFO': 0, 'WARNING': 0, 'DEBUG': 0}
    
    for linea in lineas:
        linea = linea.strip()
        if 'ERROR' in linea:
            conteo['ERROR'] += 1
        elif 'WARNING' in linea:
            conteo['WARNING'] += 1
        elif 'INFO' in linea:
            conteo['INFO'] += 1
        elif 'DEBUG' in linea:
            conteo['DEBUG'] += 1
    
    return conteo

def filtrar_errores_por_patron(lineas, patron):
    """
    Filtra líneas de ERROR que contengan un patrón específico
    """
    errores_filtrados = []
    
    for linea in lineas:
        if 'ERROR' in linea and patron.lower() in linea.lower():
            errores_filtrados.append(linea.strip())
    
    return errores_filtrados

def generar_reporte(conteo, archivo_salida="reporte_logs.txt"):
    """
    Genera un reporte en un archivo de texto
    """
    with open(archivo_salida, 'w') as reporte:
        reporte.write("=== REPORTE DE ANÁLISIS DE LOGS ===\n")
        reporte.write(f"Fecha de generación: 2024-01-16\n")
        reporte.write("=" * 40 + "\n")
        
        for nivel, cantidad in conteo.items():
            reporte.write(f"{nivel}: {cantidad} ocurrencias\n")
        
        total = sum(conteo.values())
        reporte.write(f"\nTOTAL: {total} líneas procesadas\n")

def estadisticas_errores_por_hora(lineas):
    errores_por_hora = defaultdict(int)
    for linea in lineas:
        if 'ERROR' in linea:
            # Suponiendo formato: "YYYY-MM-DD HH:MM:SS ERROR ..."
            partes = linea.split()
            if len(partes) > 1:
                hora = partes[1][:2]  # Extrae la hora (HH)
                errores_por_hora[hora] += 1
    if errores_por_hora:
        max_errores = max(errores_por_hora.values())
        horas_max = [h for h, c in errores_por_hora.items() if c == max_errores]
        print(f"Horas con más errores ({max_errores}): {', '.join(horas_max)}")
    else:
        print("No se encontraron errores para calcular estadísticas por hora.")

def main():
    """
    Función principal que orquesta el análisis
    """
    if len(sys.argv) < 2:
        print("Uso: python advanced_log_analyzer.py <archivo_log>")
        sys.exit(1)
    ruta_log = sys.argv[1]

    print("🔍 Iniciando análisis de logs...")

    # Leer archivo de log
    lineas = leer_archivo_log(ruta_log)

    if not lineas:
        print("No se pudieron leer los logs. Saliendo.")
        return

    print(f"📖 Se leyeron {len(lineas)} líneas del archivo {ruta_log}")

    # Analizar niveles de log
    conteo = analizar_niveles_log(lineas)

    # Mostrar resultados en consola
    print("\n📊 RESUMEN DE NIVELES DE LOG:")
    print("-" * 30)
    for nivel, cantidad in conteo.items():
        print(f"{nivel}: {cantidad}")

    # Filtrar errores específicos
    errores_db = filtrar_errores_por_patron(lineas, "database")
    print(f"\n🔴 Errores de base de datos: {len(errores_db)}")
    for error in errores_db:
        print(f"   - {error}")

    # Estadísticas de errores por hora
    estadisticas_errores_por_hora(lineas)

    # Generar reporte
    generar_reporte(conteo)
    print(f"\n📄 Reporte generado: reporte_logs.txt")

# Punto de entrada del script
if __name__ == "__main__":
    main()