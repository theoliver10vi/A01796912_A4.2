"""
Programa: wordCount.py
Descripción:
    Cuenta palabras distintas y su frecuencia en un archivo de texto.

Autor: Oliver Yousu Viveros Juárez
"""
# pylint: disable=invalid-name
import os
import sys
import time


def main():
    """Función principal."""
    if len(sys.argv) != 2:
        print("Uso: python wordCount.py <archivo_entrada>")
        sys.exit(1)

    inicio = time.time()
    archivo_entrada = sys.argv[1]

    try:
        with open(archivo_entrada, "r", encoding="utf-8") as archivo:
            palabras = archivo.read().lower().split()
    except FileNotFoundError:
        print(f"Archivo no encontrado: {archivo_entrada}")
        sys.exit(1)

    conteo = {}
    for palabra in palabras:
        conteo[palabra] = conteo.get(palabra, 0) + 1

    os.makedirs("results", exist_ok=True)
    ruta_salida = os.path.join("results", "WordCountResults.txt")

    with open(ruta_salida, "w", encoding="utf-8") as salida:
        for palabra, cantidad in sorted(conteo.items()):
            salida.write(f"{palabra}: {cantidad}\n")

    tiempo = time.time() - inicio
    print(f"Tiempo de ejecución (s): {tiempo}")


if __name__ == "__main__":
    main()
