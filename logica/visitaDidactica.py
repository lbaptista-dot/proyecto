class VisitaDidactica:
    def __init__(self, docente, practicante, fecha, calificacion, observaciones):
        self.docente = docente
        self.practicante = practicante
        self.fecha = fecha
        self.calificacion = calificacion  # Puede ser un número (ej. 9) o texto/número
        self.observaciones = observaciones

    def __str__(self):
        return (f"\n=== DATOS DE LA VISITA ==-\n"
                f"Fecha: {self.fecha}\n"
                f"Docente: {self.docente.nombre}\n"
                f"Practicante: {self.practicante.nombre}\n"
                f"Calificación: {self.calificacion}\n"
                f"Observaciones: {self.observaciones}")
