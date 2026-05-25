# Ejercicio: Perfil de Usuario

Este script de Python implementa una clase básica para gestionar la información y el puntaje de un usuario o jugador, aplicando conceptos fundamentales de la Programación Orientada a Objetos (POO).

## Descripción del Código
El código define la clase `Ejercicio`, la cual almacena datos de identificación y permite la modificación dinámica de su puntaje a través de métodos específicos.

### Atributos
* `nombre`: Nombre del usuario.
* `num_control`: Número de control o identificador único.
* `nivel`: Nivel actual del usuario.
* `puntos`: Cantidad de puntos acumulados (Integer).

### Métodos Principales
* `__init__`: Constructor que inicializa los datos generales del usuario.
* `getNombre` y `getnum_control`: Métodos de acceso para retornar la información respectiva.
* `ganar_puntos`: Incrementa la cantidad de puntos actuales mediante un parámetro y muestra el total actualizado.
* `perder_puntos`: Disminuye la cantidad de puntos mediante un parámetro y muestra el total actualizado.
* `mostrar_perfil`: Imprime en consola un resumen con todos los datos almacenados en la instancia.

## Autor
* **Brayhan Rodriguez Tereso** - *Ingeniería en Sistemas*