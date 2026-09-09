from logica.cola_fifo import ColaFIFO

class CentroEducativo:
    def __init__(self, idCentro, nombre, localidad, cuposTotales):
        self.idCentro = idCentro
        self.nombre = nombre
        self.localidad = localidad
        self.cuposTotales = int(cuposTotales)
        self.estudiantesAsignados = []
        self.colaReserva = ColaFIFO()

    @staticmethod
    def desdeLineaTxt(linea):
        # Transforma una línea del archivo de texto en un objeto CentroEducativo usable
        datos = linea.strip().split(",")
        if len(datos) >= 4:
            idCentro, nombre, localidad, cuposTotales = datos[:4]
            return CentroEducativo(idCentro, nombre, localidad, int(cuposTotales))
        return None

    def __str__(self):
        # Lo que muestra la consola al listar los centros de forma clara
        return f"[{self.idCentro}] {self.nombre} ({self.localidad}) - Cupos totales: {self.cuposTotales}"