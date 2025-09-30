#!/usr/bin/env python3
"""
Advanced Log Analyzer - Verión Web Service
"""
from flask import Flask, jsonify
import datetime

app = Flask(__name__)


def leer_archivo_log(ruta_archivo):
    """
    Lee un archivo de log y retorna las líneas
    """
    try:
        with open(ruta_archivo, "r") as archivo:
            lineas = archivo.readlines()
        return lineas
    except FileNotFoundError:
        return []


def analizar_niveles_log(lineas):
    """
    Analiza y cuenta los diferentes niveles de log
    """
    conteo = {"ERROR": 0, "INFO": 0, "WARNING": 0, "DEBUG": 0}

    for linea in lineas:
        linea = linea.strip()
        if "ERROR" in linea:
            conteo["ERROR"] += 1
        elif "WARNING" in linea:
            conteo["WARNING"] += 1
        elif "INFO" in linea:
            conteo["INFO"] += 1
        elif "DEBUG" in linea:
            conteo["DEBUG"] += 1

    return conteo


@app.route("/")
def home():
    return jsonify(
        {
            "service": "Log Analyzer API",
            "version": "1.0",
            "timestamp": datetime.datetime.now().isoformat(),
        }
    )


@app.route("/analyze")
def analyze():
    ruta_log = "app.log"
    lineas = leer_archivo_log(ruta_log)

    if not lineas:
        return jsonify({"error": "No se pudo leer el archivo de log"}), 500

    conteo = analizar_niveles_log(lineas)
    total = sum(conteo.values())

    return jsonify(
        {
            "files": ruta_log,
            "total_lines": total,
            "analysis": conteo,
            "timestamp": datetime.datetime.now().isoformat(),
        }
    )


@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200


if __name__ == "__main__":
    import os
    app.run(host="127.0.0.1", port=5000)  # Solo accesible localmente