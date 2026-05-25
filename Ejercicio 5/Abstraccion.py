from abc import ABC, abstractmethod
# Clase abstracta plantilla
class animal (ABC):
@abstractmethod
def hablar (self):
    pass #No se implementa el metodo

#Clase en especifico
class Perro(Animal):
    def hablar (self):
        return "GUUUAUU"
    
    