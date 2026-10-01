from logica.persona import Persona

class Docente(Persona):
    def __init__(self, cedula, nombre, mail, contacto, especialidad="Informática"):
        super().__init__(cedula, nombre, mail, contacto)
        self.especialidad = especialidad

    def __str__(self):
        base = super().__str__()
        return f"{base}\n • Especialidad: {self.especialidad}"