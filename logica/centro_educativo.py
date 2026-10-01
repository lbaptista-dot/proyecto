from logica.cola_fifo import ColaFIFO

class CentroEducativo:
    def __init__(self, idCentro, nombre, localidad, cuposTotales):
        # Datos principales que identifican y describen al centro educativo
        self.idCentro = idCentro
        self.nombre = nombre
        self.localidad = localidad
        self.cuposTotales = int(cuposTotales)

        # Estructuras para gestionar la capacidad y las inscripciones
        self.estudiantesAsignados = []  # Lista con los practicantes que ya lograron un cupo
        self.colaReserva = ColaFIFO()   # Cola FIFO para los estudiantes que queden en lista de espera

    def __str__(self):
        # Formato claro y ordenado que se muestra en la consola al listar los centros
        return f"[{self.idCentro}] {self.nombre} ({self.localidad}) - Cupos totales: {self.cuposTotales}"