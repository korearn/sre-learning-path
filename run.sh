#!/bin/bash

echo "???? Ejecutando Log Analyzer en Docker..."

# Verificar que el archivo de log existe
if [ ! -f "./src/app.log" ]; then
    echo "??? Error: Archivo src/app.log no encontrado"
    echo "???? Ejecuta primero: docker-compose up para generar logs de ejemplo"
    exit 1
fi

# Usar la imagen v1 que sabemos funciona
echo "???? Analizando logs con imagen estable (v1)..."
docker run --rm -v $(pwd)/src/app.log:/app/app.log log-analyzer:v1

echo "??? An??lisis completado!"
