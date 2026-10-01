from logica.abb_centros import ABBCentros

class GestionCentros:
    # Esta clase se encarga de administrar los centros tanto en una lista (para mostrarlos)
    # como en el Árbol Binario (para buscarlos rapidísimo).
    def __init__(self):
        self.centros = []
        self.abb = ABBCentros()

    def cargarCentros(self, listaCentros):
        # Carga los centros (por ejemplo, desde un archivo de texto) y los indexa en el árbol
        self.centros = listaCentros
        self.abb = ABBCentros()
        for centro in self.centros:
            self.abb.insertar(centro)

    def agregarCentro(self, centro):
        # Agrega un centro nuevo a la lista general y también lo inserta ordenado en el Árbol ABB
        self.centros.append(centro)
        self.abb.insertar(centro)

    def buscarPorNombreABB(self, nombre):
        # Realiza una búsqueda súper rápida y eficiente utilizando el Árbol Binario de Búsqueda
        return self.abb.buscarPorNombre(nombre)

    def obtenerTodos(self):
        # Devuelve la lista completa con todos los centros registrados
        return self.centros

    def estaVacia(self):
        # Devuelve Verdadero si todavía no hay ningún centro registrado (verificando si la cantidad es igual a 0)
        return len(self.centros) == 0

    def cantidad(self):
        # Cuenta cuántos centros hay en total en el sistema
        return len(self.centros)
