from logica.persona import Persona


class Practicante(Persona):
    def __init__(self, cedula, nombre, mail, contacto, grado):
        # Heredamos los datos básicos de la persona usando super()
        super().__init__(cedula, nombre, mail, contacto)
        self.grado = grado

        # Inicializamos los datos de práctica con valores por defecto hasta que se le asigne un centro
        self.centroAsignado = "Sin asignar"
        self.adscriptorAsignado = "Sin asignar"
        self.diasPractica = "N/D"
        self.horarioPractica = "N/D"
        self.centroObjeto = None


    def __str__(self):
        # Obtenemos la representación en texto de la clase base (Persona)
        base = super().__str__()

        # Retornamos toda la información unificada, incluyendo el grado, el centro y los horarios
        return (
            f"{base}\n"
            f" • Grado: {self.grado}\n"
            f" • Centro Práctica: {self.centroAsignado} | Adscriptor: {self.adscriptorAsignado}\n"
            f" • Días/Horario: {self.diasPractica} ({self.horarioPractica})"
        )