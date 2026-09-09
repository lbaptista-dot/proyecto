class Nodo:
    def __init__(self, centro):
        self.__centro = centro  # El objeto CentroEducativo
        self.__izquierda = None
        self.__derecha = None

    @property
    def centro(self):
        return self.__centro

    @centro.setter
    def centro(self, valor):
        self.__centro = valor

    @property
    def izquierda(self):
        return self.__izquierda

    @izquierda.setter
    def izquierda(self, nodo):
        self.__izquierda = nodo

    @property
    def derecha(self):
        return self.__derecha

    @derecha.setter
    def derecha(self, nodo):
        self.__derecha = nodo


class ABBCentros:
    def __init__(self):
        self.__raiz = None

    @property
    def raiz(self):
        return self.__raiz

    @raiz.setter
    def raiz(self, nodo):
        self.__raiz = nodo

    def estaVacio(self):
        return self.__raiz is None

    # ---------- Insertar ordenado por nombre del centro ----------

    def insertar(self, centro):
        self.__raiz = self.__insertarRecursivo(self.__raiz, centro)

    def __insertarRecursivo(self, nodo, centro):
        if nodo is None:
            return Nodo(centro)

        # Comparamos alfabéticamente en minúsculas los nombres de los centros
        if centro.nombre.lower() < nodo.centro.nombre.lower():
            nodo.izquierda = self.__insertarRecursivo(nodo.izquierda, centro)
        elif centro.nombre.lower() > nodo.centro.nombre.lower():
            nodo.derecha = self.__insertarRecursivo(nodo.derecha, centro)
        # Si tienen exactamente el mismo nombre, no se duplica

        return nodo

    # ---------- Buscar por nombre ----------

    def buscarPorNombre(self, nombre):
        return self.__buscarRecursivo(self.__raiz, nombre.lower())

    def __buscarRecursivo(self, nodo, nombre):
        if nodo is None:
            return None

        if nombre == nodo.centro.nombre.lower():
            return nodo.centro
        elif nombre < nodo.centro.nombre.lower():
            return self.__buscarRecursivo(nodo.izquierda, nombre)
        else:
            return self.__buscarRecursivo(nodo.derecha, nombre)

    # ---------- Recorridos (Inorden, Preorden, Postorden) ----------

    def inorden(self):
        resultado = []
        self.__inordenRecursivo(self.__raiz, resultado)
        return resultado

    def __inordenRecursivo(self, nodo, resultado):
        if nodo is not None:
            self.__inordenRecursivo(nodo.izquierda, resultado)
            resultado.append(nodo.centro)
            self.__inordenRecursivo(nodo.derecha, resultado)

    def preorden(self):
        resultado = []
        self.__preordenRecursivo(self.__raiz, resultado)
        return resultado

    def __preordenRecursivo(self, nodo, resultado):
        if nodo is not None:
            resultado.append(nodo.centro)
            self.__preordenRecursivo(nodo.izquierda, resultado)
            self.__preordenRecursivo(nodo.derecha, resultado)

    def postorden(self):
        resultado = []
        self.__postordenRecursivo(self.__raiz, resultado)
        return resultado

    def __postordenRecursivo(self, nodo, resultado):
        if nodo is not None:
            self.__postordenRecursivo(nodo.izquierda, resultado)
            self.__postordenRecursivo(nodo.derecha, resultado)
            resultado.append(nodo.centro)