# Ejercicio: Herencia y Polimorfismo (Clase Animal)

Este proyecto consta de múltiples archivos en Python diseñados para demostrar los conceptos de herencia y polimorfismo dentro de la Programación Orientada a Objetos (POO).

## Descripción del Proyecto
El código establece una jerarquía de clases donde una clase padre (`Animal`) comparte sus atributos y comportamientos básicos con dos clases hijas (`Perro` y `Gato`), permitiendo la reutilización de código y la especialización de métodos.

### Estructura de Archivos
* `Animal.py`: Define la clase base. Incluye el constructor con los atributos `nombre` y `edad`, además de los métodos `describir` y `hablar`. *(Nota: Se utiliza `yo` como referencia de instancia en lugar del convencional `self`)*.
* `Gato.py`: Clase derivada que hereda de `Animal` y sobrescribe el método `hablar` para emitir su propio sonido ("!Miauuu¡").
* `Perro.py`: Clase derivada que hereda de `Animal` y sobrescribe el método `hablar` para emitir su propio sonido ("!GUAUUU").
* `main.py`: Archivo de ejecución principal que importa las clases, crea las instancias correspondientes y llama a sus métodos para probar el funcionamiento.

## Conceptos de POO Aplicados
* **Herencia:** Las clases derivadas (`Perro` y `Gato`) adquieren automáticamente las características y métodos de la clase base `Animal`.
* **Polimorfismo:** El método `hablar` es implementado con el mismo nombre en todas las jerarquías, pero su comportamiento de salida cambia dependiendo de si el objeto instanciado es un perro o un gato.

## Autor
* **Brayhan Rodriguez Tereso** - *Ingeniería en Sistemas*