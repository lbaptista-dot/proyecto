class Persona:
    def __init__(self, cedula, nombre, mail="", contacto=""):
        # Guardamos los datos básicos que comparten todas las personas del sistema
        self.cedula = cedula
        self.nombre = nombre
        self.mail = mail
        self.contacto = contacto

    def __str__(self):
        # Creamos un texto ordenado para mostrar la información principal en pantalla,
        # poniendo 'N/D' si el mail o el contacto están vacíos
        return f"[{self.cedula}] {self.nombre} (Mail: {self.mail or 'N/D'}, Contacto: {self.contacto or 'N/D'})"
