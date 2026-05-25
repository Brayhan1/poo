# Ejercicio: Abstracción en Python

Este script de Python demuestra la implementación del pilar de la abstracción dentro de la Programación Orientada a Objetos (POO), utilizando el módulo estándar `abc` (Abstract Base Classes).

## Descripción del Código
El archivo `Abstraccion.py` establece una clase base que funciona estrictamente como una plantilla. Esta clase no está diseñada para crear objetos directamente, sino para dictar las reglas y la estructura que deben seguir las clases derivadas.

## Conceptos de POO Aplicados
* **Abstracción:** Creación de la clase base `animal` heredando de `ABC`. Esto convierte a la clase en un molde abstracto que no puede ser instanciado por sí mismo.
* **Métodos Abstractos:** Se utiliza el decorador `@abstractmethod` en el método `hablar`. Esto obliga a cualquier clase hija (como `Perro`) a proporcionar obligatoriamente su propia implementación de dicho método; de lo contrario, el programa lanzará un error en tiempo de ejecución.
* **Herencia:** La clase `Perro` hereda de la clase abstracta y cumple con el contrato al proporcionar la lógica específica para el método `hablar`.

## Autor
* **Brayhan Rodriguez Tereso** - *Ingeniería en Sistemas*