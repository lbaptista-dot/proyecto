class Persona:
    def __init__(self, cedula, nombre, mail="", contacto=""):
        self.cedula = cedula
        self.nombre = nombre
        self.mail = mail
        self.contacto = contacto

    def __str__(self):
        return f"[{self.cedula}] {self.nombre} (Mail: {self.mail or 'N/D'}, Contacto: {self.contacto or 'N/D'})"
