from logica.docente import Docente

class Adscriptor(Docente):
    def __init__(self, cedula, nombre, mail, contacto, centroPractica, grado, dias, horario, especialidad="Informática"):
        super().__init__(cedula, nombre, mail, contacto, especialidad)
        self.centroPractica = centroPractica
        self.grado = grado
        self.dias = dias
        self.horario = horario

    def __str__(self):
        base = super().__str__()
        return (
            f"{base}\n"
            f" • Centro de Práctica: {self.centroPractica}\n"
            f" • Grado: {self.grado} | Días: {self.dias} | Horario: {self.horario}"
        )