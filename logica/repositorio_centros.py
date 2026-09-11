from logica.abb_centros import ABBCentros
from logica.centro_educativo import CentroEducativo
from logica.practicante import Practicante
from logica.adscriptor import Adscriptor
from logica.docenteDidactica import DocenteDidactica
from logica.tribunalFinal import TribunalFinal

def menuCentrosPracticas(abbCentros, listaCentros):
    """Menú para administrar los centros educativos donde se realizan las prácticas."""
    while True:
        print("\n--- MENÚ CENTROS DE PRÁCTICA ---")
        print("1. Registrar")
        print("2. Modificar")
        print("3. Borrar")
        print("4. Listar")
        print("5. Salir")

        opcion = input("Elegir opción: ").strip()

        if opcion == "1":
            print("\n[Registrar Centro]")
            idCentro = input("ID Centro: ").strip()
            nombre = input("Nombre del centro: ").strip()
            localidad = input("Localidad: ").strip()
            try:
                cuposTotales = int(input("Cupos totales: ").strip())
            except ValueError:
                cuposTotales = 0

            # Creamos el objeto centro y le asignamos los cupos disponibles
            nuevoCentro = CentroEducativo(idCentro, nombre, localidad, cuposTotales)
            nuevoCentro.cuposDisponibles = cuposTotales

            # Lo guardamos en el Árbol Binario de Búsqueda y en la lista general
            abbCentros.insertar(nuevoCentro)
            listaCentros.append(nuevoCentro)
            print(f"¡Centro '{nombre}' registrado con éxito!")

        elif opcion == "2":
            print("\n[Modificar Centro]")
            nombreBuscado = input("Ingrese el nombre del centro a modificar: ").strip().lower()
            centroEncontrado = None
            for c in listaCentros:
                if c.nombre.strip().lower() == nombreBuscado:
                    centroEncontrado = c
                    break

            if centroEncontrado:
                print(f"Centro encontrado: {centroEncontrado}")
                nuevoNombre = input("Nuevo nombre (enter para omitir): ").strip()
                nuevaLocalidad = input("Nueva localidad (enter para omitir): ").strip()
                nuevosCupos = input("Nuevos cupos totales (enter para omitir): ").strip()

                if nuevoNombre: centroEncontrado.nombre = nuevoNombre
                if nuevaLocalidad: centroEncontrado.localidad = nuevaLocalidad
                if nuevosCupos:
                    centroEncontrado.cuposTotales = int(nuevosCupos)
                    centroEncontrado.cuposDisponibles = int(nuevosCupos)
                print("¡Centro modificado con éxito!")
            else:
                print("No se encontró ningún centro con ese nombre.")

        elif opcion == "3":
            print("\n[Borrar Centro]")
            nombreBuscado = input("Ingrese el nombre del centro a borrar: ").strip().lower()
            largoInicial = len(listaCentros)
            listaCentros[:] = [c for c in listaCentros if c.nombre.strip().lower() != nombreBuscado]

            if len(listaCentros) < largoInicial:
                # Si borramos uno, reconstruimos el árbol para que no quede mal ordenado
                abbCentros.raiz = None
                for c in listaCentros:
                    abbCentros.insertar(c)
                print("¡Centro borrado con éxito!")
            else:
                print("No se encontró ningún centro con ese nombre.")

        elif opcion == "4":
            print("\n--- LISTA DE CENTROS ---")
            if not listaCentros:
                print("Todavía no hay centros registrados.")
            else:
                for c in listaCentros:
                    print(f"{c} | Cupos: {getattr(c, 'cuposDisponibles', 'N/D')}/{getattr(c, 'cuposTotales', 'N/D')}")

        elif opcion == "5":
            break
        else:
            print("Opción no válida. Probá de nuevo.")


def menuAdscriptores(listaAdscriptores):
    """Menú para administrar los profesores adscriptores."""
    while True:
        print("\n--- MENÚ ADSCRIPTORES ---")
        print("1. Registrar")
        print("2. Modificar")
        print("3. Borrar")
        print("4. Listar")
        print("5. Salir")

        opcion = input("Elegir opción: ").strip()

        if opcion == "1":
            print("\n[Registrar Adscriptor]")
            cedula = input("Cédula: ").strip()
            nombre = input("Nombre: ").strip()
            mail = input("Mail: ").strip()
            contacto = input("Contacto opcional: ").strip()
            centroPractica = input("Centro de práctica asignado: ").strip()
            grado = input("Grado que dicta: ").strip()
            dias = input("Días disponibles: ").strip()
            horario = input("Horario disponible: ").strip()

            nuevoAdscriptor = Adscriptor(cedula, nombre, mail, contacto, centroPractica, grado, dias, horario)
            listaAdscriptores.append(nuevoAdscriptor)
            print(f"¡Adscriptor '{nombre}' registrado con éxito!")

        elif opcion == "2":
            print("\n[Modificar Adscriptor]")
            cedulaBuscada = input("Ingrese la cédula del adscriptor a modificar: ").strip()
            encontrado = False
            for a in listaAdscriptores:
                if a.cedula == cedulaBuscada:
                    nuevoNombre = input("Nuevo nombre (enter para omitir): ").strip()
                    nuevoMail = input("Nuevo mail (enter para omitir): ").strip()
                    if nuevoNombre: a.nombre = nuevoNombre
                    if nuevoMail: a.mail = nuevoMail
                    print("¡Adscriptor modificado con éxito!")
                    encontrado = True
                    break
            if not encontrado:
                print("No se encontró un adscriptor con esa cédula.")

        elif opcion == "3":
            print("\n[Borrar Adscriptor]")
            cedulaBuscada = input("Ingrese la cédula del adscriptor a borrar: ").strip()
            largoInicial = len(listaAdscriptores)
            listaAdscriptores[:] = [a for a in listaAdscriptores if a.cedula != cedulaBuscada]
            if len(listaAdscriptores) < largoInicial:
                print("¡Adscriptor borrado con éxito!")
            else:
                print("No se encontró esa cédula.")

        elif opcion == "4":
            print("\n--- LISTA DE ADSCRIPTORES ---")
            if not listaAdscriptores:
                print("No hay adscriptores registrados.")
            else:
                for a in listaAdscriptores:
                    print(a)

        elif opcion == "5":
            break
        else:
            print("Opción no válida.")


def menuPracticantes(listaPracticantes, listaCentros, listaAdscriptores):
    """Menú para registrar practicantes y asignarles su centro y adscriptor."""
    while True:
        print("\n--- MENÚ PRACTICANTES ---")
        print("1. Registrar Practicante")
        print("2. Modificar Practicante")
        print("3. Borrar Practicante")
        print("4. Listar Practicantes")
        print("5. Asignar Centro y Descontar Cupo")
        print("6. Salir")

        opcion = input("Elegir opción: ").strip()

        if opcion == "1":
            print("\n[Registrar Practicante]")
            cedula = input("Cédula: ").strip()
            nombre = input("Nombre: ").strip()
            mail = input("Mail: ").strip()
            contacto = input("Contacto opcional: ").strip()
            grado = input("Grado: ").strip()

            nuevoPracticante = Practicante(cedula, nombre, mail, contacto, grado)
            listaPracticantes.append(nuevoPracticante)
            print(f"¡Practicante '{nombre}' registrado!")

        elif opcion == "2":
            print("\n[Modificar Practicante]")
            cedulaBuscada = input("Ingrese la cédula del practicante a modificar: ").strip()
            encontrado = False
            for p in listaPracticantes:
                if p.cedula == cedulaBuscada:
                    nuevoNombre = input("Nuevo nombre (enter para omitir): ").strip()
                    if nuevoNombre: p.nombre = nuevoNombre
                    print("¡Practicante modificado con éxito!")
                    encontrado = True
                    break
            if not encontrado:
                print("No se encontró un practicante con esa cédula.")

        elif opcion == "3":
            print("\n[Borrar Practicante]")
            cedulaBuscada = input("Ingrese la cédula del practicante a borrar: ").strip()

            # Si borramos al practicante, devolvemos el cupo al centro educativo
            for p in listaPracticantes:
                if p.cedula == cedulaBuscada and hasattr(p, 'centroObjeto') and p.centroObjeto:
                    p.centroObjeto.cuposDisponibles += 1

            largoInicial = len(listaPracticantes)
            listaPracticantes[:] = [p for p in listaPracticantes if p.cedula != cedulaBuscada]
            if len(listaPracticantes) < largoInicial:
                print("¡Practicante borrado y cupo devuelto al centro!")
            else:
                print("No se encontró esa cédula.")

        elif opcion == "4":
            print("\n--- LISTA DE PRACTICANTES ---")
            if not listaPracticantes:
                print("No hay practicantes registrados.")
            else:
                for p in listaPracticantes:
                    print(p)

        elif opcion == "5":
            print("\n[Asignación de Práctica]")
            cedulaBuscada = input("Ingrese la cédula del practicante: ").strip()

            practicanteEncontrado = None
            for p in listaPracticantes:
                if p.cedula == cedulaBuscada:
                    practicanteEncontrado = p
                    break

            if not practicanteEncontrado:
                print("No se encontró un practicante con esa cédula.")
            else:
                if not listaCentros:
                    print("No hay centros educativos registrados.")
                else:
                    print(f"\nPracticante: {practicanteEncontrado.nombre} (Grado: {getattr(practicanteEncontrado, 'grado', 'N/D')})")
                    print("\nCentros disponibles y cupos:")
                    for idx, c in enumerate(listaCentros):
                        disponibles = getattr(c, 'cuposDisponibles', c.cuposTotales)
                        print(f"{idx + 1}. {c.nombre} (Localidad: {c.localidad}) - Cupos disponibles: {disponibles}")

                    try:
                        seleccionCentro = int(input("Seleccione el número del centro: ")) - 1
                        if 0 <= seleccionCentro < len(listaCentros):
                            centroElegido = listaCentros[seleccionCentro]

                            if not hasattr(centroElegido, 'cuposDisponibles'):
                                centroElegido.cuposDisponibles = int(centroElegido.cuposTotales)

                            if centroElegido.cuposDisponibles <= 0:
                                print("¡Error! Este centro ya no tiene cupos disponibles.")
                                continue

                            # Buscamos si hay un adscriptor para este centro
                            adscriptorEncontrado = None
                            for a in listaAdscriptores:
                                if a.centroPractica.strip().lower() == centroElegido.nombre.strip().lower():
                                    adscriptorEncontrado = a
                                    break

                            if adscriptorEncontrado:
                                print(f"\n-> Adscriptor responsable: {adscriptorEncontrado.nombre}")
                                print(f"-> Días y Horarios: {adscriptorEncontrado.dias} | {adscriptorEncontrado.horario}")
                                nombreAdscriptorTxt = adscriptorEncontrado.nombre
                            else:
                                print("\n-> No hay un adscriptor registrado para este centro.")
                                nombreAdscriptorTxt = "Sin adscriptor"

                            dias = input("\nIngrese los días de práctica asignados: ").strip()
                            horario = input("Ingrese el horario asignado: ").strip()

                            # Restamos 1 al cupo del centro seleccionado
                            centroElegido.cuposDisponibles -= 1

                            # Guardamos los datos en el practicante
                            practicanteEncontrado.centroAsignado = centroElegido.nombre
                            practicanteEncontrado.adscriptorAsignado = nombreAdscriptorTxt
                            practicanteEncontrado.diasPractica = dias
                            practicanteEncontrado.horarioPractica = horario
                            practicanteEncontrado.centroObjeto = centroElegido

                            print(f"¡Asignación exitosa! Cupos restantes en {centroElegido.nombre}: {centroElegido.cuposDisponibles}")
                        else:
                            print("Número de centro inválido.")
                    except ValueError:
                        print("Por favor, ingrese un número válido.")

        elif opcion == "6":
            break
        else:
            print("Opción no válida.")


def menuDocenteDidactica(listaDocentes, listaPracticantes):
    """Menú para gestionar docentes de didáctica y armar el tribunal final."""
    while type(True) == bool: # Bucle estándar del menú
        print("\n--- MENÚ DOCENTE DIDÁCTICA Y TRIBUNAL ---")
        print("1. Registrar Docente")
        print("2. Modificar Docente")
        print("3. Listar Docentes")
        print("4. Armar Tribunal Final (Defensa)")
        print("5. Salir")

        opcion = input("Elegir opción: ").strip()

        if opcion == "1":
            print("\n[Registrar Docente]")
            cedula = input("Cédula: ").strip()
            nombre = input("Nombre: ").strip()
            mail = input("Mail: ").strip()
            contacto = input("Contacto opcional: ").strip()
            asignatura = input("Asignatura: ").strip()

            nuevoDocente = DocenteDidactica(cedula, nombre, mail, contacto, asignatura)
            listaDocentes.append(nuevoDocente)
            print(f"¡Docente '{nombre}' registrado!")

        elif opcion == "2":
            print("\n[Modificar Docente]")
            cedulaBuscada = input("Ingrese la cédula del docente a modificar: ").strip()
            encontrado = False
            for d in listaDocentes:
                if d.cedula == cedulaBuscada:
                    nuevoNombre = input("Nuevo nombre (enter para omitir): ").strip()
                    if nuevoNombre: d.nombre = nuevoNombre
                    print("¡Docente modificado con éxito!")
                    encontrado = True
                    break
            if not encontrado:
                print("No se encontró un docente con esa cédula.")

        elif opcion == "3":
            print("\n--- LISTA DE DOCENTES ---")
            if not listaDocentes:
                print("No hay docentes registrados.")
            else:
                for d in listaDocentes:
                    print(d)

        elif opcion == "4":
            print("\n[Gestión de Tribunal Final para Defensa]")
            if not listaPracticantes:
                print("No hay practicantes registrados.")
            elif len(listaDocentes) < 3:
                print("Se necesitan al menos 3 docentes registrados para armar el tribunal.")
            else:
                print("Seleccione el practicante a evaluar:")
                for idx, p in enumerate(listaPracticantes):
                    print(f"{idx + 1}. {p.nombre} (Cédula: {p.cedula})")

                try:
                    p_idx = int(input("Número de practicante: ")) - 1
                    practicanteElegido = listaPracticantes[p_idx]

                    print("\nDocentes disponibles:")
                    for idx, d in enumerate(listaDocentes):
                        print(f"{idx + 1}. {d.nombre} - Asignatura: {getattr(d, 'asignatura', 'N/D')}")

                    print("\nAsigne los 3 miembros del tribunal:")
                    j1 = int(input("Número del 1er Docente: ")) - 1
                    j2 = int(input("Número del 2do Docente: ")) - 1
                    j3 = int(input("Número del 3er Docente: ")) - 1

                    nuevoTribunal = TribunalFinal(
                        practicanteElegido,
                        listaDocentes[j1],
                        listaDocentes[j2],
                        listaDocentes[j3]
                    )

                    print("\n¡Tribunal Final asignado con éxito!")
                    print(nuevoTribunal)

                except (ValueError, IndexError):
                    print("Selección inválida. Intente nuevamente.")

        elif opcion == "5":
            break
        else:
            print("Opción no válida.")


def main():
    """Función principal: carga los archivos TXT al arrancar y muestra el menú general."""
    abbCentros = ABBCentros()
    listaCentros = []
    listaAdscriptores = []
    listaPracticantes = []
    listaDocentes = []

    # 1. Cargamos los Centros Educativos desde el archivo de texto
    try:
        with open("persistencia/centros.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                centro = CentroEducativo.desdeLineaTxt(linea)
                if centro:
                    if hasattr(centro, 'cuposTotales'):
                        centro.cuposDisponibles = int(centro.cuposTotales)
                    abbCentros.insertar(centro)
                    listaCentros.append(centro)
    except FileNotFoundError:
        pass

    # 2. Cargamos los Adscriptores desde el archivo de texto
    try:
        with open("persistencia/adscriptores.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                partes = [p.strip() for p in linea.split(",")]
                if len(partes) >= 9:
                    nuevoAdsc = Adscriptor(
                        cedula=partes[0], nombre=partes[1], mail=partes[2],
                        contacto=partes[3], centroPractica=partes[8],
                        grado=partes[4], dias=partes[6], horario=partes[7]
                    )
                    listaAdscriptores.append(nuevoAdsc)
    except FileNotFoundError:
        pass

    # 3. Cargamos los Practicantes desde el archivo de texto
    try:
        with open("persistencia/practicantes.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                partes = [p.strip() for p in linea.split(",")]
                if len(partes) >= 5:
                    nuevoPrac = Practicante(partes[0], partes[1], partes[2], partes[3], partes[4])
                    listaPracticantes.append(nuevoPrac)
    except FileNotFoundError:
        pass

    # 4. Cargamos los Docentes de Didáctica desde el archivo de texto
    try:
        with open("persistencia/docentes_didactica.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                partes = [p.strip() for p in linea.split(",")]
                if len(partes) >= 4:
                    nuevoDocente = DocenteDidactica(
                        cedula=partes[0], nombre=partes[1],
                        mail="N/D", contacto="N/D", asignatura=partes[2]
                    )
                    listaDocentes.append(nuevoDocente)
    except FileNotFoundError:
        pass

    # Bucle del Menú Principal del Sistema
    while True:
        print("\n==========================================")
        print("    SISTEMA DE GESTIÓN DE PRÁCTICAS      ")
        print("==========================================")
        print("1. Centros de Prácticas")
        print("2. Adscriptores")
        print("3. Practicantes")
        print("4. Docente Didáctica y Tribunal")
        print("5. Salir")

        opcion = input("Elegir opción: ").strip()

        if opcion == "1":
            menuCentrosPracticas(abbCentros, listaCentros)
        elif opcion == "2":
            menuAdscriptores(listaAdscriptores)
        elif opcion == "3":
            menuPracticantes(listaPracticantes, listaCentros, listaAdscriptores)
        elif opcion == "4":
            menuDocenteDidactica(listaDocentes, listaPracticantes)
        elif opcion == "5":
            print("\n¡Saliendo del sistema. Hasta luego!")
            break
        else:
            print("Opción incorrecta. Intentá otra vez.")


if __name__ == "__main__":
    main()