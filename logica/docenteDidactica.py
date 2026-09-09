from logica.persona import Persona

class DocenteDidactica(Persona):
    def __init__(self, cedula, nombre, mail, contacto, asignatura):
        super().__init__(cedula, nombre, mail, contacto)
        self.asignatura = asignatura

    def __str__(self):
        base = super().__str__()
        return f"{base}\n • Asignatura: {self.asignatura}"