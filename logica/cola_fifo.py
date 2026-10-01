class ColaFIFO:
    def __init__(self):
        # Lista interna para organizar a los estudiantes en orden de llegada (El primero que llega es el primero en ser atendido)
        self.elementos = []

    def encolar(self, elemento):
        # Añade un estudiante al final de la fila de espera
        self.elementos.append(elemento)

    def desencolar(self):
        # Saca al primer estudiante que hizo la fila si hay elementos adentro (preguntando si la cantidad es mayor a 0)
        if len(self.elementos) > 0:
            return self.elementos.pop(0)
        return None

    def estaVacia(self):
        # Devuelve Verdadero si no hay nadie esperando en la cola
        return len(self.elementos) == 0

    def obtenerElementos(self):
        # Devuelve una copia de la lista de personas que están esperando
        return list(self.elementos)

    def cantidad(self):
        # Cuenta cuántas personas están esperando en la fila
        return len(self.elementos)
