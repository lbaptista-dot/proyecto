class VisitaDidactica:
    def __init__(self, docente, practicante, fecha, calificacion, observaciones):
        self.docente = docente
        self.practicante = practicante
        self.fecha = str(fecha).strip()
        self.calificacion = str(calificacion).strip()  # Puede ser un número (ej. 9) o texto/número
        self.observaciones = str(observaciones).strip()

    def __str__(self):
        nombreDocente = self.docente.nombre if hasattr(self.docente, 'nombre') else str(self.docente)
        nombrePracticante = self.practicante.nombre if hasattr(self.practicante, 'practicante') else str(self.practicante)

        return (f"\n=== DATOS DE LA VISITA ==-\n"
                f"Fecha: {self.fecha}\n"
                f"Docente: {nombreDocente}\n"
                f"Practicante: {nombrePracticante}\n"
                f"Calificación: {self.calificacion}\n"
                f"Observaciones: {self.observaciones}")

    def aTextoTxt(self):
        """Convierte los datos de la visita en una línea de texto plano para guardar en visitas.txt"""
        cedDoc = self.docente.cedula if hasattr(self.docente, 'cedula') else "N/D"
        nomDoc = self.docente.nombre if hasattr(self.docente, 'nombre') else "N/D"

        cedPrac = self.practicante.cedula if hasattr(self.practicante, 'cedula') else "N/D"
        nomPrac = self.practicante.nombre if hasattr(self.practicante, 'nombre') else "N/D"

        return f"{cedDoc} - {nomDoc}, {cedPrac} - {nomPrac}, {self.fecha}, {self.calificacion}, {self.observaciones}"
