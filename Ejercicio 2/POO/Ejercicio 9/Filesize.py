import os
ruta="test.text"
size= os.path.getsize(ruta)
kb=size/1024
mb=size/(1024*1024)
print(f"tamaño: {kb:.2f}KB")
print(f"tamaño: {mb:.4f}MB")