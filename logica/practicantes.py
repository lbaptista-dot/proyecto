
class practicantes:
    def __init__(self, nombre):
        self.nombre = nombre
        self.calificaciones = []

    def agregar_nota(self, nota):
        self.calificaciones.append(nota)

    def calcular_promedio(self):
        if len(self.calificaciones) == 0:
            return 0

        return sum(self.calificaciones) / len(self.calificaciones)