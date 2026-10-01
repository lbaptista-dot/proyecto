from logica.docente import Docente

class Adscriptor(Docente):
    def _init_(self, cedula, nombre, mail, contacto, centroPractica, grado, dias, horario, especialidad="Informática"):
        super()._init_(cedula, nombre, mail, contacto, especialidad)
        self.centroPractica = centroPractica
        self.grado = grado
        self.dias = dias
        self.horario = horario

    def _str_(self):
        base = super()._str_()
        return ((
            f"{base}\n"
            f" • Centro de Práctica: {self.centroPractica}\n"
            f" • Grado: {self.grado} | Días: {self.dias} | Horario: {self.horario}"
        )

@staticmethod)
    def desdeLineaTxt(linea):
        partes = linea.strip().split(",")
        if len(partes) >= 6:
            return Adscriptor(partes[0], partes[1], partes[2], partes[3], partes[4], partes[5])
        return None