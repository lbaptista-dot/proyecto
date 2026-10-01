# ==========================================
# IMPORTACIÓN DE CLASES Y MÓDULOS NECESARIOS
# ==========================================
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
    listaNotasEstudiante = []

    # Recorremos todas las visitas registradas en el sistema
    for visitaActual in listaVisitasRegistradas:
        # Si la visita pertenece al estudiante que estamos consultando
        if visitaActual.practicante.cedula == practicanteSeleccionado.cedula:
            try:
                # Intentamos convertir la calificación a número para poder promediarla
                calificacionNumerica = float(visitaActual.calificacion)
                listaNotasEstudiante.append(calificacionNumerica)
            except ValueError:
                pass  # Si la nota no es un número válido, la ignoramos

    # Si no tiene notas cargadas, devolvemos un texto avisando
    if len(listaNotasEstudiante) == 0:
        return "Sin notas numéricas"

    # Calculamos el promedio sumando todo y dividiendo entre la cantidad de notas
    promedioFinal = sum(listaNotasEstudiante) / len(listaNotasEstudiante)
    return promedioFinal

# ==========================================
# MENÚ: Administrar los centros de práctica educativa
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

        # Opción 1: Crear un centro nuevo y guardarlo en el archivo
        if opcionSeleccionada == "1":
            print("\n[Registrar Centro]")
            idCentro = input("ID Centro: ").strip()
            nombreCentro = input("Nombre del centro: ").strip()
            localidadCentro = input("Localidad: ").strip()
            try:
                cuposTotalesCentro = int(input("Cupos totales: ").strip())
            except ValueError:
                cuposTotalesCentro = 0

            # Creamos el objeto con los datos ingresados
            nuevoCentro = CentroEducativo(idCentro, nombreCentro, localidadCentro, cuposTotalesCentro)
            nuevoCentro.cuposDisponibles = cuposTotalesCentro

            # Lo guardamos en el árbol y en la lista general del programa
            abbCentros.insertar(nuevoCentro)
            listaCentros.append(nuevoCentro)

            # Guardamos la lista completa actualizada en el archivo usando idCentro
            try:
                archivoCentros = open("persistencia/centros.txt", "w")
                for centroActual in listaCentros:
                    archivoCentros.write(str(centroActual.idCentro) + ", " + str(centroActual.nombre) + ", " + str(centroActual.localidad) + ", " + str(centroActual.cuposTotales) + "\n")
                archivoCentros.close()
            except Exception as errorArchivo:
                print("Error al guardar en el archivo de centros:", errorArchivo)

            print("¡Centro '" + nombreCentro + "' registrado con éxito!")

        # Opción 2: Modificar los datos de un centro existente y actualizar archivo
        elif opcionSeleccionada == "2":
            print("\n[Modificar Centro]")
            nombreBuscado = input("Ingrese el nombre del centro a modificar: ").strip().lower()

            centroEncontrado = None
            for centroActual in listaCentros:
                if centroActual.nombre.strip().lower() == nombreBuscado:
                    centroEncontrado = centroActual
                    break

            if centroEncontrado:
                print("Centro encontrado: " + centroEncontrado.nombre)
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

                # Sobrescribimos el archivo con la lista actualizada
                try:
                    archivoCentros = open("persistencia/centros.txt", "w")
                    for centroActual in listaCentros:
                        archivoCentros.write(str(centroActual.idCentro) + ", " + str(centroActual.nombre) + ", " + str(centroActual.localidad) + ", " + str(centroActual.cuposTotales) + "\n")
                    archivoCentros.close()
                except Exception as errorArchivo:
                    print("Error al actualizar el archivo de centros:", errorArchivo)

                print("¡Centro modificado y guardado con éxito!")
            else:
                print("No se encontró ningún centro con ese nombre.")

        # Opción 3: Eliminar un centro del sistema y actualizar archivo
        elif opcionSeleccionada == "3":
            print("\n[Borrar Centro]")
            nombreBuscado = input("Ingrese el nombre del centro a borrar: ").strip().lower()
            largoInicialCentros = len(listaCentros)

            # Filtramos la lista para sacar al centro que coincida con el nombre
            listaCentros[:] = [centroActual for centroActual in listaCentros if centroActual.nombre.strip().lower() != nombreBuscado]

            if len(listaCentros) < largoInicialCentros:
                # Reconstruimos el árbol binario porque cambió la lista
                abbCentros.raiz = None
                for centroActual in listaCentros:
                    abbCentros.insertar(centroActual)

                # Guardamos los cambios en el archivo de texto
                try:
                    archivoCentros = open("persistencia/centros.txt", "w")
                    for centroActual in listaCentros:
                        archivoCentros.write(str(centroActual.idCentro) + ", " + str(centroActual.nombre) + ", " + str(centroActual.localidad) + ", " + str(centroActual.cuposTotales) + "\n")
                    archivoCentros.close()
                except Exception as errorArchivo:
                    print("Error al actualizar el archivo de centros:", errorArchivo)

                print("¡Centro borrado y archivo actualizado con éxito!")
            else:
                print("No se encontró ningún centro con ese nombre.")

        # Opción 4: Mostrar todos los centros que están registrados
        elif opcionSeleccionada == "4":
            print("\n--- LISTA DE CENTROS ---")
            if not listaCentros:
                print("Todavía no hay centros registrados.")
            else:
                for centroActual in listaCentros:
                    print(str(centroActual) + " | Disponibles: " + str(centroActual.cuposDisponibles) + "/" + str(centroActual.cuposTotales))

        # Opción 5: Salir de este menú y volver al anterior
        elif opcionSeleccionada == "5":
            break
        else:
            print("Opción no válida.")

# ==========================================
# MENÚ: Administrar a los adscriptores
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

        # Opción 1: Registrar un nuevo adscriptor y guardarlo
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

            # Guardamos la lista completa actualizada en el archivo de texto
            try:
                archivoAdscriptores = open("persistencia/adscriptores.txt", "w")
                for adscriptorActual in listaAdscriptores:
                    archivoAdscriptores.write(
                        adscriptorActual.cedula + ", " +
                        adscriptorActual.nombre + ", " +
                        adscriptorActual.mail + ", " +
                        adscriptorActual.contacto + ", " +
                        adscriptorActual.grado + ", , " +
                        adscriptorActual.dias + ", " +
                        adscriptorActual.horario + ", " +
                        adscriptorActual.centroPractica + "\n"
                    )
                archivoAdscriptores.close()
            except Exception as errorArchivo:
                print("Error al guardar adscriptor:", errorArchivo)

            print("¡Adscriptor '" + nombreAdscriptor + "' registrado con éxito!")

        # Opción 2: Modificar adscriptor buscando por cédula y actualizar archivo
        elif opcionSeleccionada == "2":
            print("\n[Modificar Adscriptor]")
            cedulaBuscada = input("Ingrese la cédula del adscriptor a modificar: ").strip()
            adscriptorEncontrado = False
            for adscriptorActual in listaAdscriptores:
                if adscriptorActual.cedula == cedulaBuscada:
                    nuevoNombre = input("Nuevo nombre [Actual: " + adscriptorActual.nombre + "] (enter para omitir): ").strip()
                    nuevoMail = input("Nuevo mail [Actual: " + adscriptorActual.mail + "] (enter para omitir): ").strip()
                    nuevoContacto = input("Nuevo contacto [Actual: " + adscriptorActual.contacto + "] (enter para omitir): ").strip()
                    nuevoGrado = input("Nuevo grado [Actual: " + adscriptorActual.grado + "] (enter para omitir): ").strip()

                    if nuevoNombre: adscriptorActual.nombre = nuevoNombre
                    if nuevoMail: adscriptorActual.mail = nuevoMail
                    if nuevoContacto: adscriptorActual.contacto = nuevoContacto
                    if nuevoGrado: adscriptorActual.grado = nuevoGrado

                    # Guardamos los cambios actualizados en el archivo
                    try:
                        archivoAdscriptores = open("persistencia/adscriptores.txt", "w")
                        for a in listaAdscriptores:
                            archivoAdscriptores.write(
                                a.cedula + ", " + a.nombre + ", " + a.mail + ", " +
                                a.contacto + ", " + a.grado + ", , " + a.dias + ", " +
                                a.horario + ", " + a.centroPractica + "\n"
                            )
                        archivoAdscriptores.close()
                    except Exception as errorArchivo:
                        print("Error al actualizar el archivo:", errorArchivo)

                    print("¡Adscriptor modificado y guardado con éxito!")
                    adscriptorEncontrado = True
                    break
            if not adscriptorEncontrado:
                print("No se encontró un adscriptor con esa cédula.")

        # Opción 3: Borrar adscriptor de la lista y actualizar el archivo de texto
        elif opcionSeleccionada == "3":
            print("\n--- Borrar Adscriptor ---")
            cedulaBuscada = input("Ingrese la cédula del adscriptor a borrar: ").strip()
            largoInicialAdscriptores = len(listaAdscriptores)

            # Filtramos la lista para sacar al adscriptor que coincida con la cédula
            listaAdscriptores[:] = [adscriptorActual for adscriptorActual in listaAdscriptores if adscriptorActual.cedula != cedulaBuscada]

            if len(listaAdscriptores) < largoInicialAdscriptores:
                # Sobrescribimos el archivo de texto con los adscriptores que quedaron
                try:
                    archivoAdscriptores = open("persistencia/adscriptores.txt", "w")
                    for adscriptorActual in listaAdscriptores:
                        archivoAdscriptores.write(
                            adscriptorActual.cedula + ", " +
                            adscriptorActual.nombre + ", " +
                            adscriptorActual.mail + ", " +
                            adscriptorActual.contacto + ", " +
                            adscriptorActual.grado + ", , " +
                            adscriptorActual.dias + ", " +
                            adscriptorActual.horario + ", " +
                            adscriptorActual.centroPractica + "\n"
                        )
                    archivoAdscriptores.close()
                except Exception as errorArchivo:
                    print("Error al actualizar el archivo de adscriptores:", errorArchivo)

                print("¡Adscriptor borrado con éxito y archivo actualizado!")
            else:
                print("No se encontró esa cédula.")

        # Opción 4: Listar a todos los adscriptores
        elif opcionSeleccionada == "4":
            print("\n--- LISTA DE ADSCRIPTORES ---")
            if not listaAdscriptores:
                print("No hay adscriptores registrados.")
            else:
                for adscriptorActual in listaAdscriptores:
                    print(str(adscriptorActual))

        elif opcionSeleccionada == "5":
            break
        else:
            print("Opción no válida.")

# ==========================================
# MENÚ: Administrar practicantes y asignaciones de centros
# ==========================================
def menuPracticantes(listaPracticantes, listaCentros, listaAdscriptores, listaVisitas):
    while True:
        print("\n--- MENÚ PRACTICANTES ---")
        print("1. Registrar practicante")
        print("2. Modificar practicante")
        print("3. Borrar practicante")
        print("4. Listar practicantes (Con estado y promedios)")
        print("5. Asignar centro de práctica")
        print("6. Volver al menú principal")

        opcionSeleccionada = input("Elegir opción: ").strip()

        # Opción 1: Registrar un estudiante practicante y guardarlo
        if opcionSeleccionada == "1":
            print("\n[Registrar Practicante]")
            cedulaPracticante = input("Cédula: ").strip()
            nombrePracticante = input("Nombre: ").strip()
            mailPracticante = input("Mail: ").strip()
            contactoPracticante = input("Contacto opcional: ").strip()
            gradoPracticante = input("Grado: ").strip()
            estadoPracticante = input("Estado (Habilitado / En suspenso): ").strip()

            nuevoPracticante = Practicante(cedulaPracticante, nombrePracticante, mailPracticante, contactoPracticante, gradoPracticante)
            nuevoPracticante.estado = estadoPracticante
            listaPracticantes.append(nuevoPracticante)

            # Guardamos la lista completa actualizada en el archivo
            try:
                archivoPracticantes = open("persistencia/practicantes.txt", "w")
                for p in listaPracticantes:
                    archivoPracticantes.write(p.cedula + ", " + p.nombre + ", " + p.mail + ", " + p.contacto + ", " + p.grado + ", " + p.estado + "\n")
                archivoPracticantes.close()
            except Exception as errorArchivo:
                print("Error al guardar practicante:", errorArchivo)

            print("¡Practicante '" + nombrePracticante + "' registrado con éxito!")

        # Opción 2: Modificar practicante y actualizar archivo
        elif opcionSeleccionada == "2":
            print("\n[Modificar Practicante]")
            cedulaBuscada = input("Ingrese la cédula del practicante a modificar: ").strip()
            practicanteEncontrado = False
            for practicanteActual in listaPracticantes:
                if practicanteActual.cedula == cedulaBuscada:
                    nuevoNombre = input("Nuevo nombre [Actual: " + practicanteActual.nombre + "] (enter para omitir): ").strip()
                    nuevoMail = input("Nuevo mail [Actual: " + practicanteActual.mail + "] (enter para omitir): ").strip()
                    nuevoContacto = input("Nuevo contacto [Actual: " + practicanteActual.contacto + "] (enter para omitir): ").strip()
                    nuevoGrado = input("Nuevo grado [Actual: " + practicanteActual.grado + "] (enter para omitir): ").strip()
                    nuevoEstado = input("Nuevo estado [Actual: " + practicanteActual.estado + "] (Habilitado / En suspenso) (enter para omitir): ").strip()

                    if nuevoNombre: practicanteActual.nombre = nuevoNombre
                    if nuevoMail: practicanteActual.mail = nuevoMail
                    if nuevoContacto: practicanteActual.contacto = nuevoContacto
                    if nuevoGrado: practicanteActual.grado = nuevoGrado
                    if nuevoEstado: practicanteActual.estado = nuevoEstado

                    # Guardamos los cambios actualizados en el archivo
                    try:
                        archivoPracticantes = open("persistencia/practicantes.txt", "w")
                        for p in listaPracticantes:
                            archivoPracticantes.write(p.cedula + ", " + p.nombre + ", " + p.mail + ", " + p.contacto + ", " + p.grado + ", " + p.estado + "\n")
                        archivoPracticantes.close()
                    except Exception as errorArchivo:
                        print("Error al actualizar el archivo:", errorArchivo)

                    print("¡Practicante modificado y guardado con éxito!")
                    practicanteEncontrado = True
                    break
            if not practicanteEncontrado:
                print("No se encontró un practicante con esa cédula.")

        # Opción 3: Borrar practicante de forma sencilla y actualizar el archivo
        elif opcionSeleccionada == "3":
            print("\n[Borrar Practicante]")
            cedulaBuscada = input("Ingrese la cédula del practicante a borrar: ").strip()

            for practicanteActual in listaPracticantes:
                if practicanteActual.cedula == cedulaBuscada:
                    try:
                        if practicanteActual.centroObjeto:
                            practicanteActual.centroObjeto.cuposDisponibles += 1
                    except AttributeError:
                        pass

            largoInicialPracticantes = len(listaPracticantes)
            listaPracticantes[:] = [practicanteActual for practicanteActual in listaPracticantes if practicanteActual.cedula != cedulaBuscada]

            if len(listaPracticantes) < largoInicialPracticantes:
                # Sobrescribimos el archivo con los practicantes restantes
                try:
                    archivoPracticantes = open("persistencia/practicantes.txt", "w")
                    for practicanteActual in listaPracticantes:
                        archivoPracticantes.write(
                            practicanteActual.cedula + ", " +
                            practicanteActual.nombre + ", " +
                            practicanteActual.mail + ", " +
                            practicanteActual.contacto + ", " +
                            practicanteActual.grado + ", " +
                            practicanteActual.estado + "\n"
                        )
                    archivoPracticantes.close()
                except Exception as errorArchivo:
                    print("Error al actualizar el archivo:", errorArchivo)

                print("¡Practicante borrado con éxito y archivo actualizado!")
            else:
                print("No se encontró esa cédula.")

        # Opción 4: Listar todos los practicantes con su estado y promedio
        elif opcionSeleccionada == "4":
            print("\n--- LISTA DE PRACTICANTES Y ESTADOS ---")
            if not listaPracticantes:
                print("No hay practicantes registrados.")
            else:
                for practicanteActual in listaPracticantes:
                    promedioActual = calcularPromedioPracticante(practicanteActual, listaVisitas)
                    print("Cédula: " + str(practicanteActual.cedula) + " | Nombre: " + str(practicanteActual.nombre) + " | Grado: " + str(practicanteActual.grado) + " | Estado: " + str(practicanteActual.estado) + " | Promedio: " + str(promedioActual))

        # Opción 5: Asignarle un centro de práctica a un estudiante
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
                    print("\nPracticante: " + practicanteEncontrado.nombre)
                    print("\nCentros disponibles:")
                    for indiceCentro, centroActual in enumerate(listaCentros):
                        print(str(indiceCentro + 1) + ". " + str(centroActual.nombre) + " (Disponibles: " + str(centroActual.cuposDisponibles) + ")")

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

                            diasInput = input("\nDías de práctica [Sugerido: " + diasSugeridos + "] (Enter para aceptar): ").strip()
                            diasAsignados = diasInput if diasInput else diasSugeridos

                            horarioInput = input("Horario [Sugerido: " + horarioSugerido + "] (Enter para aceptar): ").strip()
                            horarioAsignado = horarioInput if horarioInput else horarioSugerido

                            # Descontamos un cupo del centro seleccionado
                            centroElegido.cuposDisponibles -= 1

                            practicanteEncontrado.centroAsignado = centroElegido.nombre
                            practicanteEncontrado.adscriptorAsignado = nombreAdscriptorTxt
                            practicanteEncontrado.diasPractica = diasAsignados
                            practicanteEncontrado.horarioPractica = horarioAsignado
                            practicanteEncontrado.centroObjeto = centroElegido

                            print("¡Asignación exitosa! Quedan " + str(centroElegido.cuposDisponibles) + " cupos.")
                        else:
                            print("Número inválido.")
                    except ValueError:
                        print("Por favor, ingrese un número válido.")

        elif opcionSeleccionada == "6":
            break
        else:
            print("Opción no válida.")

# ==========================================
# MENÚ: Manejar docentes, visitas de didáctica y tribunales
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

        # Opción 1: Registrar un docente de didáctica nuevo y guardarlo
        if opcionSeleccionada == "1":
            print("\n[Registrar Docente]")
            cedulaDocente = input("Cédula: ").strip()
            nombreDocente = input("Nombre: ").strip()
            mailDocente = input("Mail: ").strip()
            contactoDocente = input("Contacto opcional: ").strip()
            asignaturaDocente = input("Asignatura / Cargo: ").strip()

            nuevoDocente = DocenteDidactica(cedulaDocente, nombreDocente, mailDocente, contactoDocente, asignaturaDocente)
            listaDocentes.append(nuevoDocente)

            # Guardamos la lista completa actualizada en el archivo
            try:
                archivoDocentes = open("persistencia/docentes_didactica.txt", "w")
                for d in listaDocentes:
                    archivoDocentes.write(d.cedula + ", " + d.nombre + ", " + d.asignatura + "\n")
                archivoDocentes.close()
            except Exception as errorArchivo:
                print("Error al guardar docente:", errorArchivo)

            print("¡Docente '" + nombreDocente + "' registrado y guardado con éxito!")

        # Opción 2: Modificar datos de un docente y actualizar archivo
        elif opcionSeleccionada == "2":
            print("\n[Modificar Docente]")
            cedulaBuscada = input("Ingrese la cédula del docente a modificar: ").strip()
            docenteEncontrado = False
            for docenteActual in listaDocentes:
                if docenteActual.cedula == cedulaBuscada:
                    nuevoNombre = input("Nuevo nombre [Actual: " + docenteActual.nombre + "] (enter para omitir): ").strip()
                    nuevoMail = input("Nuevo mail [Actual: " + docenteActual.mail + "] (enter para omitir): ").strip()
                    nuevoContacto = input("Nuevo contacto [Actual: " + docenteActual.contacto + "] (enter para omitir): ").strip()
                    nuevaAsignatura = input("Nuevo cargo/asignatura [Actual: " + docenteActual.asignatura + "] (enter para omitir): ").strip()

                    if nuevoNombre: docenteActual.nombre = nuevoNombre
                    if nuevoMail: docenteActual.mail = nuevoMail
                    if nuevoContacto: docenteActual.contacto = nuevoContacto
                    if nuevaAsignatura: docenteActual.asignatura = nuevaAsignatura

                    # Guardamos los cambios actualizados en el archivo
                    try:
                        archivoDocentes = open("persistencia/docentes_didactica.txt", "w")
                        for d in listaDocentes:
                            archivoDocentes.write(d.cedula + ", " + d.nombre + ", " + d.asignatura + "\n")
                        archivoDocentes.close()
                    except Exception as errorArchivo:
                        print("Error al actualizar el archivo:", errorArchivo)

                    print("¡Docente modificado y guardado con éxito!")
                    docenteEncontrado = True
                    break
            if not docenteEncontrado:
                print("No se encontró un docente con esa cédula.")

        # Opción 3: Listar docentes
        elif opcionSeleccionada == "3":
            print("\n--- LISTA DE DOCENTES ---")
            if not listaDocentes:
                print("No hay docentes registrados.")
            else:
                for docenteActual in listaDocentes:
                    print("Cédula: " + str(docenteActual.cedula) + " | Nombre: " + str(docenteActual.nombre) + " | Cargo: " + str(docenteActual.asignatura))

        # Opción 4: Registrar una visita escolar/didáctica a un estudiante
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
                    archivoVisitas = open("persistencia/visitas.txt", "a")
                    archivoVisitas.write(docenteEncontrado.cedula + ", " + practicanteEncontrado.cedula + ", " + fechaVisita + ", " + calificacionVisita + ", " + observacionesVisita + "\n")
                    archivoVisitas.close()
                except Exception as errorArchivo:
                    print("Error al guardar visita:", errorArchivo)

                promedioActual = calcularPromedioPracticante(practicanteEncontrado, listaVisitas)
                print("\n¡Visita registrada con éxito!")
                print("   Promedio actual del practicante: " + str(promedioActual))

        # Opción 5: Ver el promedio final de las visitas de un practicante específico
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
                    print("\n--- INFORME FINAL DE VISITAS ---")
                    print("Practicante: " + practicanteBuscado.nombre)
                    print("Cédula: " + practicanteBuscado.cedula)
                    print("Promedio final de notas: " + str(promedioFinal))

        # Opción 6: Ver la lista completa de todas las visitas hechas
        elif opcionSeleccionada == "6":
            print("\n--- LISTA DE VISITAS REGISTRADAS ---")
            if not listaVisitas:
                print("Aún no hay visitas registradas.")
            else:
                for visitaActual in listaVisitas:
                    print(str(visitaActual))

        # Opción 7: Armar el tribunal examinador final para un alumno
        elif opcionSeleccionada == "7":
            print("\n[Gestión de Tribunal Final]")
            if not listaPracticantes:
                print("No hay practicantes registrados.")
            elif len(listaDocentes) < 1 and len(listaAdscriptores) < 1:
                print("Se necesitan docentes o adscriptores registrados.")
            else:
                print("\nPracticantes:")
                for practicanteActual in listaPracticantes:
                    print("- Cédula: " + str(practicanteActual.cedula) + " | Nombre: " + str(practicanteActual.nombre))

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
                print("3. No agregar tercer miembro (Dejar solo 2)")
                opcionTercero = input("Elija opción: ").strip()

                if opcionTercero == "1":
                    tercerMiembro = buscarMiembroTribunal("Cédula del 3er Miembro: ")
                elif opcionTercero == "2":
                    cedulaNuevoDocente = input("Cédula: ").strip()
                    nombreNuevoDocente = input("Nombre: ").strip()
                    cargoNuevoDocente = input("Cargo o Asignatura: ").strip()
                    tercerMiembro = DocenteDidactica(cedulaNuevoDocente, nombreNuevoDocente, "N/D", "N/D", cargoNuevoDocente)
                    listaDocentes.append(tercerMiembro)

                    try:
                        archivoDocentes = open("persistencia/docentes_didactica.txt", "w")
                        for d in listaDocentes:
                            archivoDocentes.write(d.cedula + ", " + d.nombre + ", " + d.asignatura + "\n")
                        archivoDocentes.close()
                    except Exception as errorArchivo:
                        print("Aviso al guardar en archivo:", errorArchivo)
                else:
                    tercerMiembro = None

                nuevoTribunal = TribunalFinal(practicanteElegido, primerMiembro, segundoMiembro, tercerMiembro)
                print("\n¡Tribunal asignado con éxito!")
                print(str(nuevoTribunal))

        elif opcionSeleccionada == "8":
            break
        else:
            print("Opción no válida.")

# ==========================================
# FUNCIÓN PRINCIPAL: Arranque del sistema completo
# ==========================================
def main():
    abbCentros = ABBCentros()
    listaCentros = []
    listaAdscriptores = []
    listaPracticantes = []
    listaDocentes = []
    listaVisitas = []

    # 1. Carga automática de Centros desde el archivo
    try:
        archivoCentros = open("persistencia/centros.txt", "r")
        for lineaActual in archivoCentros:
            partesLinea = [parte.strip() for parte in lineaActual.strip().split(",")]
            if len(partesLinea) >= 4:
                centroActual = CentroEducativo(partesLinea[0], partesLinea[1], partesLinea[2], int(partesLinea[3]))
                centroActual.cuposDisponibles = centroActual.cuposTotales
                abbCentros.insertar(centroActual)
                listaCentros.append(centroActual)
        archivoCentros.close()
    except FileNotFoundError:
        pass

    # 2. Carga automática de Adscriptores desde el archivo
    try:
        archivoAdscriptores = open("persistencia/adscriptores.txt", "r")
        for lineaActual in archivoAdscriptores:
            partesLinea = [parte.strip() for parte in lineaActual.strip().split(",")]
            if len(partesLinea) >= 9:
                nuevoAdscriptor = Adscriptor(
                    cedula=partesLinea[0], nombre=partesLinea[1], mail=partesLinea[2],
                    contacto=partesLinea[3], centroPractica=partesLinea[8],
                    grado=partesLinea[4], dias=partesLinea[6], horario=partesLinea[7]
                )
                listaAdscriptores.append(nuevoAdscriptor)
        archivoAdscriptores.close()
    except FileNotFoundError:
        pass

    # 3. Carga automática de Practicantes desde el archivo
    try:
        archivoPracticantes = open("persistencia/practicantes.txt", "r")
        for lineaActual in archivoPracticantes:
            partesLinea = [parte.strip() for parte in lineaActual.strip().split(",")]
            if len(partesLinea) >= 6:
                nuevoPracticante = Practicante(partesLinea[0], partesLinea[1], partesLinea[2], partesLinea[3], partesLinea[4])
                nuevoPracticante.estado = partesLinea[5]
                listaPracticantes.append(nuevoPracticante)
            elif len(partesLinea) == 5:
                nuevoPracticante = Practicante(partesLinea[0], partesLinea[1], partesLinea[2], partesLinea[3], partesLinea[4])
                nuevoPracticante.estado = "No especificado"
                listaPracticantes.append(nuevoPracticante)
        archivoPracticantes.close()
    except FileNotFoundError:
        pass

    # 4. Carga automática de Docentes de Didáctica desde el archivo
    try:
        archivoDocentes = open("persistencia/docentes_didactica.txt", "r")
        for lineaActual in archivoDocentes:
            partesLinea = [parte.strip() for parte in lineaActual.strip().split(",")]
            if len(partesLinea) >= 3:
                nuevoDocente = DocenteDidactica(
                    cedula=partesLinea[0], nombre=partesLinea[1],
                    mail="N/D", contacto="N/D", asignatura=partesLinea[2]
                )
                listaDocentes.append(nuevoDocente)
        archivoDocentes.close()
    except FileNotFoundError:
        pass

    # 5. Carga automática de Visitas desde el archivo
    try:
        archivoVisitas = open("persistencia/visitas.txt", "r")
        for lineaActual in archivoVisitas:
            partesLinea = [parte.strip() for parte in lineaActual.strip().split(",")]
            if len(partesLinea) >= 5:
                cedDoc = partesLinea[0]
                cedPrac = partesLinea[1]
                fechaVis = partesLinea[2]
                califVis = partesLinea[3]
                obsVis = partesLinea[4]

                docenteObj = None
                for d in listaDocentes:
                    if d.cedula.strip() == cedDoc:
                        docenteObj = d
                        break

                practicanteObj = None
                for p in listaPracticantes:
                    if p.cedula.strip() == cedPrac:
                        practicanteObj = p
                        break

                if docenteObj and practicanteObj:
                    nuevaVisita = VisitaDidactica(docenteObj, practicanteObj, fechaVis, califVis, obsVis)
                    listaVisitas.append(nuevaVisita)
        archivoVisitas.close()
    except FileNotFoundError:
        pass

    # Bucle principal que muestra el menú de opciones del sistema en la consola
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