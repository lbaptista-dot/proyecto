import os
from logica.abb_centros import ABBCentros
from logica.centro_educativo import CentroEducativo
from logica.practicante import Practicante
from logica.adscriptor import Adscriptor
from logica.docenteDidactica import DocenteDidactica
from logica.tribunalFinal import TribunalFinal
from logica.visitaDidactica import VisitaDidactica

# ==========================================
# FUNCIÓN: Calcular promedio usando una lista de notas
# ==========================================
def calcularPromedioPracticante(practicanteSeleccionado, listaVisitasRegistradas):
    # Creamos una lista limpia para almacenar exclusivamente las calificaciones numéricas del estudiante
    listaNotasEstudiante = []

    # Recorremos cada visita registrada en el sistema
    for visitaActual in listaVisitasRegistradas:
        # Verificamos si la visita corresponde al practicante que estamos evaluando
        if visitaActual.practicante.cedula == practicanteSeleccionado.cedula:
            try:
                # Convertimos la calificación a número decimal y la añadimos a la lista
                calificacionNumerica = float(visitaActual.calificacion)
                listaNotasEstudiante.append(calificacionNumerica)
            except ValueError:
                pass

    # Si la lista no contiene elementos, significa que no registra notas numéricas válidas
    if len(listaNotasEstudiante) == 0:
        return "Sin notas numéricas"

    # Calculamos el promedio dividiendo la suma total de las notas entre la cantidad de notas almacenadas
    promedioFinal = sum(listaNotasEstudiante) / len(listaNotasEstudiante)
    return promedioFinal

# ==========================================
# MENÚ: Centros de práctica
# ==========================================
def menuCentrosPracticas(abbCentros, listaCentros):
    while True:
        print("\n--- MENÚ CENTROS DE PRÁCTICA ---")
        print("1. Registrar centro")
        print("2. Modificar centro")
        print("3. Borrar centro")
        print("4. Listar centros")
        print("5. Volver al menú principal")

        opcionSeleccionada = input("Elegir opción: ").strip()

        if opcionSeleccionada == "1":
            print("\n[Registrar Centro]")
            idCentro = input("ID Centro: ").strip()
            nombreCentro = input("Nombre del centro: ").strip()
            localidadCentro = input("Localidad: ").strip()
            try:
                cuposTotalesCentro = int(input("Cupos totales: ").strip())
            except ValueError:
                cuposTotalesCentro = 0

            nuevoCentro = CentroEducativo(idCentro, nombreCentro, localidadCentro, cuposTotalesCentro)
            nuevoCentro.cuposDisponibles = cuposTotalesCentro

            abbCentros.insertar(nuevoCentro)
            listaCentros.append(nuevoCentro)

            # Guardado directo en el archivo de texto de forma segura
            try:
                with open("persistencia/centros.txt", "a") as archivoCentros:
                    archivoCentros.write(f"{idCentro}, {nombreCentro}, {localidadCentro}, {cuposTotalesCentro}\n")
            except Exception as errorArchivo:
                print("Error al guardar centro:", errorArchivo)

            print(f"¡Centro '{nombreCentro}' registrado con éxito!")

        elif opcionSeleccionada == "2":
            print("\n[Modificar Centro]")
            nombreBuscado = input("Ingrese el nombre del centro a modificar: ").strip().lower()

            centroEncontrado = None
            for centroActual in listaCentros:
                if centroActual.nombre.strip().lower() == nombreBuscado:
                    centroEncontrado = centroActual
                    break

            if centroEncontrado:
                print(f"Centro encontrado: {centroEncontrado.nombre}")
                nuevoNombre = input("Nuevo nombre (enter para omitir): ").strip()
                nuevaLocalidad = input("Nueva localidad (enter para omitir): ").strip()
                nuevosCupos = input("Nuevos cupos totales (enter para omitir): ").strip()

                if nuevoNombre: centroEncontrado.nombre = nuevoNombre
                if nuevaLocalidad: centroEncontrado.localidad = nuevaLocalidad
                if nuevosCupos:
                    try:
                        centroEncontrado.cuposTotales = int(nuevosCupos)
                        centroEncontrado.cuposDisponibles = int(nuevosCupos)
                    except ValueError:
                        pass
                print("¡Centro modificado con éxito!")
            else:
                print("No se encontró ningún centro con ese nombre.")

        elif opcionSeleccionada == "3":
            print("\n[Borrar Centro]")
            nombreBuscado = input("Ingrese el nombre del centro a borrar: ").strip().lower()
            largoInicialCentros = len(listaCentros)
            listaCentros[:] = [centroActual for centroActual in listaCentros if centroActual.nombre.strip().lower() != nombreBuscado]

            if len(listaCentros) < largoInicialCentros:
                abbCentros.raiz = None
                for centroActual in listaCentros:
                    abbCentros.insertar(centroActual)
                print("¡Centro borrado con éxito!")
            else:
                print("No se encontró ningún centro con ese nombre.")

        elif opcionSeleccionada == "4":
            print("\n--- LISTA DE CENTROS ---")
            if not listaCentros:
                print("Todavía no hay centros registrados.")
            else:
                for centroActual in listaCentros:
                    print(f"{centroActual} | Cupos: {centroActual.cuposDisponibles}/{centroActual.cuposTotales}")

        elif opcionSeleccionada == "5":
            break
        else:
            print("Opción no válida.")


# ==========================================
# MENÚ: Adscriptores
# ==========================================
def menuAdscriptores(listaAdscriptores):
    while True:
        print("\n--- MENÚ ADSCRIPTORES ---")
        print("1. Registrar adscriptor")
        print("2. Modificar adscriptor")
        print("3. Borrar adscriptor")
        print("4. Listar adscriptores")
        print("5. Volver al menú principal")

        opcionSeleccionada = input("Elegir opción: ").strip()

        if opcionSeleccionada == "1":
            print("\n[Registrar Adscriptor]")
            cedulaAdscriptor = input("Cédula: ").strip()
            nombreAdscriptor = input("Nombre: ").strip()
            mailAdscriptor = input("Mail: ").strip()
            contactoAdscriptor = input("Contacto opcional: ").strip()
            centroPracticaAdscriptor = input("Centro de práctica asignado: ").strip()
            gradoAdscriptor = input("Grado que dicta: ").strip()
            diasAdscriptor = input("Días disponibles: ").strip()
            horarioAdscriptor = input("Horario disponible: ").strip()

            nuevoAdscriptor = Adscriptor(cedulaAdscriptor, nombreAdscriptor, mailAdscriptor, contactoAdscriptor, centroPracticaAdscriptor, gradoAdscriptor, diasAdscriptor, horarioAdscriptor)
            listaAdscriptores.append(nuevoAdscriptor)

            try:
                with open("persistencia/adscriptores.txt", "a") as archivoAdscriptores:
                    archivoAdscriptores.write(f"{cedulaAdscriptor}, {nombreAdscriptor}, {mailAdscriptor}, {contactoAdscriptor}, {gradoAdscriptor}, , {diasAdscriptor}, {horarioAdscriptor}, {centroPracticaAdscriptor}\n")
            except Exception as errorArchivo:
                print("Error al guardar adscriptor:", errorArchivo)

            print(f"¡Adscriptor '{nombreAdscriptor}' registrado con éxito!")

        elif opcionSeleccionada == "2":
            print("\n[Modificar Adscriptor]")
            cedulaBuscada = input("Ingrese la cédula del adscriptor a modificar: ").strip()
            adscriptorEncontrado = False
            for adscriptorActual in listaAdscriptores:
                if adscriptorActual.cedula == cedulaBuscada:
                    nuevoNombre = input(f"Nuevo nombre [Actual: {adscriptorActual.nombre}] (enter para omitir): ").strip()
                    nuevoMail = input(f"Nuevo mail [Actual: {adscriptorActual.mail}] (enter para omitir): ").strip()
                    nuevoContacto = input(f"Nuevo contacto [Actual: {adscriptorActual.contacto}] (enter para omitir): ").strip()
                    nuevoGrado = input(f"Nuevo grado [Actual: {adscriptorActual.grado}] (enter para omitir): ").strip()

                    if nuevoNombre: adscriptorActual.nombre = nuevoNombre
                    if nuevoMail: adscriptorActual.mail = nuevoMail
                    if nuevoContacto: adscriptorActual.contacto = nuevoContacto
                    if nuevoGrado: adscriptorActual.grado = nuevoGrado

                    print("¡Adscriptor modificado con éxito!")
                    adscriptorEncontrado = True
                    break
            if not adscriptorEncontrado:
                print("No se encontró un adscriptor con esa cédula.")

        elif opcionSeleccionada == "3":
            print("\n--- Borrar Adscriptor ---")
            cedulaBuscada = input("Ingrese la cédula del adscriptor a borrar: ").strip()
            largoInicialAdscriptores = len(listaAdscriptores)
            listaAdscriptores[:] = [adscriptorActual for adscriptorActual in listaAdscriptores if adscriptorActual.cedula != cedulaBuscada]
            if len(listaAdscriptores) < largoInicialAdscriptores:
                print("¡Adscriptor borrado con éxito!")
            else:
                print("No se encontró esa cédula.")

        elif opcionSeleccionada == "4":
            print("\n--- LISTA DE ADSCRIPTORES ---")
            if not listaAdscriptores:
                print("No hay adscriptores registrados.")
            else:
                for adscriptorActual in listaAdscriptores:
                    print(adscriptorActual)

        elif opcionSeleccionada == "5":
            break
        else:
            print("Opción no válida.")


# ==========================================
# MENÚ: Practicantes
# ==========================================
def menuPracticantes(listaPracticantes, listaCentros, listaAdscriptores, listaVisitas):
    while True:
        print("\n--- MENÚ PRACTICANTES ---")
        print("1. Registrar practicante")
        print("2. Modificar practicante")
        print("3. Borrar practicante")
        print("4. Listar practicantes (Con promedios en tiempo real)")
        print("5. Asignar centro de práctica")
        print("6. Volver al menú principal")

        opcionSeleccionada = input("Elegir opción: ").strip()

        if opcionSeleccionada == "1":
            print("\n[Registrar Practicante]")
            cedulaPracticante = input("Cédula: ").strip()
            nombrePracticante = input("Nombre: ").strip()
            mailPracticante = input("Mail: ").strip()
            contactoPracticante = input("Contacto opcional: ").strip()
            gradoPracticante = input("Grado: ").strip()

            nuevoPracticante = Practicante(cedulaPracticante, nombrePracticante, mailPracticante, contactoPracticante, gradoPracticante)
            listaPracticantes.append(nuevoPracticante)

            try:
                with open("persistencia/practicantes.txt", "a") as archivoPracticantes:
                    archivoPracticantes.write(f"{cedulaPracticante}, {nombrePracticante}, {mailPracticante}, {contactoPracticante}, {gradoPracticante}\n")
            except Exception as errorArchivo:
                print("Error al guardar practicante:", errorArchivo)

            print(f"¡Practicante '{nombrePracticante}' registrado!")

        elif opcionSeleccionada == "2":
            print("\n[Modificar Practicante]")
            cedulaBuscada = input("Ingrese la cédula del practicante a modificar: ").strip()
            practicanteEncontrado = False
            for practicanteActual in listaPracticantes:
                if practicanteActual.cedula == cedulaBuscada:
                    nuevoNombre = input(f"Nuevo nombre [Actual: {practicanteActual.nombre}] (enter para omitir): ").strip()
                    nuevoMail = input(f"Nuevo mail [Actual: {practicanteActual.mail}] (enter para omitir): ").strip()
                    nuevoContacto = input(f"Nuevo contacto [Actual: {practicanteActual.contacto}] (enter para omitir): ").strip()
                    nuevoGrado = input(f"Nuevo grado [Actual: {practicanteActual.grado}] (enter para omitir): ").strip()

                    if nuevoNombre: practicanteActual.nombre = nuevoNombre
                    if nuevoMail: practicanteActual.mail = nuevoMail
                    if nuevoContacto: practicanteActual.contacto = nuevoContacto
                    if nuevoGrado: practicanteActual.grado = nuevoGrado

                    print("¡Practicante modificado con éxito!")
                    practicanteEncontrado = True
                    break
            if not practicanteEncontrado:
                print("No se encontró un practicante con esa cédula.")

        elif opcionSeleccionada == "3":
            print("\n[Borrar Practicante]")
            cedulaBuscada = input("Ingrese la cédula del practicante a borrar: ").strip()

            for practicanteActual in listaPracticantes:
                if practicanteActual.cedula == cedulaBuscada and hasattr(practicanteActual, 'centroObjeto') and practicanteActual.centroObjeto:
                    practicanteActual.centroObjeto.cuposDisponibles += 1

            largoInicialPracticantes = len(listaPracticantes)
            listaPracticantes[:] = [practicanteActual for practicanteActual in listaPracticantes if practicanteActual.cedula != cedulaBuscada]
            if len(listaPracticantes) < largoInicialPracticantes:
                print("¡Practicante borrado y cupo devuelto al centro!")
            else:
                print("No se encontró esa cédula.")

        elif opcionSeleccionada == "4":
            print("\n--- LISTA DE PRACTICANTES Y PROMEDIOS ---")
            if not listaPracticantes:
                print("No hay practicantes registrados.")
            else:
                for practicanteActual in listaPracticantes:
                    promedioActual = calcularPromedioPracticante(practicanteActual, listaVisitas)
                    print(f"Cédula: {practicanteActual.cedula} | Nombre: {practicanteActual.nombre} | Grado: {practicanteActual.grado} | 📊 Promedio: {promedioActual}")

        elif opcionSeleccionada == "5":
            print("\n[Asignación de Práctica]")
            cedulaBuscada = input("Ingrese la cédula del practicante: ").strip()

            practicanteEncontrado = None
            for practicanteActual in listaPracticantes:
                if practicanteActual.cedula == cedulaBuscada:
                    practicanteEncontrado = practicanteActual
                    break

            if not practicanteEncontrado:
                print("No se encontró un practicante con esa cédula.")
            else:
                if not listaCentros:
                    print("No hay centros educativos registrados.")
                else:
                    print(f"\nPracticante: {practicanteEncontrado.nombre}")
                    print("\nCentros disponibles:")
                    for indiceCentro, centroActual in enumerate(listaCentros):
                        print(f"{indiceCentro + 1}. {centroActual.nombre} (Disponibles: {centroActual.cuposDisponibles})")

                    try:
                        seleccionCentro = int(input("Seleccione el número del centro: ")) - 1
                        if 0 <= seleccionCentro < len(listaCentros):
                            centroElegido = listaCentros[seleccionCentro]

                            if centroElegido.cuposDisponibles <= 0:
                                print("¡Error! Este centro ya no tiene cupos.")
                                continue

                            adscriptorEncontrado = None
                            for adscriptorActual in listaAdscriptores:
                                if adscriptorActual.centroPractica.strip().lower() == centroElegido.nombre.strip().lower():
                                    adscriptorEncontrado = adscriptorActual
                                    break

                            if adscriptorEncontrado:
                                nombreAdscriptorTxt = adscriptorEncontrado.nombre
                                diasSugeridos = adscriptorEncontrado.dias
                                horarioSugerido = adscriptorEncontrado.horario
                            else:
                                nombreAdscriptorTxt = "Sin adscriptor"
                                diasSugeridos = "A definir"
                                horarioSugerido = "A definir"

                            diasInput = input(f"\nDías de práctica [Sugerido: {diasSugeridos}] (Enter para aceptar): ").strip()
                            diasAsignados = diasInput if diasInput else diasSugeridos

                            horarioInput = input(f"Horario [Sugerido: {horarioSugerido}] (Enter para aceptar): ").strip()
                            horarioAsignado = horarioInput if horarioInput else horarioSugerido

                            centroElegido.cuposDisponibles -= 1

                            practicanteEncontrado.centroAsignado = centroElegido.nombre
                            practicanteEncontrado.adscriptorAsignado = nombreAdscriptorTxt
                            practicanteEncontrado.diasPractica = diasAsignados
                            practicanteEncontrado.horarioPractica = horarioAsignado
                            practicanteEncontrado.centroObjeto = centroElegido

                            print(f"¡Asignación exitosa! Quedan {centroElegido.cuposDisponibles} cupos.")
                        else:
                            print("Número inválido.")
                    except ValueError:
                        print("Por favor, ingrese un número válido.")

        elif opcionSeleccionada == "6":
            break
        else:
            print("Opción no válida.")


# ==========================================
# MENÚ: Docente de Didáctica, Visitas y Tribunal
# ==========================================
def menuDocenteDidactica(listaDocentes, listaAdscriptores, listaPracticantes, listaVisitas):
    while True:
        print("\n--- MENÚ DOCENTE DIDÁCTICA Y TRIBUNAL ---")
        print("1. Registrar docente")
        print("2. Modificar docente")
        print("3. Listar docentes")
        print("4. Registrar nueva visita a practicante")
        print("5. Calcular promedio final de visitas de un practicante")
        print("6. Listar todas las visitas realizadas")
        print("7. Armar tribunal final")
        print("8. Volver al menú principal")

        opcionSeleccionada = input("Elegir opción: ").strip()

        if opcionSeleccionada == "1":
            print("\n[Registrar Docente]")
            cedulaDocente = input("Cédula: ").strip()
            nombreDocente = input("Nombre: ").strip()
            mailDocente = input("Mail: ").strip()
            contactoDocente = input("Contacto opcional: ").strip()
            asignaturaDocente = input("Asignatura / Cargo: ").strip()

            nuevoDocente = DocenteDidactica(cedulaDocente, nombreDocente, mailDocente, contactoDocente, asignaturaDocente)
            listaDocentes.append(nuevoDocente)

            try:
                with open("persistencia/docentes_didactica.txt", "a") as archivoDocentes:
                    archivoDocentes.write(f"{cedulaDocente}, {nombreDocente}, {asignaturaDocente}\n")
            except Exception as errorArchivo:
                print("Error al guardar docente:", errorArchivo)

            print(f"¡Docente '{nombreDocente}' registrado y guardado con éxito!")

        elif opcionSeleccionada == "2":
            print("\n[Modificar Docente]")
            cedulaBuscada = input("Ingrese la cédula del docente a modificar: ").strip()
            docenteEncontrado = False
            for docenteActual in listaDocentes:
                if docenteActual.cedula == cedulaBuscada:
                    nuevoNombre = input(f"Nuevo nombre [Actual: {docenteActual.nombre}] (enter para omitir): ").strip()
                    nuevoMail = input(f"Nuevo mail [Actual: {docenteActual.mail}] (enter para omitir): ").strip()
                    nuevoContacto = input(f"Nuevo contacto [Actual: {docenteActual.contacto}] (enter para omitir): ").strip()
                    nuevaAsignatura = input(f"Nuevo cargo/asignatura [Actual: {docenteActual.asignatura}] (enter para omitir): ").strip()

                    if nuevoNombre: docenteActual.nombre = nuevoNombre
                    if nuevoMail: docenteActual.mail = nuevoMail
                    if nuevoContacto: docenteActual.contacto = nuevoContacto
                    if nuevaAsignatura: docenteActual.asignatura = nuevaAsignatura

                    print("¡Docente modificado con éxito!")
                    docenteEncontrado = True
                    break
            if not docenteEncontrado:
                print("No se encontró un docente con esa cédula.")

        elif opcionSeleccionada == "3":
            print("\n--- LISTA DE DOCENTES ---")
            if not listaDocentes:
                print("No hay docentes registrados.")
            else:
                for docenteActual in listaDocentes:
                    print(f"Cédula: {docenteActual.cedula} | Nombre: {docenteActual.nombre} | Cargo: {docenteActual.asignatura}")

        elif opcionSeleccionada == "4":
            print("\n[Registrar Visita a Practicante]")
            if not listaDocentes:
                print("Primero debe registrar docentes de didáctica.")
            elif not listaPracticantes:
                print("No hay practicantes registrados.")
            else:
                cedulaDocenteVisita = input("1. Ingrese la Cédula del Docente de Didáctica: ").strip()
                docenteEncontrado = None
                for docenteActual in listaDocentes:
                    if docenteActual.cedula.strip() == cedulaDocenteVisita:
                        docenteEncontrado = docenteActual
                        break

                if not docenteEncontrado:
                    print("No se encontró ningún docente con esa cédula.")
                    continue

                cedulaPracticanteVisita = input("2. Ingrese la Cédula del Practicante: ").strip()
                practicanteEncontrado = None
                for practicanteActual in listaPracticantes:
                    if practicanteActual.cedula.strip() == cedulaPracticanteVisita:
                        practicanteEncontrado = practicanteActual
                        break

                if not practicanteEncontrado:
                    print("No se encontró ningún practicante con esa cédula.")
                    continue

                fechaVisita = input("3. Fecha de la visita (ej: 09/09/2026): ").strip()
                observacionesVisita = input("4. Observaciones de la clase: ").strip()
                calificacionVisita = input("5. Calificación o Nota numérica (ej: 9 o 8.5): ").strip()

                nuevaVisita = VisitaDidactica(docenteEncontrado, practicanteEncontrado, fechaVisita, calificacionVisita, observacionesVisita)
                listaVisitas.append(nuevaVisita)

                try:
                    with open("persistencia/visitas.txt", "a") as archivoVisitas:
                        archivoVisitas.write(f"{docenteEncontrado.cedula}, {practicanteEncontrado.cedula}, {fechaVisita}, {calificacionVisita}, {observacionesVisita}\n")
                except Exception as errorArchivo:
                    print("Error al guardar visita:", errorArchivo)

                promedioActual = calcularPromedioPracticante(practicanteEncontrado, listaVisitas)
                print(f"\n ¡Visita registrada con éxito!")
                print(f"    Promedio actual del practicante: {promedioActual}")

        elif opcionSeleccionada == "5":
            print("\n[Calcular Promedio Final de Visitas]")
            if not listaPracticantes:
                print("No hay practicantes registrados.")
            else:
                cedulaBuscada = input("Ingrese la cédula del practicante: ").strip()
                practicanteBuscado = None
                for practicanteActual in listaPracticantes:
                    if practicanteActual.cedula.strip() == cedulaBuscada:
                        practicanteBuscado = practicanteActual
                        break

                if not practicanteBuscado:
                    print("No se encontró un practicante con esa cédula.")
                else:
                    promedioFinal = calcularPromedioPracticante(practicanteBuscado, listaVisitas)
                    print(f"\n--- INFORME FINAL DE VISITAS ---")
                    print(f"Practicante: {practicanteBuscado.nombre}")
                    print(f"Cédula: {practicanteBuscado.cedula}")
                    print(f"Promedio final de notas: {promedioFinal}")

        elif opcionSeleccionada == "6":
            print("\n--- LISTA DE VISITAS REGISTRADAS ---")
            if not listaVisitas:
                print("Aún no hay visitas registradas.")
            else:
                for visitaActual in listaVisitas:
                    print(visitaActual)

        elif opcionSeleccionada == "7":
            print("\n[Gestión de Tribunal Final]")
            if not listaPracticantes:
                print("No hay practicantes registrados.")
            elif len(listaDocentes) < 1 and len(listaAdscriptores) < 1:
                print("Se necesitan docentes o adscriptores registrados.")
            else:
                print("\nPracticantes:")
                for practicanteActual in listaPracticantes:
                    print(f"- Cédula: {practicanteActual.cedula} | Nombre: {practicanteActual.nombre}")

                cedulaPracticanteElegido = input("Ingrese la Cédula del practicante a evaluar: ").strip()
                practicanteElegido = None
                for practicanteActual in listaPracticantes:
                    if practicanteActual.cedula.strip() == cedulaPracticanteElegido:
                        practicanteElegido = practicanteActual
                        break

                if not practicanteElegido:
                    print("Practicante no encontrado.")
                    continue

                def buscarMiembroTribunal(mensajePrompt):
                    while True:
                        cedulaIngresada = input(mensajePrompt).strip()
                        for docenteActual in listaDocentes:
                            if docenteActual.cedula.strip() == cedulaIngresada:
                                return docenteActual
                        for adscriptorActual in listaAdscriptores:
                            if adscriptorActual.cedula.strip() == cedulaIngresada:
                                return adscriptorActual
                        print("No se encontró ningún docente ni adscriptor con esa cédula. Intente de nuevo.")

                print("\nAsignando Tribunal:")
                primerMiembro = buscarMiembroTribunal("Cédula del 1er Miembro (Docente/Adscriptor): ")
                segundoMiembro = buscarMiembroTribunal("Cédula del 2do Miembro (Docente/Adscriptor): ")

                print("\n3er Miembro:")
                print("1. Seleccionar existente (Docente o Adscriptor)")
                print("2. Crear uno nuevo en el momento")
                opcionTercero = input("Elija opción: ").strip()

                if opcionTercero == "1":
                    tercerMiembro = buscarMiembroTribunal("Cédula del 3er Miembro: ")
                else:
                    cedulaNuevoDocente = input("Cédula: ").strip()
                    nombreNuevoDocente = input("Nombre: ").strip()
                    cargoNuevoDocente = input("Cargo o Asignatura: ").strip()
                    tercerMiembro = DocenteDidactica(cedulaNuevoDocente, nombreNuevoDocente, "N/D", "N/D", cargoNuevoDocente)
                    listaDocentes.append(tercerMiembro)

                    try:
                        with open("persistencia/docentes_didactica.txt", "a") as archivoDocentes:
                            archivoDocentes.write(f"{cedulaNuevoDocente}, {nombreNuevoDocente}, {cargoNuevoDocente}\n")
                    except Exception as errorArchivo:
                        print("Aviso al guardar en archivo:", errorArchivo)

                nuevoTribunal = TribunalFinal(practicanteElegido, primerMiembro, segundoMiembro, tercerMiembro)
                print("\n¡Tribunal asignado con éxito!")
                print(nuevoTribunal)

        elif opcionSeleccionada == "8":
            break
        else:
            print("Opción no válida.")


# ==========================================
# FUNCIÓN PRINCIPAL (MAIN)
# ==========================================
def main():
    abbCentros = ABBCentros()
    listaCentros = []
    listaAdscriptores = []
    listaPracticantes = []
    listaDocentes = []
    listaVisitas = []

    # 1. Cargamos centros guardados
    try:
        with open("persistencia/centros.txt", "r") as archivoCentros:
            for lineaActual in archivoCentros:
                centroActual = CentroEducativo.desdeLineaTxt(lineaActual)
                if centroActual:
                    centroActual.cuposDisponibles = int(centroActual.cuposTotales)
                    abbCentros.insertar(centroActual)
                    listaCentros.append(centroActual)
    except FileNotFoundError:
        pass

    # 2. Cargamos adscriptores guardados
    try:
        with open("persistencia/adscriptores.txt", "r") as archivoAdscriptores:
            for lineaActual in archivoAdscriptores:
                partesLinea = [parte.strip() for parte in lineaActual.split(",")]
                if len(partesLinea) >= 9:
                    nuevoAdscriptor = Adscriptor(
                        cedula=partesLinea[0], nombre=partesLinea[1], mail=partesLinea[2],
                        contacto=partesLinea[3], centroPractica=partesLinea[8],
                        grado=partesLinea[4], dias=partesLinea[6], horario=partesLinea[7]
                    )
                    listaAdscriptores.append(nuevoAdscriptor)
    except FileNotFoundError:
        pass

    # 3. Cargamos practicantes guardados
    try:
        with open("persistencia/practicantes.txt", "r") as archivoPracticantes:
            for lineaActual in archivoPracticantes:
                partesLinea = [parte.strip() for parte in lineaActual.split(",")]
                if len(partesLinea) >= 5:
                    nuevoPracticante = Practicante(partesLinea[0], partesLinea[1], partesLinea[2], partesLinea[3], partesLinea[4])
                    listaPracticantes.append(nuevoPracticante)
    except FileNotFoundError:
        pass

    # 4. Cargamos docentes de didáctica guardados
    try:
        with open("persistencia/docentes_didactica.txt", "r") as archivoDocentes:
            for lineaActual in archivoDocentes:
                partesLinea = [parte.strip() for parte in lineaActual.split(",")]
                if len(partesLinea) >= 3:
                    nuevoDocente = DocenteDidactica(
                        cedula=partesLinea[0], nombre=partesLinea[1],
                        mail="N/D", contacto="N/D", asignatura=partesLinea[2]
                    )
                    listaDocentes.append(nuevoDocente)
    except FileNotFoundError:
        pass

    # 5. Cargamos las visitas guardadas y las vinculamos correctamente
    try:
        with open("persistencia/visitas.txt", "r") as archivoVisitas:
            for lineaActual in archivoVisitas:
                partesLinea = [parte.strip() for parte in lineaActual.split(",")]
                if len(partesLinea) >= 5:
                    cedulaDocenteArchivo, cedulaPracticanteArchivo, fechaVisitaArchivo, calificacionVisitaArchivo, observacionesVisitaArchivo = partesLinea[0], partesLinea[1], partesLinea[2], partesLinea[3], partesLinea[4]

                    docenteObj = None
                    for docenteActual in listaDocentes:
                        if docenteActual.cedula.strip() == cedulaDocenteArchivo:
                            docenteObj = docenteActual
                            break

                    practicanteObj = None
                    for practicanteActual in listaPracticantes:
                        if practicanteActual.cedula.strip() == cedulaPracticanteArchivo:
                            practicanteObj = practicanteActual
                            break

                    if docenteObj and practicanteObj:
                        nuevaVisita = VisitaDidactica(docenteObj, practicanteObj, fechaVisitaArchivo, calificacionVisitaArchivo, observacionesVisitaArchivo)
                        listaVisitas.append(nuevaVisita)
    except FileNotFoundError:
        pass

    # Menú Principal del Programa
    while True:
        print("\n==========================================")
        print("    SISTEMA DE GESTIÓN DE PRÁCTICAS      ")
        print("==========================================")
        print("1. Gestionar Centros de Prácticas")
        print("2. Gestionar Adscriptores")
        print("3. Gestionar Practicantes")
        print("4. Docente Didáctica, Visitas y Tribunal")
        print("5. Salir del sistema")

        opcionSeleccionada = input("Elegir opción: ").strip()

        if opcionSeleccionada == "1":
            menuCentrosPracticas(abbCentros, listaCentros)
        elif opcionSeleccionada == "2":
            menuAdscriptores(listaAdscriptores)
        elif opcionSeleccionada == "3":
            menuPracticantes(listaPracticantes, listaCentros, listaAdscriptores, listaVisitas)
        elif opcionSeleccionada == "4":
            menuDocenteDidactica(listaDocentes, listaAdscriptores, listaPracticantes, listaVisitas)
        elif opcionSeleccionada == "5":
            print("\n¡Saliendo del sistema. Hasta luego!")
            break
        else:
            print("Opción incorrecta. Intentá otra vez.")


if __name__ == "__main__":
    main()