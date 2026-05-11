#exceociones basicas
# parte 1: try / except simple
print ("=" * 50)
print ("PARTE 1: Division con manejo de errores")
print ("=" * 50)
try:
    a= int (input("ingresa el numerador:"))
    b= int (input("ingresa el denominador:"))
    total = a/b

except ValueError:
    print("Error : Solo numeros")

except ZeroDivisionError: