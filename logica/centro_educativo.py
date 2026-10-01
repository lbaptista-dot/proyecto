from logica.cola_fifo import ColaFIFO

class CentroEducativo:
    def __init__(self, idCentro, nombre, localidad, cuposTotales):
        # Datos principales que identifican y describen al centro educativo
        self.idCentro = str(idCentro).strip()
        self.nombre = str(nombre).strip()
        self.localidad = str(localidad).strip()

        try:
            self.cuposTotales = int(cuposTotales)
        except ValueError:
            self.cuposTotales = 0

        # Estructuras para gestionar la capacidad y las inscripciones
        self.cuposDisponibles = self.cuposTotales
        self.estudiantesAsignados = []  # Lista con los practicantes que ya lograron un cupo
        self.colaReserva = ColaFIFO()   # Cola FIFO para los estudiantes que queden en lista de espera

    def __str__(self):
        # Formato claro y ordenado que se muestra en la consola al listar los centros
        return f"[{self.idCentro}] {self.nombre} ({self.localidad}) - Cupos totales: {self.cuposTotales}"

    def aTextoTxt(self):
        """Convierte los datos del centro en una línea de texto plano para guardar en centros.txt"""
        return f"{self.idCentro}, {self.nombre}, {self.localidad}, {self.cuposTotales}"

    @staticmethod
    def desdeLineaTxt(linea):
        """Crea y devuelve un objeto CentroEducativo a partir de una línea leída del archivo centros.txt"""
        partes = [p.strip() for p in linea.strip().split(",")]
        if len(partes) >= 4:
            return CentroEducativo(partes[0], partes[1], partes[2], partes[3])
        return None
