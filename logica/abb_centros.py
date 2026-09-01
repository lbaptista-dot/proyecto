class NodoABB:
    def __init__(self, centro):
        self.centro = centro
        self.izquierdo = None
        self.derecho = None


class ABBCentros:
    # Árbol Binario de Búsqueda para buscar centros por nombre rápidamente.
    def __init__(self):
        self.__raiz = None

    def insertar(self, centro):
        self.__raiz = self._insertar_recursivo(self.__raiz, centro)

    def _insertar_recursivo(self, nodo, centro):
        if nodo is None:
            return NodoABB(centro)
        if centro.nombre.lower() < nodo.centro.nombre.lower():
            nodo.izquierdo = self._insertar_recursivo(nodo.izquierdo, centro)
        else:
            nodo.derecho = self._insertar_recursivo(nodo.derecho, centro)
        return nodo

    def buscarPorNombre(self, nombre):
        return self._buscar_recursivo(self.__raiz, nombre.lower())

    def _buscar_recursivo(self, nodo, nombre):
        if nodo is None or nodo.centro.nombre.lower() == nombre:
            return nodo.centro if nodo else None
        if nombre < nodo.centro.nombre.lower():
            return self._buscar_recursivo(nodo.izquierdo, nombre)
        return self._buscar_recursivo(nodo.derecho, nombre)