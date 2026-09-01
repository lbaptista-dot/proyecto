from logica.abb_centros import ABBCentros

class GestionCentros:
    # Gestiona la lista de centros en memoria exactamente como la clase Agenda.
    def __init__(self):
        self.__centros = []
        self.__abb = ABBCentros()

    @property
    def centros(self):
        return self.__centros

    def cargarCentros(self, centros):
        self.__centros = centros
        self.__abb = ABBCentros()
        for c in self.__centros:
            self.__abb.insertar(c)

    # CREATE: agrega un centro nuevo al final de la lista.
    def agregarCentro(self, centro):
        self.__centros.append(centro)
        self.__abb.insertar(centro)

    # DELETE: saca de la lista el centro de esa posicion.
    def eliminarCentro(self, posicion):
        if 0 <= posicion < len(self.__centros):
            return self.__centros.pop(posicion)
        return None

    # READ: obtiene el centro por posicion.
    def obtenerCentro(self, posicion):
        if 0 <= posicion < len(self.__centros):
            return self.__centros[posicion]
        return None

    # UPDATE: actualiza los datos del centro en la posicion dada.
    def modificarCentro(self, posicion, nombre=None, localidad=None, cupos_totales=None):
        centro = self.obtenerCentro(posicion)
        if centro is None:
            return None
        centro.actualizar(nombre, localidad, cupos_totales)
        return centro

    def buscarPorNombreABB(self, nombre):
        return self.__abb.buscarPorNombre(nombre)

    def estaVacia(self):
        return len(self.__centros) == 0

    def cantidad(self):
        return len(self.__centros)