from logica.persona import Persona

class Adscriptor(Persona):
    def __init__(self, cedula, nombre, mail, contacto, centroPractica, grado, dias, horario):
        super().__init__(cedula, nombre, mail, contacto)
        self.centroPractica = centroPractica
        self.grado = grado
        self.dias = dias
        self.horario = horario

    def __str__(self):
        base = super().__str__()
        return (
            f"{base}\n"
            f" • Centro: {self.centroPractica} | Grado: {self.grado}\n"
            f" • Disponibilidad: {self.dias} ({self.horario})"
        )