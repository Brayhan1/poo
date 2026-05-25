# Ejercicio: Clases Abstractas y Polimorfismo (Minecraft Mobs)

Este proyecto implementa los conceptos de clases abstractas y polimorfismo en Python, utilizando una temática de personajes del videojuego Minecraft para ilustrar las jerarquías de clases.

## Descripción del Código
El sistema define una clase base abstracta que establece las reglas para crear entidades dentro del juego. A partir de este molde, se construyen diferentes clases derivadas, cada una con sus propias características específicas.

### Estructura de Archivos
* `Mob`: Clase abstracta que define los métodos obligatorios (`hacer_sonido`, `comportamiento`, `moverse`) y un método concreto compartido (`presentarse`) para imprimir la información en pantalla.
* `Creeper`, `Enderman`, `Vaca`: Clases derivadas que heredan de `Mob`. Cada una sobreescribe los métodos abstractos para retornar cadenas de texto con sus comportamientos característicos.
* `main.py`: Script de ejecución que valida la incapacidad de instanciar clases abstractas mediante un bloque `try-except`. Posteriormente, almacena múltiples objetos diferentes en una lista y los recorre mediante un ciclo `for` para presentarlos.

## Conceptos de POO Aplicados
* **Abstracción:** Se obliga a las clases hijas a definir sus propios sonidos y movimientos utilizando el decorador `@abstractmethod`. La clase padre no puede instanciarse por sí sola.
* **Herencia:** Las tres criaturas comparten el atributo de vida (HP) y reutilizan el método `presentarse` de la clase padre, evitando escribir la lógica de impresión múltiples veces.
* **Polimorfismo:** En el archivo principal, se utiliza un único ciclo para llamar a los métodos de distintos objetos (Vaca, Creeper, Enderman), y cada uno responde de manera diferente según su propia implementación.

## Autor
* **Brayhan Rodriguez Tereso** - *Ingeniería en Sistemas*