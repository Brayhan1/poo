# Ejercicio: Manejo de Archivos y Metadatos

Este conjunto de scripts en Python demuestra cómo realizar operaciones básicas de entrada y salida (File I/O) con archivos de texto, así como la interacción con el sistema operativo para obtener sus propiedades.

## Descripción del Proyecto
El código se divide en tres operaciones secuenciales que ilustran la creación, modificación y análisis del peso de un archivo en el disco duro.

### Estructura de Archivos
* `Escritura.py`: Inicializa el proceso abriendo (o creando) el archivo `test.text` en modo de escritura (`"w"`), lo que limpia cualquier contenido previo.
* `Add.py`: Abre el archivo en modo de extensión o adjuntar (`"a"`). Utiliza un ciclo `for` para escribir el carácter "B" exactamente 1,048,576 veces. Dado que cada carácter pesa un byte, este código inyecta exactamente 1 Megabyte de datos en el documento.
* `Filesize.py`: Importa el módulo `os` para extraer los metadatos del archivo usando `os.path.getsize()`. Posteriormente, realiza operaciones matemáticas para convertir el tamaño base (bytes) a Kilobytes (KB) y Megabytes (MB), imprimiendo el resultado con un formato de decimales controlado.
* `test.text`: Es el documento de texto plano resultante donde se almacenan físicamente los datos escritos por los scripts anteriores.

## Conceptos Aplicados
* **Manipulación de Archivos:** Uso de la función `open()` con diferentes parámetros de acceso (`"w"` para sobrescribir y `"a"` para agregar al final sin borrar lo anterior).
* **Control de Flujo:** Uso de un ciclo iterativo con un rango precalculado ($1024 \times 1024$) para controlar el tamaño exacto del archivo generado.
* **Módulos del Sistema:** Implementación de la librería estándar `os` para interactuar con el sistema de archivos del sistema operativo y consultar propiedades físicas (peso) en lugar del contenido del documento.

## Autor
* **Brayhan Rodriguez Tereso** - *Ingeniería en Sistemas*