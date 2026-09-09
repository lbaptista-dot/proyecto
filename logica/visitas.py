class Visita:
    def __init__(self, fecha, observaciones, nota):
        self.fecha = fecha
        self.observaciones = observaciones
        self.nota = nota

    def __str__(self):
        return f"Fecha: {self.fecha}, Observaciones: {self.observaciones}, Nota: {self.nota}"


visita1 = Visita("7/8/2026", "Excelente desempeño durante la clase", 10)
visita2 = Visita("20/8/2026", "Se notó la falta de participación", 6)

visitas = [visita1, visita2]

for visita in visitas:
    print(visita)