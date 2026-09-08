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

            nuevoCentro = CentroEducativo(idCentro, nombre, localidad, cuposTotales)
            nuevoCentro.cuposDisponibles = cuposTotales

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

                            centroElegido.cuposDisponibles -= 1

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
    """Menú para gestionar docentes y armar el tribunal con opción flexible para el 3er miembro."""
    while True:
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
            asignatura = input("Asignatura / Especialidad: ").strip()

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
                    print(f"Cédula: {d.cedula} | Nombre: {d.nombre} | Especialidad/Cargo: {getattr(d, 'asignatura', 'N/D')}")

        elif opcion == "4":
            print("\n[Gestión de Tribunal Final para Defensa]")
            if not listaPracticantes:
                print("No hay practicantes registrados.")
            elif len(listaDocentes) < 2:
                print(f"Se necesitan al menos 2 docentes base en el sistema. Hay {len(listaDocentes)} registrados.")
            else:
                print("\nPracticantes disponibles:")
                for p in listaPracticantes:
                    print(f"- Cédula: {p.cedula} | Nombre: {p.nombre}")

                cedPrac = input("Ingrese la Cédula o Nombre del practicante a evaluar: ").strip().lower()
                practicanteElegido = None
                for p in listaPracticantes:
                    if p.cedula.strip().lower() == cedPrac or p.nombre.strip().lower() == cedPrac:
                        practicanteElegido = p
                        break

                if not practicanteElegido:
                    print("No se encontró al practicante.")
                    continue

                print(f"\nDocentes/Directores disponibles en el sistema:")
                for d in listaDocentes:
                    print(f"- Cédula: {d.cedula} | Nombre: {d.nombre} | Especialidad/Cargo: {getattr(d, 'asignatura', 'N/D')}")

                def buscarDocentePorInput(mensaje):
                    while True:
                        ingreso = input(mensaje).strip().lower()
                        for d in listaDocentes:
                            if d.cedula.strip().lower() == ingreso or d.nombre.strip().lower() == ingreso:
                                return d
                        print("Docente no encontrado. Verifique la cédula o el nombre e intente de nuevo.")

                print("\nAsignando los miembros del tribunal:")
                doc1 = buscarDocentePorInput("Ingrese el 1er Miembro (Cédula o Nombre): ")
                doc2 = buscarDocentePorInput("Ingrese el 2do Miembro (Cédula o Nombre): ")

                # Elección para el 3er miembro: Existente o Nuevo en el momento
                print("\n--- 3er MIEMBRO DEL TRIBUNAL ---")
                print("1. Seleccionar un docente existente de la lista")
                print("2. Agregar uno nuevo en el momento (Director, Adscriptor u otra especialidad/cargo)")
                opcionTercero = input("Seleccione una opción para el 3er miembro: ").strip()

                doc3 = None
                if opcionTercero == "1":
                    doc3 = buscarDocentePorInput("Ingrese el 3er Miembro existente (Cédula o Nombre): ")
                elif opcionTercero == "2":
                    print("\n[Registrar Nuevo Miembro para el Tribunal]")
                    cedula3 = input("Cédula: ").strip()
                    nombre3 = input("Nombre: ").strip()
                    mail3 = input("Mail (opcional): ").strip()
                    contacto3 = input("Contacto (opcional): ").strip()
                    especialidadCargo = input("Especialidad o Cargo (ej: Director, Adscriptor, Informática, etc.): ").strip()

                    doc3 = DocenteDidactica(cedula3, nombre3, mail3 if mail3 else "N/D", contacto3 if contacto3 else "N/D", especialidadCargo)
                    listaDocentes.append(doc3) # Lo guardamos también en la lista general
                    print(f"¡Nuevo miembro '{nombre3}' ({especialidadCargo}) registrado y sumado al tribunal!")
                else:
                    print("Opción no válida. Se tomará por defecto un docente existente.")
                    doc3 = buscarDocentePorInput("Ingrese el 3er Miembro existente (Cédula o Nombre): ")

                nuevoTribunal = TribunalFinal(practicanteElegido, doc1, doc2, doc3)

                print("\n¡Tribunal Final asignado con éxito!")
                print(nuevoTribunal)

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

    # 1. Cargamos los Centros Educativos
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

    # 2. Cargamos los Adscriptores
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

    # 3. Cargamos los Practicantes
    try:
        with open("persistencia/practicantes.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                partes = [p.strip() for p in linea.split(",")]
                if len(partes) >= 5:
                    nuevoPrac = Practicante(partes[0], partes[1], partes[2], partes[3], partes[4])
                    listaPracticantes.append(nuevoPrac)
    except FileNotFoundError:
        pass

    # 4. Cargamos los Docentes de Didáctica
    try:
        with open("persistencia/docentes_didactica.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                partes = [p.strip() for p in linea.split(",")]
                if len(partes) >= 3:
                    nuevoDocente = DocenteDidactica(
                        cedula=partes[0], nombre=partes[1],
                        mail="N/D", contacto="N/D", asignatura=partes[2]
                    )
                    listaDocentes.append(nuevoDocente)
    except FileNotFoundError:
        pass

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