from logica.docente import Docente

class Adscriptor(Docente):
    def __init__(self, cedula, nombre, mail, contacto, centroPractica, grupos, especialidad="Informática"):
        # Heredamos los atributos básicos y la especialidad de la clase padre (Docente)
        super().__init__(cedula, nombre, mail, contacto, especialidad)
        self.centroPractica = centroPractica
        self.grupos = grupos  # Lista de diccionarios, ej: [{'grupo': '1°1', 'dias': 'Lunes', 'horario': '8:00'}]

    def __str__(self):
        # Obtenemos la representación en texto de la clase padre (Docente)
        base = super().__str__()

        # Recorremos la lista de grupos para armar un texto ordenado con cada uno
        info_grupos = ""
        for g in self.grupos:
            info_grupos += f"\n    • Grupo: {g['grupo']} | Días: {g['dias']} | Horario: {g['horario']}"

        # Devolvemos el texto completo combinado y ordenado para mostrar en pantalla
        return (
            f"{base}\n"
            f" • Centro de Práctica: {self.centroPractica}\n"
            f" • Grupos a cargo:{info_grupos}"
        )

