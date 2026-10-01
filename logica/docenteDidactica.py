from logica.docente import Docente

class DocenteDidactica(Docente):
    def __init__(self, cedula, nombre, mail, contacto, asignatura):
        # Heredamos los datos básicos del docente y le pasamos la asignatura como su especialidad
        super().__init__(cedula, nombre, mail, contacto, especialidad=asignatura)
        self.asignatura = asignatura

    def __str__(self):
        # Obtenemos la información base de la clase padre (Docente)
        base = super().__str__()

        # Le agregamos la asignatura específica de didáctica para mostrar en pantalla
        return f"{base}\n • Asignatura: {self.asignatura}"
