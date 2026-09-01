from logica.gestion_centros import GestionCentros
from logica.centro_educativo import CentroEducativo
from persistencia.repositorio_centros import RepositorioCentros


def mostrarMenu():
    print()
    print("===== GESTIÓN DE PRÁCTICAS DOCENTES (CENTROS) =====")
    print("1. Agregar centro educativo")
    print("2. Listar centros educativos")
    print("3. Modificar centro educativo")
    print("4. Eliminar centro educativo")
    print("5. Solicitar cupo / Cola FIFO")
    print("6. Liberar cupo")
    print("7. Buscar centro por nombre (Árbol ABB)")
    print("8. Salir (guarda en .txt)")


def listarCentros(gestion):
    if gestion.estaVacia():
        print("La lista de centros está vacía.")
        return
    print("Centros en memoria:")
    for i, c in enumerate(gestion.centros):
        print(f"  {i}. {c}")


def main():
    gestion = GestionCentros()
    repositorio = RepositorioCentros()

    # Carga inicial desde el archivo .txt
    gestion.cargarCentros(repositorio.cargarDesdeTxt())
    print(f"Se cargaron {gestion.cantidad()} centros desde el archivo TXT.")

    opcion = ""
    while opcion != "8":
        mostrarMenu()
        opcion = input("Elegí una opción: ").strip()

        if opcion == "1":
            id_centro = input("ID Centro: ").strip()
            if id_centro == "":
                print("El ID no puede estar vacío.")
                continue
            nombre = input("Nombre: ").strip()
            localidad = input("Localidad: ").strip()
            cupos = input("Cupos totales: ").strip()
            if not cupos.isdigit():
                print("Los cupos deben ser un número entero.")
                continue

            gestion.agregarCentro(CentroEducativo(id_centro, nombre, localidad, cupos))
            print("Centro educativo agregado.")

        elif opcion == "2":
            listarCentros(gestion)

        elif opcion == "3":
            listarCentros(gestion)
            if not gestion.estaVacia():
                entrada = input("Número de centro a modificar: ").strip()
                if entrada.isdigit():
                    centro = gestion.obtenerCentro(int(entrada))
                    if centro is None:
                        print("Número fuera de rango.")
                    else:
                        print(f"Centro actual: {centro}")
                        print("Deja un campo en blanco para mantener el valor actual.")
                        nombre = input("Nuevo nombre: ").strip()
                        localidad = input("Nueva localidad: ").strip()
                        cupos = input("Nuevos cupos totales: ").strip()

                        cupos_val = int(cupos) if cupos.isdigit() else None
                        gestion.modificarCentro(int(entrada), nombre, localidad, cupos_val)
                        print(f"Centro actualizado: {centro}")
                else:
                    print("Tienes que ingresar un número.")

        elif opcion == "4":
            listarCentros(gestion)
            if not gestion.estaVacia():
                entrada = input("Número de centro a eliminar: ").strip()
                if entrada.isdigit():
                    eliminado = gestion.eliminarCentro(int(entrada))
                    if eliminado is not None:
                        print(f"Eliminado: {eliminado}")
                    else:
                        print("Número fuera de rango.")
                else:
                    print("Tienes que ingresar un número.")

        elif opcion == "5":
            listarCentros(gestion)
            if not gestion.estaVacia():
                entrada = input("Número de centro donde solicitar cupo: ").strip()
                if entrada.isdigit():
                    centro = gestion.obtenerCentro(int(entrada))
                    if centro is None:
                        print("Número fuera de rango.")
                    else:
                        ci = input("C.I. del alumno practicante: ").strip()
                        if ci != "":
                            print(centro.solicitarCupo(ci))
                        else:
                            print("La C.I. no puede estar vacía.")
                else:
                    print("Tienes que ingresar un número.")

        elif opcion == "6":
            listarCentros(gestion)
            if not gestion.estaVacia():
                entrada = input("Número de centro donde liberar cupo: ").strip()
                if entrada.isdigit():
                    centro = gestion.obtenerCentro(int(entrada))
                    if centro is None:
                        print("Número fuera de rango.")
                    else:
                        ci = input("C.I. del alumno a liberar: ").strip()
                        if ci != "":
                            print(centro.liberarCupo(ci))
                        else:
                            print("La C.I. no puede estar vacía.")
                else:
                    print("Tienes que ingresar un número.")

        elif opcion == "7":
            nombre = input("Nombre del centro a buscar: ").strip()
            hallado = gestion.buscarPorNombreABB(nombre)
            if hallado:
                print(f"Resultado en Árbol ABB: {hallado}")
            else:
                print("No se encontró ningún centro con ese nombre en el ABB.")

        elif opcion == "8":
            # Guarda exclusivamente en .txt
            repositorio.guardarEnTxt(gestion.centros)
            print("Datos guardados correctamente en 'centros.txt'. ¡Hasta luego!")

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()