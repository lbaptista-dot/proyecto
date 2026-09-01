import os
from logica.centro_educativo import CentroEducativo

class RepositorioCentros:
    # Ruta orientada directamente al archivo centros.txt
    PATH_TXT = os.path.join(os.path.dirname(__file__), "centros.txt")

    def cargarDesdeTxt(self):
        centros = []
        if os.path.exists(self.PATH_TXT):
            with open(self.PATH_TXT, "r", encoding="utf-8") as f:
                for linea in f:
                    if linea.strip():
                        centro = CentroEducativo.desdeLineaTxt(linea)
                        if centro:
                            centros.append(centro)
        else:
            # Si no existe, crea centros.txt automáticamente
            os.makedirs(os.path.dirname(self.PATH_TXT), exist_ok=True)
            with open(self.PATH_TXT, "w", encoding="utf-8") as f:
                pass
        return centros

    def guardarEnTxt(self, lista_centros):
        os.makedirs(os.path.dirname(self.PATH_TXT), exist_ok=True)
        with open(self.PATH_TXT, "w", encoding="utf-8") as f:
            for c in lista_centros:
                f.write(c.aLineaTxt())