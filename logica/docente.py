from logica.persona import Persona

class Docente(Persona):
    def __init__(self, cedula, nombre, mail, contacto, especialidad="Informática"):
        # Llamamos al constructor de la clase padre (Persona) para heredar los datos básicos
        super().__init__(cedula, nombre, mail, contacto)
        self.especialidad = especialidad

    def __str__(self):
        # Obtenemos el texto base que viene de la clase Persona
        base = super().__str__()

        # Le sumamos la especialidad del docente para mostrarlo ordenado en pantalla
        return f"{base}\n • Especialidad: {self.especialidad}"
