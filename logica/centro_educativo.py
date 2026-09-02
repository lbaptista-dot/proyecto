from logica.cola_fifo import ColaFIFO

class CentroEducativo:
    # Representa un Liceo o Escuela asociado a las prácticas.
    def __init__(self, id_centro, nombre, localidad, cupos_totales):
        self.__id_centro = id_centro
        self.__nombre = nombre
        self.__localidad = localidad
        self.__cupos_totales = int(cupos_totales)
        self.__estudiantes_asignados = []
        self.__cola_reserva = ColaFIFO()

    @property
    def id_centro(self): return self.__id_centro

    @property
    def nombre(self): return self.__nombre

    @property
    def localidad(self): return self.__localidad

    @property
    def cupos_totales(self): return self.__cupos_totales

    @property
    def estudiantes_asignados(self): return self.__estudiantes_asignados

    @property
    def cola_reserva(self): return self.__cola_reserva

    def actualizar(self, nombre=None, localidad=None, cupos_totales=None):
        if nombre: self.__nombre = nombre
        if localidad: self.__localidad = localidad
        if cupos_totales is not None: self.__cupos_totales = int(cupos_totales)

    def cuposDisponibles(self):
        return self.__cupos_totales - len(self.__estudiantes_asignados)

    def solicitarCupo(self, estudiante_ci):
        if estudiante_ci in self.__estudiantes_asignados:
            return "El estudiante ya esta asignado a este centro."

        if self.cuposDisponibles() > 0:
            self.__estudiantes_asignados.append(estudiante_ci)
            return f"Cupo asignado exitosamente a C.I. {estudiante_ci} en {self.__nombre}."
        else:
            self.__cola_reserva.encolar(estudiante_ci)
            pos = self.__cola_reserva.cantidad()
            return f"Centro sin cupos libres. C.I. {estudiante_ci} ingreso a la Cola FIFO (Posicion #{pos})."

    def liberarCupo(self, estudiante_ci):
        if estudiante_ci in self.__estudiantes_asignados:
            self.__estudiantes_asignados.remove(estudiante_ci)
            if not self.__cola_reserva.estaVacia():
                siguiente_ci = self.__cola_reserva.desencolar()
                self.__estudiantes_asignados.append(siguiente_ci)
                return f"Cupo liberado. Se asigno automaticamente a C.I. {siguiente_ci} desde la Cola FIFO."
            return "Cupo liberado. No hay estudiantes en lista de espera."
        return "El estudiante no pertenece a este centro."

    def Diccionario(self):
        return {
            "id_centro": self.__id_centro,
            "nombre": self.__nombre,
            "localidad": self.__localidad,
            "cupos_totales": self.__cupos_totales,
            "estudiantes_asignados": self.__estudiantes_asignados,
            "cola_reserva": self.__cola_reserva.obtenerElementos()
        }

    @staticmethod
    def desdeDiccionario(datos):
        c = CentroEducativo(datos["id_centro"], datos["nombre"], datos["localidad"], datos["cupos_totales"])
        c.__estudiantes_asignados = datos.get("estudiantes_asignados", [])
        for ci in datos.get("cola_reserva", []):
            c.__cola_reserva.encolar(ci)
        return c

    def aLineaTxt(self):
        asig_str = ";".join(self.__estudiantes_asignados) if self.__estudiantes_asignados else "VACIO"
        cola_str = ";".join(self.__cola_reserva.obtenerElementos()) if not self.__cola_reserva.estaVacia() else "VACIO"
        return f"{self.__id_centro},{self.__nombre},{self.__localidad},{self.__cupos_totales},{asig_str},{cola_str}\n"

    @staticmethod
    def desdeLineaTxt(linea):
        datos = linea.strip().split(",")
        if len(datos) >= 6:
            id_c, nom, loc, cupos, asig_str, cola_str = datos[:6]
            c = CentroEducativo(id_c, nom, loc, int(cupos))
            if asig_str != "VACIO":
                c.__estudiantes_asignados = asig_str.split(";")
            if cola_str != "VACIO":
                for ci in cola_str.split(";"):
                    c.__cola_reserva.encolar(ci)
            return c
        return None

    def __str__(self):
        return f"[{self.__id_centro}] {self.__nombre} ({self.__localidad}) - Cupos: {len(self.__estudiantes_asignados)}/{self.__cupos_totales} | En Cola: {self.__cola_reserva.cantidad()}"