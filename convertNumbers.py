"""
Programa: convertNumbers.py
Descripción:
    Convierte números decimales a binario y hexadecimal usando
    algoritmos básicos.

Autor: Oliver Yousu Viveros Juárez
"""
# pylint: disable=invalid-name
import os
import sys
import time


def decimal_a_binario(numero):
    """Convierte un número decimal a binario."""
    if numero == 0:
        return "0"

    resultado = ""
    while numero > 0:
        resultado = str(numero % 2) + resultado
        numero //= 2
    return resultado


def decimal_a_hexadecimal(numero):
    """Convierte un número decimal a hexadecimal."""
    digitos = "0123456789ABCDEF"
    if numero == 0:
        return "0"

    resultado = ""
    while numero > 0:
        resultado = digitos[numero % 16] + resultado
        numero //= 16
    return resultado


def main():
    """Función principal."""
    if len(sys.argv) != 2:
        print("Uso: python convertNumbers.py <archivo_entrada>")
        sys.exit(1)

    inicio = time.time()
    archivo_entrada = sys.argv[1]

    try:
        with open(archivo_entrada, "r", encoding="utf-8") as archivo:
            numeros = [int(linea.strip()) for linea in archivo if linea.strip()]
    except FileNotFoundError:
        print(f"Archivo no encontrado: {archivo_entrada}")
        sys.exit(1)

    os.makedirs("results", exist_ok=True)
    ruta_salida = os.path.join("results", "ConversionResults.txt")

    with open(ruta_salida, "w", encoding="utf-8") as salida:
        salida.write("Number | Binary | Hex\n")
        for numero in numeros:
            binario = decimal_a_binario(numero)
            hexadecimal = decimal_a_hexadecimal(numero)
            salida.write(f"{numero} | {binario} | {hexadecimal}\n")

    tiempo = time.time() - inicio
    print(f"Tiempo de ejecución (s): {tiempo}")


if __name__ == "__main__":
    main()
