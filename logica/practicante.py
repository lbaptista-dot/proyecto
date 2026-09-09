from logica.persona import Persona

class Practicante(Persona):
    def __init__(self, cedula, nombre, mail, contacto, grado):
        super().__init__(cedula, nombre, mail, contacto)
        self.grado = grado
        self.centroAsignado = "Sin asignar"
        self.adscriptorAsignado = "Sin asignar"
        self.diasPractica = "N/D"
        self.horarioPractica = "N/D"
        self.centroObjeto = None

    def __str__(self):
        base = super().__str__()
        return (
            f"{base}\n"
            f" • Grado: {self.grado}\n"
            f" • Centro Práctica: {self.centroAsignado} | Adscriptor: {self.adscriptorAsignado}\n"
            f" • Días/Horario: {self.diasPractica} ({self.horarioPractica})"
        )