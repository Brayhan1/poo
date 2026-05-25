archivo = open("test.text", "a", encoding="utf-8")

# El rango define cuántas veces se ejecutará el bloque
for i in range(1048576):
    archivo.write("B")

archivo.close()