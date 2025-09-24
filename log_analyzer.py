# log_analyzer.py
# Simulamos un archivo de log de una aplicación
log_entries = [
    "2023-10-01 08:15:10 INFO - User login successful",
    "2023-10-01 08:15:12 ERROR - Database connection failed",
    "2023-10-01 08:15:15 INFO - Data retrieval initiated",
    "2023-10-01 08:15:16 ERROR - Invalid user input",
    "2023-10-01 08:15:20 INFO - Transaction completed",
    "2023-10-01 08:15:22 ERROR - Payment gateway timeout"
]

# Tu tarea:
# 1. Contar cuántos ERRORs hay en el log
# 2. Imprimir las líneas que contienen "ERROR"

error_count = 0
print("Líneas de INFO encontradas:")
print("-" * 40)

# TU CÓDIGO VA AQUÍ (usa un bucle for y un if)
for entry in log_entries:
    if "INFO" in entry:
        print(entry)
        error_count += 1

print("-" * 40)
print(f"Total de errores encontrados: {error_count}")