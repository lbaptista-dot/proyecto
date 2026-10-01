class TribunalFinal:
    def __init__(self, practicante, docente1Info, docente2Info, docenteOtraEspecialidad):
        self.practicante = practicante
        self.docente1Info = docente1Info
        self.docente2Info = docente2Info
        self.docenteOtraEspecialidad = docenteOtraEspecialidad
        self.calificacion = None

    def __str__(self):
        return (
            f"=== TRIBUNAL DE DEFENSA ===\n"
            f" • Practicante: {self.practicante.nombre}\n"
            f" • Jurado 1 (Informática): {self.docente1Info.nombre}\n"
            f" • Jurado 2 (Informática): {self.docente2Info.nombre}\n"
            f" • Jurado 3 (Otra Especialidad): {self.docenteOtraEspecialidad.nombre} "
            f"({self.docenteOtraEspecialidad.asignatura})\n"
            f" • Calificación: {'Pendiente' if self.calificacion is None else self.calificacion}"
        )
