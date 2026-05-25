class Ejercicio:
    def __init__(self, nombre, num_control, nivel, puntos):
        self.nombre = nombre
        self.num_control = num_control
        self.nivel = nivel
        self.puntos = puntos

    def getNombre(self):
        return self.nombre

    def getnum_control(self):
        return self.num_control 
 
    def ganar_puntos(self, cantidad: int):
        self.puntos += cantidad
        print(f"{self.nombre} ha ganado {cantidad} puntos. Total: {self.puntos}")
        
    def perder_puntos(self, cantidad: int):
        self.puntos -= cantidad
        print(f"{self.nombre} ha perdido {cantidad} puntos. Total: {self.puntos}")

    def mostrar_perfil(self):
        print("\n--- Perfil de Jugador ---")
        print(f"Nombre: {self.nombre}")
        print(f"Número de Control: {self.num_control}")
        print(f"Nivel: {self.nivel}")
        print(f"Puntos: {self.puntos}")

