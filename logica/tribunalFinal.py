class TribunalFinal:
    def __init__(self, practicante, primerMiembro, segundoMiembro, tercerMiembro=None):
        # Guardamos los objetos recibidos en los atributos de la clase
        self.practicante = practicante
        self.primerMiembro = primerMiembro
        self.segundoMiembro = segundoMiembro
        self.tercerMiembro = tercerMiembro

    def __str__(self):
        # Verificamos de forma segura si el tercer miembro fue asignado o es None
        if self.tercerMiembro is not None:
            tercerNombre = self.tercerMiembro.nombre
        else:
            tercerNombre = "No asignado (Solo 2 miembros)"

        # Retornamos el texto formateado con los datos del tribunal
        return (
                "\n--- TRIBUNAL EXAMINADOR FINAL ---\n"
                "• Practicante: " + str(self.practicante.nombre) + "\n"
                                                                   "• 1er Miembro: " + str(self.primerMiembro.nombre) + "\n"
                                                                                                                        "• 2do Miembro: " + str(self.segundoMiembro.nombre) + "\n"
                                                                                                                                                                              "• 3er Miembro: " + str(tercerNombre)
        )
