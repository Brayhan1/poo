# Ejercicio: Modelado de Clase Cuenta Bancaria

Este ejercicio consiste en la creación de una clase en Python para simular el comportamiento básico de una cuenta bancaria, aplicando conceptos de la Programación Orientada a Objetos (POO).

## Descripción del Código
El script define la clase `CuentaBancaria`, la cual permite almacenar los datos del cliente y gestionar su dinero mediante operaciones de validación, depósito y retiro.

### Atributos
* `titular`: Nombre del propietario de la cuenta (String).
* `numeroCuenta`: Identificador de la cuenta bancaria (String).
* `saldo`: Cantidad de dinero disponible (Float/Integer).

### Métodos Principales
* `__init__`: Inicializa los datos del titular, el número de cuenta y el saldo inicial.
* `depositar`: Incrementa el saldo actual sumando la cantidad especificada.
* `retirar`: Evalúa si hay fondos suficientes. Si la cantidad solicitada es menor o igual al saldo, realiza la resta; de lo contrario, retorna un mensaje de "Saldo insuficiente".
* `consultarSaldo`: Retorna el saldo actual de la cuenta.
* `mostrarInformacion`: Retorna un f-string con el nombre del titular y su saldo actual.

## Lógica Matemática
Las operaciones modifican el atributo del saldo utilizando aritmética básica y condicionales:

* **Depósito:** Saldo = Saldo + Cantidad
* **Retiro:** Saldo = Saldo - Cantidad (Condicionado a que Cantidad <= Saldo)

## Autor
* **Brayhan Rodriguez Tereso** - *Ingeniería en Sistemas*