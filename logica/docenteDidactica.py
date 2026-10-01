from logica.docente import Docente

class DocenteDidactica(Docente):
    def _init_(self, cedula, nombre, mail, contacto, asignatura):
        super()._init_(cedula, nombre, mail, contacto, especialidad=asignatura)
        self.asignatura = asignatura

    def _str_(self):
        base = super()._str_()
        return f"{base}\n • Asignatura: {self.asignatura}"
