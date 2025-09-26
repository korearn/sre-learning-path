# Dockerfile
# Usa una imagen oficial de Python
FROM python:3.9-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos de requisitos primero (para cache de Docker)
COPY requirements.txt .

# Instala las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código de la aplicación
COPY src/ .

# Comando por defecto cuando se ejecute el contenedor
CMD ["python", "./advanced_log_analyzer.py", "app.log"]