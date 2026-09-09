class VisitaDidactica:
    def __init__(self, practicante, docente, fecha, observaciones, calificacion):
        # Guardamos los datos básicos de la visita y a quiénes involucra
        self.__practicante = practicante  # El objeto Practicante que fue visitado
        self.__docente = docente          # El objeto DocenteDidactica que hizo la visita
        self.__fecha = fecha              # Día en que se realizó
        self.__observaciones = observaciones  # Comentarios o devolución escrita
        self.__calificacion = calificacion    # Nota o concepto que le puso

    # Getters usando @property (tal como pide el profesor)
    @property
    def practicante(self):
        return self.__practicante

    @property
    def docente(self):
        return self.__docente

    @property
    def fecha(self):
        return self.__fecha

    @property
    def observaciones(self):
        return self.__observaciones

    @property
    def calificacion(self):
        return self.__calificacion

    #Método __str formateado prolijamente hacia abajo para que se lea fácil en pantalla
    def __str__(self):
        return (
            f"=== DATOS DE LA VISITA ==-\n"
            f" Fecha: {self.__fecha}\n"
            f" Practicante: {self.__practicante.nombre}\n"
            f" Docente: {self.__docente.nombre}\n"
            f" Calificación: {self.__calificacion}\n"
            f" Observaciones: {self.__observaciones}\n"
        )