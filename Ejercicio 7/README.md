# Ejercicio: Manejo de Excepciones Básico

Este script de Python demuestra la implementación de bloques de control de errores para evitar que un programa colapse ante entradas inválidas o cálculos matemáticos no permitidos.

## Descripción del Código
El archivo `excepcionesA.py` solicita al usuario ingresar dos números (numerador y denominador) para realizar una división, evaluando y capturando posibles fallas durante el tiempo de ejecución.

## Conceptos Aplicados
* **Bloque Try-Except:** Uso de la estructura `try` para probar un segmento de código propenso a fallar, y `except` para definir la respuesta del programa ante el error.
* **ValueError:** Captura la excepción que se genera si el usuario ingresa texto o caracteres especiales cuando el programa espera la conversión a números enteros (`int`).
* **ZeroDivisionError:** Intercepta el intento matemático inválido de dividir cualquier cantidad entre cero.

## Autor
* **Brayhan Rodriguez Tereso** - *Ingeniería en Sistemas*