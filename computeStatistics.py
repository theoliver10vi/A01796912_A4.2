"""
Programa: computeStatistics.py
Descripción:
    Calcula estadísticas descriptivas básicas a partir de un archivo
    de números recibido como argumento por línea de comandos.

Autor: Oliver Yousu Viveros Juárez
"""
# pylint: disable=invalid-name
import os
import sys
import time


def leer_numeros(ruta_archivo):
    """Lee números desde un archivo de texto."""
    numeros = []
    invalidos = 0

    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                for token in linea.split():
                    try:
                        numeros.append(float(token))
                    except ValueError:
                        invalidos += 1
    except FileNotFoundError as exc:
        raise FileNotFoundError(
            f"Archivo no encontrado: {ruta_archivo}"
        ) from exc

    return numeros, invalidos


def calcular_media(valores):
    """Calcula la media."""
    return sum(valores) / len(valores)


def calcular_mediana(valores):
    """Calcula la mediana."""
    valores_ordenados = sorted(valores)
    n = len(valores_ordenados)
    mitad = n // 2

    if n % 2 == 0:
        return (valores_ordenados[mitad - 1] + valores_ordenados[mitad]) / 2

    return valores_ordenados[mitad]


def calcular_moda(valores):
    """Calcula la moda."""
    frecuencias = {}
    for valor in valores:
        frecuencias[valor] = frecuencias.get(valor, 0) + 1

    max_frecuencia = max(frecuencias.values())
    return [k for k, v in frecuencias.items() if v == max_frecuencia]


def calcular_varianza(valores, media):
    """Calcula la varianza poblacional."""
    suma = 0.0
    for valor in valores:
        suma += (valor - media) ** 2
    return suma / len(valores)


def escribir_resultados(ruta_salida, contenido):
    """Escribe resultados en archivo."""
    os.makedirs("results", exist_ok=True)
    with open(ruta_salida, "w", encoding="utf-8") as archivo:
        archivo.write(contenido)


def main():
    """Función principal."""
    if len(sys.argv) != 2:
        print("Uso: python computeStatistics.py <archivo_entrada>")
        sys.exit(1)

    inicio = time.time()
    archivo_entrada = sys.argv[1]

    numeros, invalidos = leer_numeros(archivo_entrada)

    if not numeros:
        print("No se encontraron números válidos.")
        sys.exit(1)

    media = calcular_media(numeros)
    mediana = calcular_mediana(numeros)
    moda = calcular_moda(numeros)
    varianza = calcular_varianza(numeros, media)
    desviacion = varianza ** 0.5

    tiempo = time.time() - inicio

    salida = (
        "Compute Statistics - Results\n"
        f"Archivo de entrada: {archivo_entrada}\n"
        f"Números válidos: {len(numeros)}\n"
        f"Tokens inválidos: {invalidos}\n\n"
        f"Media: {media}\n"
        f"Mediana: {mediana}\n"
        f"Moda: {moda}\n"
        f"Varianza (poblacional): {varianza}\n"
        f"Desviación estándar (poblacional): {desviacion}\n\n"
        f"Tiempo de ejecución (s): {tiempo}\n"
    )

    print(salida)

    ruta_resultados = os.path.join("results", "StatisticsResults.txt")
    escribir_resultados(ruta_resultados, salida)


if __name__ == "__main__":
    main()
