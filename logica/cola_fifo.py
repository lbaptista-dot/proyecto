class ColaFIFO:
    # Representa la cola de espera FIFO para reservas de cupos.
    def __init__(self):
        self.__elementos = []

    def encolar(self, elemento):
        self.__elementos.append(elemento)

    def desencolar(self):
        if not self.estaVacia():
            return self.__elementos.pop(0)
        return None

    def estaVacia(self):
        return len(self.__elementos) == 0

    def obtenerElementos(self):
        return list(self.__elementos)

    def cantidad(self):
        return len(self.__elementos)