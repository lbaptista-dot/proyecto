# CLASE NODO (Para construir el Árbol Binario)
# ==========================================
class Nodo:
    def __init__(self, centro):
        self.__centro = centro  # El objeto CentroEducativo que guarda este nodo
        self.__izquierda = None  # Apunta al hijo menor (alfabéticamente anterior)
        self.__derecha = None    # Apunta al hijo mayor (alfabéticamente posterior)

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


# ==========================================
class Nodo:
    def __init__(self, dato):
        self.__dato = dato
        self.__izquierda = None
        self.__derecha = None

    @property
    def dato(self):
        return self.__dato

    @dato.setter
    def dato(self, valor):
        self.__dato = valor

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

    # ---------- Agregar un nodo ordenado por ID ----------

    def insertar(self, centro):
        self.__raiz = self.__agregarRecursivo(self.__raiz, centro)

    def __agregarRecursivo(self, nodo, centro):
        # Caso base: encontramos el lugar donde crear el nuevo nodo.
        # Comparamos por idCentro (convertido a string/minúscula para ordenar de forma segura)
        if nodo is None:
            return Nodo(centro)

        id_nuevo = str(centro.idCentro).strip().lower()
        id_actual = str(nodo.dato.idCentro).strip().lower()

        if id_nuevo < id_actual:
            nodo.izquierda = self.__agregarRecursivo(nodo.izquierda, centro)
        elif id_nuevo > id_actual:
            nodo.derecha = self.__agregarRecursivo(nodo.derecha, centro)
        # Si id_nuevo == id_actual no se inserta (árbol sin duplicados).

        return nodo

    # ---------- Buscar por ID en el ABB ----------

    def buscarPorId(self, id_buscado):
        return self.__buscarRecursivo(self.__raiz, str(id_buscado).strip().lower())

    def __buscarRecursivo(self, nodo, id_buscado):
        if nodo is None:
            return None

        id_actual = str(nodo.dato.idCentro).strip().lower()

        if id_buscado == id_actual:
            return nodo.dato
        elif id_buscado < id_actual:
            return self.__buscarRecursivo(nodo.izquierda, id_buscado)
        else:
            return self.__buscarRecursivo(nodo.derecha, id_buscado)

    # ---------- Listar (recorridos) ----------

    def inorden(self):
        # Izquierda -> Raiz -> Derecha. En un ABB devuelve los datos ORDENADOS por ID.
        resultado = []
        self.__inordenRecursivo(self.__raiz, resultado)
        return resultado

    def __inordenRecursivo(self, nodo, resultado):
        if nodo is not None:
            self.__inordenRecursivo(nodo.izquierda, resultado)
            resultado.append(nodo.dato)
            self.__inordenRecursivo(nodo.derecha, resultado)

    def preorden(self):
        # Raiz -> Izquierda -> Derecha.
        resultado = []
        self.__preordenRecursivo(self.__raiz, resultado)
        return resultado

    def __preordenRecursivo(self, nodo, resultado):
        if nodo is not None:
            resultado.append(nodo.dato)
            self.__preordenRecursivo(nodo.izquierda, resultado)
            self.__preordenRecursivo(nodo.derecha, resultado)

    def postorden(self):
        # Izquierda -> Derecha -> Raiz.
        resultado = []
        self.__postordenRecursivo(self.__raiz, resultado)
        return resultado

    def __postordenRecursivo(self, nodo, resultado):
        if nodo is not None:
            self.__postordenRecursivo(nodo.izquierda, resultado)
            self.__postordenRecursivo(nodo.derecha, resultado)
            resultado.append(nodo.dato)

    # ---------- Buscar por Nombre o Localidad en el ABB ----------
    def buscarPorNombreOLocalidad(self, texto_buscado):
        # Como el ABB está ordenado por ID, para buscar por nombre o localidad
        # recorremos todos los nodos del árbol (aprovechando el método inorden) y filtramos.
        todosLosCentros = self.inorden()
        texto = str(texto_buscado).strip().lower()

        centrosEncontrados = []
        for centro in todosLosCentros:
            nombreCentro = str(centro.nombre).strip().lower()
            localidadCentro = str(centro.localidad).strip().lower()

            # Si el texto coincide parcial o totalmente con el nombre o la localidad
            if texto in nombreCentro or texto in localidadCentro:
                centrosEncontrados.append(centro)

        return centrosEncontrados
