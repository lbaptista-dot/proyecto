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
# MENÚ: Administrar los centros de práctica educativa (Actualizado con ID y Persistencia)
# ==========================================
def menuCentrosPracticas(abbCentros, listaCentros):
    while True:
        print("\n--- MENÚ CENTROS DE PRÁCTICA ---")
        print("1. Registrar centro")
        print("2. Modificar centro")
        print("3. Borrar centro")
        print("4. Listar centros")
        print("5. Buscar centro por Nombre") # <--- NUEVA OPCIÓN
        print("6. Volver al menú principal")


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


            # Guardamos la lista completa actualizada en el archivo
            try:
                archivoCentros = open("persistencia/centros.txt", "w")
                for centroActual in listaCentros:
                    archivoCentros.write(str(centroActual.idCentro) + ", " + str(centroActual.nombre) + ", " + str(centroActual.localidad) + ", " + str(centroActual.cuposTotales) + "\n")
                archivoCentros.close()
            except Exception as errorArchivo:
                print("Error al guardar en el archivo de centros:", errorArchivo)


            print("¡Centro '" + nombreCentro + "' registrado con éxito!")


        # Opción 2: Modificar los datos de un centro existente buscando por ID
        elif opcionSeleccionada == "2":
            print("\n[Modificar Centro]")
            idBuscado = input("Ingrese el ID del centro a modificar: ").strip()


            centroEncontrado = None
            for centroActual in listaCentros:
                if str(centroActual.idCentro).strip() == idBuscado:
                    centroEncontrado = centroActual
                    break


            if centroEncontrado:
                print("Centro encontrado: " + centroEncontrado.nombre)
                nuevoNombre = input("Nuevo nombre [Actual: " + centroEncontrado.nombre + "] (enter para omitir): ").strip()
                nuevaLocalidad = input("Nueva localidad [Actual: " + centroEncontrado.localidad + "] (enter para omitir): ").strip()
                nuevosCupos = input("Nuevos cupos totales [Actual: " + str(centroEncontrado.cuposTotales) + "] (enter para omitir): ").strip()


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
                print("No se encontró ningún centro con ese ID.")


        # Opción 3: Eliminar un centro del sistema buscando por ID
        elif opcionSeleccionada == "3":
            print("\n[Borrar Centro]")
            idBuscado = input("Ingrese el ID del centro a borrar: ").strip()
            largoInicialCentros = len(listaCentros)


            # Filtramos la lista para sacar al centro que coincida con el ID
            listaCentros[:] = [centroActual for centroActual in listaCentros if str(centroActual.idCentro).strip() != idBuscado]


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
                print("No se encontró ningún centro con ese ID.")


        # Opción 4: Mostrar todos los centros que están registrados
        elif opcionSeleccionada == "4":
            print("\n--- LISTA DE CENTROS ---")
            if not listaCentros:
                print("Todavía no hay centros registrados.")
            else:
                for centroActual in listaCentros:
                    print("ID: " + str(centroActual.idCentro) + " | " + str(centroActual) + " | Disponibles: " + str(centroActual.cuposDisponibles) + "/" + str(centroActual.cuposTotales))


        # Opción 5: Buscar centro por Nombre o Localidad usando el ABB
        elif opcionSeleccionada == "5":
            print("\n[Búsqueda de Centros por Nombre o Localidad]")
            textoBuscado = input("Ingrese el nombre o localidad a buscar: ").strip()


            # Recibimos la lista de centros que devuelve el ABB
            listaResultados = abbCentros.buscarPorNombreOLocalidad(textoBuscado)


            if not listaResultados:
                print("No se encontró ningún centro con ese nombre.")
            else:
                print(f"\n¡Se encontraron {len(listaResultados)} centro(s)")
                for centroActual in listaResultados:
                    print("ID: " + str(centroActual.idCentro) + " | Nombre: " + str(centroActual.nombre) + " | Localidad: " + str(centroActual.localidad) + " | Cupos: " + str(centroActual.cuposDisponibles) + "/" + str(centroActual.cuposTotales))


        elif opcionSeleccionada == "6":
            break


        # Opción 6: Salir de este menú y volver al anterior
        elif opcionSeleccionada == "6":
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


        # Opción 1: Registrar un nuevo adscriptor
        if opcionSeleccionada == "1":
            print("\n[Registrar Adscriptor]")
            cedulaAdscriptor = input("Cédula: ").strip()
            nombreAdscriptor = input("Nombre: ").strip()
            mailAdscriptor = input("Mail: ").strip()
            contactoAdscriptor = input("Contacto opcional: ").strip()
            centroPracticaAdscriptor = input("Centro de práctica asignado: ").strip()


            listaGruposObj = []
            while True:
                nombreGrupo = input("Nombre del grupo (ej: 1°1): ").strip()
                diasGrupo = input("Días disponibles (ej: Lunes): ").strip()
                horarioGrupo = input("Horario disponible (ej: 8:00): ").strip()


                listaGruposObj.append({
                    'grupo': nombreGrupo,
                    'dias': diasGrupo,
                    'horario': horarioGrupo
                })


                otro = input("¿Desea agregar otro grupo para este adscriptor? (s/n): ").strip().lower()
                if otro != 's':
                    break


            nuevoAdscriptor = Adscriptor(cedulaAdscriptor, nombreAdscriptor, mailAdscriptor, contactoAdscriptor, centroPracticaAdscriptor, listaGruposObj)
            listaAdscriptores.append(nuevoAdscriptor)


            try:
                archivoAdscriptores = open("persistencia/adscriptores.txt", "a")
                str_grupos = "; ".join([f"{g['grupo']}|{g['dias']}|{g['horario']}" for g in listaGruposObj])
                archivoAdscriptores.write(cedulaAdscriptor + ", " + nombreAdscriptor + ", " + mailAdscriptor + ", " + contactoAdscriptor + ", " + centroPracticaAdscriptor + ", " + str_grupos + "\n")
                archivoAdscriptores.close()
            except Exception as errorArchivo:
                print("Error al guardar adscriptor:", errorArchivo)


            print("¡Adscriptor '" + nombreAdscriptor + "' registrado con éxito!")


        # Opción 2: Modificar adscriptor buscando por cédula
        elif opcionSeleccionada == "2":
            print("\n[Modificar Adscriptor]")
            cedulaBuscada = input("Ingrese la cédula del adscriptor a modificar: ").strip()
            adscriptorEncontrado = None


            for adscriptorActual in listaAdscriptores:
                if adscriptorActual.cedula == cedulaBuscada:
                    adscriptorEncontrado = adscriptorActual
                    break


            if adscriptorEncontrado:
                print(f"Adscriptor encontrado: {adscriptorEncontrado.nombre}")


                # Pedimos los nuevos datos (si presiona Enter sin escribir nada, conserva el valor anterior)
                nuevaCedula = input(f"Nueva cédula [Actual: {adscriptorEncontrado.cedula}](enter para omitir): ").strip()
                nuevoNombre = input(f"Nuevo nombre [Actual: {adscriptorEncontrado.nombre}](enter para omitir): ").strip()
                nuevoMail = input(f"Nuevo mail [Actual: {adscriptorEncontrado.mail}](enter para omitir): ").strip()
                nuevoContacto = input(f"Nuevo contacto [Actual: {adscriptorEncontrado.contacto}](enter para omitir): ").strip()
                nuevoCentro = input(f"Nuevo centro de práctica [Actual: {adscriptorEncontrado.centroPractica}](enter para omitir): ").strip()


                if nuevaCedula: adscriptorEncontrado.cedula = nuevaCedula
                if nuevoNombre: adscriptorEncontrado.nombre = nuevoNombre
                if nuevoMail: adscriptorEncontrado.mail = nuevoMail
                if nuevoContacto: adscriptorEncontrado.contacto = nuevoContacto
                if nuevoCentro: adscriptorEncontrado.centroPractica = nuevoCentro


                # Preguntamos si desea modificar los grupos
                modificarGrupos = input("¿Desea modificar los grupos y horarios? (s/n): ").strip().lower()
                if modificarGrupos == 's':
                    listaGruposObj = []
                    while True:
                        nombreGrupo = input("Nombre del grupo (ej: 7°1): ").strip()
                        diasGrupo = input("Días disponibles (ej: Lunes y Jueves): ").strip()
                        horarioGrupo = input("Horario disponible (ej: 8:10 a 9:45 y 11:05 a 13:00): ").strip()


                        listaGruposObj.append({
                            'grupo': nombreGrupo,
                            'dias': diasGrupo,
                            'horario': horarioGrupo
                        })


                        otro = input("¿Desea agregar otro grupo? (s/n): ").strip().lower()
                        if otro != 's':
                            break
                    adscriptorEncontrado.grupos = listaGruposObj


                # Sobrescribimos todo el archivo `adscriptores.txt` con la lista actualizada y limpia
                try:
                    archivoAdscriptores = open("persistencia/adscriptores.txt", "w")
                    for a in listaAdscriptores:
                        # Aseguramos que tenga grupos para evitar errores
                        grupos_a_guardar = getattr(a, 'grupos', [])
                        str_grupos = "; ".join([f"{g['grupo']}|{g['dias']}|{g['horario']}" for g in grupos_a_guardar])


                        linea_archivo = f"{a.cedula}, {a.nombre}, {a.mail}, {a.contacto}, {a.centroPractica}, {str_grupos}\n"
                        archivoAdscriptores.write(linea_archivo)
                    archivoAdscriptores.close()
                except Exception as errorArchivo:
                    print("Error al actualizar el archivo de adscriptores:", errorArchivo)


                print("¡Adscriptor modificado y guardado con éxito!")
            else:
                print("No se encontró un adscriptor con esa cédula.")


        # Opción 3: Borrar un adscriptor
        elif opcionSeleccionada == "3":
            print("\n--- Borrar Adscriptor ---")
            cedulaBuscada = input("Ingrese la cédula del adscriptor a borrar: ").strip()
            largoInicialAdscriptores = len(listaAdscriptores)


            # Filtramos la lista para sacar al adscriptor que coincida con la cédula
            listaAdscriptores[:] = [adscriptorActual for adscriptorActual in listaAdscriptores if str(adscriptorActual.cedula).strip() != cedulaBuscada]


            if len(listaAdscriptores) < largoInicialAdscriptores:
                # Sobrescribimos el archivo de texto con la lista actualizada
                try:
                    archivoAdscriptores = open("persistencia/adscriptores.txt", "w")
                    for a in listaAdscriptores:
                        grupos_a_guardar = getattr(a, 'grupos', [])
                        str_grupos = "; ".join([f"{g['grupo']}|{g['dias']}|{g['horario']}" for g in grupos_a_guardar])


                        linea_archivo = f"{a.cedula}, {a.nombre}, {a.mail}, {a.contacto}, {a.centroPractica}, {str_grupos}\n"
                        archivoAdscriptores.write(linea_archivo)
                    archivoAdscriptores.close()
                except Exception as errorArchivo:
                    print("Error al actualizar el archivo de adscriptores:", errorArchivo)


                print("¡Adscriptor borrado y archivo actualizado con éxito!")
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
        print("6. Ver expediente / Historial académico completo")
        print("7. Volver al menú principal")


        opcionSeleccionada = input("Elegir opción: ").strip()


        # Opción 1: Registrar un estudiante practicante
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


            try:
                archivoPracticantes = open("persistencia/practicantes.txt", "a")
                archivoPracticantes.write(cedulaPracticante + ", " + nombrePracticante + ", " + mailPracticante + ", " + contactoPracticante + ", " + gradoPracticante + ", " + estadoPracticante + "\n")
                archivoPracticantes.close()
            except Exception as errorArchivo:
                print("Error al guardar practicante:", errorArchivo)


            print("¡Practicante '" + nombrePracticante + "' registrado!")


        # Opción 2: Modificar practicante
        elif opcionSeleccionada == "2":
            print("\n[Modificar Practicante]")
            cedulaBuscada = input("Ingrese la cédula del practicante a modificar: ").strip()
            practicanteEncontrado = None
            for practicanteActual in listaPracticantes:
                if str(practicanteActual.cedula).strip() == cedulaBuscada:
                    practicanteEncontrado = practicanteActual
                    break


            if practicanteEncontrado:
                print(f"Practicante encontrado: {practicanteEncontrado.nombre}")
                nuevaCedula = input(f"Nueva cédula [Actual: {practicanteEncontrado.cedula}]: ").strip()
                nuevoNombre = input(f"Nuevo nombre [Actual: {practicanteEncontrado.nombre}]: ").strip()
                nuevoMail = input(f"Nuevo mail [Actual: {practicanteEncontrado.mail}]: ").strip()
                nuevoContacto = input(f"Nuevo contacto [Actual: {practicanteEncontrado.contacto}]: ").strip()
                nuevoGrado = input(f"Nuevo grado [Actual: {practicanteEncontrado.grado}]: ").strip()


                estadoActualTxt = practicanteEncontrado.estado if hasattr(practicanteEncontrado, 'estado') else 'Habilitado'
                nuevoEstado = input(f"Nuevo estado [Actual: {estadoActualTxt}] (Habilitado / En suspenso): ").strip()


                if nuevaCedula: practicanteEncontrado.cedula = nuevaCedula
                if nuevoNombre: practicanteEncontrado.nombre = nuevoNombre
                if nuevoMail: practicanteEncontrado.mail = nuevoMail
                if nuevoContacto: practicanteEncontrado.contacto = nuevoContacto
                if nuevoGrado: practicanteEncontrado.grado = nuevoGrado
                if nuevoEstado: practicanteEncontrado.estado = nuevoEstado


                # Sobrescribimos el archivo de practicantes con la lista actualizada
                try:
                    archivoPracticantes = open("persistencia/practicantes.txt", "w")
                    for p in listaPracticantes:
                        est = p.estado if hasattr(p, 'estado') else 'Habilitado'
                        archivoPracticantes.write(f"{p.cedula}, {p.nombre}, {p.mail}, {p.contacto}, {p.grado}, {est}\n")
                    archivoPracticantes.close()
                except Exception as errorArchivo:
                    print("Error al actualizar el archivo de practicantes:", errorArchivo)


                print("¡Practicante modificado y guardado con éxito!")
            else:
                print("No se encontró un practicante con esa cédula.")


        # Opción 3: Borrar practicante y actualizar archivo y cupos
        elif opcionSeleccionada == "3":
            print("\n[Borrar Practicante]")
            cedulaBuscada = input("Ingrese la cédula del practicante a borrar: ").strip()


            for practicanteActual in listaPracticantes:
                if str(practicanteActual.cedula).strip() == cedulaBuscada and hasattr(practicanteActual, 'centroObjeto') and practicanteActual.centroObjeto:
                    practicanteActual.centroObjeto.cuposDisponibles += 1


            largoInicialPracticantes = len(listaPracticantes)
            listaPracticantes[:] = [practicanteActual for practicanteActual in listaPracticantes if str(practicanteActual.cedula).strip() != cedulaBuscada]


            if len(listaPracticantes) < largoInicialPracticantes:
                # Sobrescribimos el archivo de practicantes eliminando al usuario
                try:
                    archivoPracticantes = open("persistencia/practicantes.txt", "w")
                    for p in listaPracticantes:
                        est = p.estado if hasattr(p, 'estado') else 'Habilitado'
                        archivoPracticantes.write(f"{p.cedula}, {p.nombre}, {p.mail}, {p.contacto}, {p.grado}, {est}\n")
                    archivoPracticantes.close()
                except Exception as errorArchivo:
                    print("Error al actualizar el archivo de practicantes:", errorArchivo)


                print("¡Practicante borrado del sistema y del archivo con éxito!")
            else:
                print("No se encontró esa cédula.")


        # Opción 4: Mostrar la lista de todos los practicantes con sus datos, estado y asignaciones
        elif opcionSeleccionada == "4":
            print("\n--- LISTA DE PRACTICANTES Y ASIGNACIONES ---")


            if not listaPracticantes:
                print("No hay practicantes registrados.")
            else:
                for practicanteActual in listaPracticantes:
                    promedioActual = calcularPromedioPracticante(practicanteActual, listaVisitas)


                    estadoActual = practicanteActual.estado if hasattr(practicanteActual, 'estado') else "No especificado"
                    centroAsignado = practicanteActual.centroAsignado if hasattr(practicanteActual, 'centroAsignado') else "Sin asignar"
                    adscriptorAsignado = practicanteActual.adscriptorAsignado if hasattr(practicanteActual, 'adscriptorAsignado') else "Sin adscriptor"
                    diasPractica = practicanteActual.diasPractica if hasattr(practicanteActual, 'diasPractica') else "N/D"
                    horarioPractica = practicanteActual.horarioPractica if hasattr(practicanteActual, 'horarioPractica') else "N/D"


                    print("• Cédula: " + str(practicanteActual.cedula) + " | Nombre: " + str(practicanteActual.nombre) + " | Grado: " + str(practicanteActual.grado) + " | Estado: " + str(estadoActual))
                    print("  Centro: " + str(centroAsignado) + " | Adscriptor: " + str(adscriptorAsignado) + " | Días: " + str(diasPractica) + " | Horario: " + str(horarioPractica) + " | Promedio: " + str(promedioActual))
                    print("-" * 80)


        # Opción 5: Asignarle un centro, adscriptor y grupo de práctica al estudiante de forma interactiva
        elif opcionSeleccionada == "5":
            print("\n[Asignación de Práctica]")
            cedulaBuscada = input("Ingrese la cédula del practicante: ").strip()


            practicanteEncontrado = None
            for practicanteActual in listaPracticantes:
                if str(practicanteActual.cedula).strip() == cedulaBuscada:
                    practicanteEncontrado = practicanteActual
                    break


            if not practicanteEncontrado:
                print("No se encontró un practicante con esa cédula.")
            else:
                if not listaCentros:
                    print("No hay centros educativos registrados.")
                else:
                    print("\nPracticante: " + practicanteEncontrado.nombre)
                    print("\n--- CENTROS EDUCATIVOS DISPONIBLES ---")


                    for indiceCentro, centroActual in enumerate(listaCentros):
                        print(str(indiceCentro + 1) + ". " + str(centroActual.nombre) + " (Cupos disponibles: " + str(centroActual.cuposDisponibles) + ")")


                    try:
                        seleccionCentro = int(input("Seleccione el número del centro: ")) - 1


                        if 0 <= seleccionCentro < len(listaCentros):
                            centroElegido = listaCentros[seleccionCentro]


                            if centroElegido.cuposDisponibles <= 0:
                                print("¡Error! Este centro ya no tiene cupos disponibles.")
                                continue


                            adscriptorEncontrado = None
                            for adscriptorActual in listaAdscriptores:
                                if adscriptorActual.centroPractica.strip().lower() == centroElegido.nombre.strip().lower():
                                    adscriptorEncontrado = adscriptorActual
                                    break


                            if adscriptorEncontrado and adscriptorEncontrado.grupos:
                                nombreAdscriptorTxt = adscriptorEncontrado.nombre
                                print("\n--- GRUPOS Y HORARIOS DEL ADSCRIPTOR: " + nombreAdscriptorTxt + " ---")


                                for indiceGrupo, infoGrupo in enumerate(adscriptorEncontrado.grupos):
                                    print(str(indiceGrupo + 1) + ". Grupo: " + str(infoGrupo['grupo']) + " | Días: " + str(infoGrupo['dias']) + " | Horario: " + str(infoGrupo['horario']))


                                try:
                                    seleccionGrupo = int(input("Seleccione el número del grupo de práctica: ")) - 1
                                    if 0 <= seleccionGrupo < len(adscriptorEncontrado.grupos):
                                        grupoSeleccionado = adscriptorEncontrado.grupos[seleccionGrupo]
                                        diasAsignados = grupoSeleccionado['dias']
                                        horarioAsignado = grupoSeleccionado['horario']
                                        nombreGrupoAsignado = grupoSeleccionado['grupo']
                                    else:
                                        print("Selección de grupo inválida. Se asignará por defecto.")
                                        diasAsignados = "A definir"
                                        horarioAsignado = "A definir"
                                        nombreGrupoAsignado = "General"
                                except ValueError:
                                    diasAsignados = "A definir"
                                    horarioAsignado = "A definir"
                                    nombreGrupoAsignado = "General"
                            else:
                                nombreAdscriptorTxt = "Sin adscriptor"
                                nombreGrupoAsignado = "General"
                                diasAsignados = input("Ingrese los días de práctica: ").strip()
                                horarioAsignado = input("Ingrese el horario asignado: ").strip()


                            centroElegido.cuposDisponibles -= 1


                            practicanteEncontrado.centroAsignado = centroElegido.nombre
                            practicanteEncontrado.adscriptorAsignado = nombreAdscriptorTxt
                            practicanteEncontrado.grupoPractica = nombreGrupoAsignado
                            practicanteEncontrado.diasPractica = diasAsignados
                            practicanteEncontrado.horarioPractica = horarioAsignado
                            practicanteEncontrado.centroObjeto = centroElegido


                            # Actualizamos practicantes
                            try:
                                archivoPracticantes = open("persistencia/practicantes.txt", "w")
                                for p in listaPracticantes:
                                    est = p.estado if hasattr(p, 'estado') else "Habilitado"
                                    cent = p.centroAsignado if hasattr(p, 'centroAsignado') else "Sin asignar"
                                    adsc = p.adscriptorAsignado if hasattr(p, 'adscriptorAsignado') else "Sin adscriptor"
                                    dias = p.diasPractica if hasattr(p, 'diasPractica') else "N/D"
                                    hor = p.horarioPractica if hasattr(p, 'horarioPractica') else "N/D"


                                    archivoPracticantes.write(str(p.cedula) + ", " + str(p.nombre) + ", " + str(p.mail) + ", " + str(p.contacto) + ", " + str(p.grado) + ", " + str(est) + ", " + str(cent) + ", " + str(adsc) + ", " + str(dias) + ", " + str(hor) + "\n")
                                archivoPracticantes.close()
                            except Exception as errorArchivo:
                                print("Error al guardar la asignación en el archivo de practicantes:", errorArchivo)


                            # Actualizamos centros
                            try:
                                archivoCentros = open("persistencia/centros.txt", "w")
                                for c in listaCentros:
                                    archivoCentros.write(str(c.idCentro) + ", " + str(c.nombre) + ", " + str(c.localidad) + ", " + str(c.cuposDisponibles) + "\n")
                                archivoCentros.close()
                            except Exception as errorArchivo:
                                print("Error al actualizar el archivo de centros:", errorArchivo)


                            print("\n¡Asignación exitosa! Quedan " + str(centroElegido.cuposDisponibles) + " cupos disponibles en el centro.")
                        else:
                            print("El número de centro ingresado no es válido.")
                    except ValueError:
                        print("Por favor, ingrese un número válido.")


        # Opción 6: Ver Expediente o Historial Académico Completo del Practicante
        elif opcionSeleccionada == "6":
            print("\n--- HISTORIAL ACADÉMICO COMPLETO DEL PRACTICANTE ---")
            if not listaPracticantes:
                print("No hay practicantes registrados en el sistema.")
            else:
                cedulaBuscada = input("Ingrese la cédula del practicante a consultar: ").strip()
                practicanteBuscado = None


                for p in listaPracticantes:
                    if str(p.cedula).strip() == cedulaBuscada:
                        practicanteBuscado = p
                        break


                if not practicanteBuscado:
                    print("No se encontró un practicante con esa cédula.")
                else:
                    print("\n" + "="*50)
                    print(f" EXPEDIENTE ACADÉMICO: {practicanteBuscado.nombre}")
                    print("="*50)
                    print(f"• Cédula: {practicanteBuscado.cedula}")


                    mailMostrar = practicanteBuscado.mail if hasattr(practicanteBuscado, 'mail') else "N/D"
                    contactoMostrar = practicanteBuscado.contacto if hasattr(practicanteBuscado, 'contacto') else "N/D"
                    gradoMostrar = practicanteBuscado.grado if hasattr(practicanteBuscado, 'grado') else "N/D"
                    estadoMostrar = practicanteBuscado.estado if hasattr(practicanteBuscado, 'estado') else "Habilitado"


                    print(f"• Mail: {mailMostrar}")
                    print(f"• Contacto: {contactoMostrar}")
                    print(f"• Grado: {gradoMostrar}")
                    print(f"• Estado: {estadoMostrar}")


                    centroAsignado = practicanteBuscado.centroAsignado if hasattr(practicanteBuscado, 'centroAsignado') else "Sin asignar"
                    adscriptorAsignado = practicanteBuscado.adscriptorAsignado if hasattr(practicanteBuscado, 'adscriptorAsignado') else "Sin adscriptor"
                    diasPrac = practicanteBuscado.diasPractica if hasattr(practicanteBuscado, 'diasPractica') else "N/D"
                    horarioPrac = practicanteBuscado.horarioPractica if hasattr(practicanteBuscado, 'horarioPractica') else "N/D"


                    print("\n--- DATOS DE PRÁCTICA ---")
                    print(f"• Centro Educativo: {centroAsignado}")
                    print(f"• Adscriptor: {adscriptorAsignado}")
                    print(f"• Días y Horarios: {diasPrac} ({horarioPrac})")


                    print("\n--- TRIBUNAL EXAMINADOR FINAL ---")
                    tribunalEncontrado = None
                    if 'listaTribunales' in globals() or 'listaTribunales' in locals():
                        for t in listaTribunales:
                            if str(t.practicante.cedula).strip() == str(practicanteBuscado.cedula).strip():
                                tribunalEncontrado = t
                                break

                    if tribunalEncontrado:
                        print(f"• 1er Miembro: {tribunalEncontrado.primerMiembro.nombre} ({tribunalEncontrado.primerMiembro.cedula})")
                        print(f"• 2do Miembro: {tribunalEncontrado.segundoMiembro.nombre} ({tribunalEncontrado.segundoMiembro.cedula})")
                        if tribunalEncontrado.tercerMiembro:
                            print(f"• 3er Miembro: {tribunalEncontrado.tercerMiembro.nombre} ({tribunalEncontrado.tercerMiembro.cedula})")
                        else:
                            print("• 3er Miembro: No asignado (Solo 2 miembros)")
                    else:
                        print("• Este practicante aún no tiene tribunal final asignado.")
                    print("="*50)


        # Opción 7: Volver al menú principal
        elif opcionSeleccionada == "7":
            break
        else:
            print("Opción no válida.")


# ==========================================
# MENÚ: Manejar docentes, visitas de didáctica y tribunales
# ==========================================
def menuDocenteDidactica(listaDocentes, listaAdscriptores, listaPracticantes, listaVisitas, listaTribunales):
    while True:
        print("\n--- MENÚ DOCENTE DIDÁCTICA Y TRIBUNAL ---")
        print("1. Registrar docente")
        print("2. Modificar docente")
        print("3. Listar docentes")
        print("4. Borrar docente")
        print("5. Registrar nueva visita a practicante")
        print("6. Calcular promedio final de visitas de un practicante")
        print("7. Listar todas las visitas realizadas")
        print("8. Armar o actualizar tribunal final")
        print("9. Consultar tribunal de un practicante")
        print("10. Volver al menú principal")


        opcionSeleccionada = input("Elegir opción: ").strip()


        # Opción 1: Registrar un docente de didáctica nuevo
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
                archivoDocentes = open("persistencia/docentes_didactica.txt", "a")
                # Agregamos mail y contacto separados por comas
                archivoDocentes.write(cedulaDocente + ", " + nombreDocente + ", " + mailDocente + ", " + contactoDocente + ", " + asignaturaDocente + "\n")
                archivoDocentes.close()
            except Exception as errorArchivo:
                print("Error al guardar docente:", errorArchivo)


            print("¡Docente '" + nombreDocente + "' registrado y guardado con éxito!")


        # Opción 2: Modificar los datos de un docente existente por su cédula
        elif opcionSeleccionada == "2":
            print("\n[Modificar Docente]")
            cedulaBuscada = input("Ingrese la cédula del docente a modificar: ").strip()
            docenteEncontrado = False


            # Recorremos la lista de docentes para buscar al que coincida con la cédula
            for docenteActual in listaDocentes:
                if str(docenteActual.cedula).strip() == cedulaBuscada:
                    print("Docente encontrado: " + docenteActual.nombre)


                    # Solicitamos los nuevos datos (si presiona Enter sin escribir nada, se omite)
                    nuevoNombre = input("Nuevo nombre [Actual: " + str(docenteActual.nombre) + "] (enter para omitir): ").strip()
                    nuevoMail = input("Nuevo Mail [Actual: " + str(docenteActual.mail) + "] (enter para omitir): ").strip()
                    nuevoContacto = input("Nuevo contacto [Actual: " + str(docenteActual.contacto) + "] (enter para omitir): ").strip()
                    nuevaAsignatura = input("Nueva Asignatura / Cargo [Actual: " + str(docenteActual.asignatura) + "] (enter para omitir): ").strip()


                    # Actualizamos individualmente cada atributo si el usuario ingresó un valor
                    if nuevoNombre:
                        docenteActual.nombre = nuevoNombre
                    if nuevoMail:
                        docenteActual.mail = nuevoMail
                    if nuevoContacto:
                        docenteActual.contacto = nuevoContacto
                    if nuevaAsignatura:
                        docenteActual.asignatura = nuevaAsignatura


                    # Guardamos los cambios actualizando el archivo de texto txt de forma persistente
                    try:
                        archivoDocentes = open("persistencia/docentes_didactica.txt", "w")
                        for d in listaDocentes:
                            archivoDocentes.write(str(d.cedula) + ", " + str(d.nombre) + ", " + str(d.mail) + ", " + str(d.contacto) + ", " + str(d.asignatura) + "\n")
                        archivoDocentes.close()
                    except Exception as errorArchivo:
                        print("Error al actualizar el archivo de docentes:", errorArchivo)


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
        # Opción 4: Borrar un docente de didáctica por su cédula y actualizar el archivo
        elif opcionSeleccionada == "4":
            print("\n[Borrar Docente]")
            cedulaBuscada = input("Ingrese la cédula del docente a borrar: ").strip()


            largoInicialDocentes = len(listaDocentes)


            # Filtramos la lista eliminando al docente que coincida con la cédula
            listaDocentes[:] = [docenteActual for docenteActual in listaDocentes if str(docenteActual.cedula).strip() != cedulaBuscada]


            # Verificamos si realmente se borró alguno
            if len(listaDocentes) < largoInicialDocentes:
                # Sobrescribimos el archivo de texto de docentes de forma persistente
                try:
                    archivoDocentes = open("persistencia/docentes_didactica.txt", "w")
                    for d in listaDocentes:
                        archivoDocentes.write(str(d.cedula) + ", " + str(d.nombre) + ", " + str(d.asignatura) + "\n")
                    archivoDocentes.close()
                except Exception as errorArchivo:
                    print("Error al actualizar el archivo de docentes:", errorArchivo)


                print("¡Docente borrado del sistema y del archivo con éxito!")
            else:
                print("No se encontró ningún docente con esa cédula.")


        # Opción 5: Registrar una visita escolar/didáctica a un estudiante
        elif opcionSeleccionada == "5":
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
                    lineaVisita = (
                            str(docenteEncontrado.cedula) + " - " + str(docenteEncontrado.nombre) + ", " +
                            str(practicanteEncontrado.cedula) + " - " + str(practicanteEncontrado.nombre) + ", " +
                            str(fechaVisita) + ", " + str(calificacionVisita) + ", " + str(observacionesVisita) + "\n"
                    )
                    archivoVisitas.write(lineaVisita)
                    archivoVisitas.close()
                except Exception as errorArchivo:
                    print("Error al guardar visita:", errorArchivo)


                promedioActual = calcularPromedioPracticante(practicanteEncontrado, listaVisitas)
                print("\n¡Visita registrada con éxito!")
                print("   Promedio actual del practicante: " + str(promedioActual))


        # Opción 6: Ver el promedio final de las visitas de un practicante específico
        elif opcionSeleccionada == "6":
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


        # Opción 7: Listar visitas (permite ver todas o filtrar por un practicante específico)
        elif opcionSeleccionada == "7":
            print("\n--- MENÚ DE VISITAS ---")
            print("1. Ver todas las visitas registradas")
            print("2. Ver visitas de un practicante en específico")
            subOpcionVisita = input("Elija una opción: ").strip()


            # Opción 7.1: Mostrar absolutamente todas las visitas del sistema
            if subOpcionVisita == "1":
                print("\n--- LISTA COMPLETA DE VISITAS ---")
                if not listaVisitas:
                    print("Aún no hay visitas registradas.")
                else:
                    for visitaActual in listaVisitas:
                        print(str(visitaActual))


            # Opción 7.2: Filtrar y mostrar únicamente las visitas del practicante que elijamos
            elif subOpcionVisita == "2":
                print("\n--- FILTRAR VISITAS POR PRACTICANTE ---")
                if not listaPracticantes:
                    print("No hay practicantes registrados.")
                else:
                    cedulaBuscada = input("Ingrese la cédula del practicante: ").strip()


                    # Verificamos primero si el practicante existe en el sistema
                    practicanteEncontrado = None
                    for p in listaPracticantes:
                        if str(p.cedula).strip() == cedulaBuscada:
                            practicanteEncontrado = p
                            break


                    if not practicanteEncontrado:
                        print("No se encontró un practicante con esa cédula.")
                    else:
                        print("\n--- VISITAS DE: " + str(practicanteEncontrado.nombre) + " ---")
                        contadorVisitas = 0


                        # Recorremos todas las visitas y filtramos solo las que coincidan con la cédula
                        for visitaActual in listaVisitas:
                            if str(visitaActual.practicante.cedula).strip() == cedulaBuscada:
                                print(str(visitaActual))
                                contadorVisitas += 1


                        # Si el alumno existe pero no tiene visitas cargadas todavía
                        if contadorVisitas == 0:
                            print("Este practicante aún no tiene visitas registradas.")
            else:
                print("Opción no válida.")


        # Opción 8: Armar el tribunal examinador final para un alumno y guardarlo en la lista
        elif opcionSeleccionada == "8":
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
                    if str(practicanteActual.cedula).strip() == cedulaPracticanteElegido:
                        practicanteElegido = practicanteActual
                        break


                if not practicanteElegido:
                    print("Practicante no encontrado.")
                    continue


                def buscarMiembroTribunal(mensajePrompt):
                    while True:
                        cedulaIngresada = input(mensajePrompt).strip()
                        for docenteActual in listaDocentes:
                            if str(docenteActual.cedula).strip() == cedulaIngresada:
                                return docenteActual
                        for adscriptorActual in listaAdscriptores:
                            if str(adscriptorActual.cedula).strip() == cedulaIngresada:
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
                else:
                    tercerMiembro = None


                # Verificamos si el practicante ya tenía un tribunal asignado para reemplazarlo o agregarlo nuevo
                tribunalExistente = None
                for t in listaTribunales:
                    if str(t.practicante.cedula).strip() == str(practicanteElegido.cedula).strip():
                        tribunalExistente = t
                        break


                if tribunalExistente:
                    # Si ya existía, actualizamos sus miembros en memoria
                    tribunalExistente.primerMiembro = primerMiembro
                    tribunalExistente.segundoMiembro = segundoMiembro
                    tribunalExistente.tercerMiembro = tercerMiembro
                    tribunalAfectado = tribunalExistente
                    print("\n¡Tribunal actualizado con éxito!")
                else:
                    # Si es nuevo, lo creamos y lo guardamos en la lista general en memoria
                    nuevoTribunal = TribunalFinal(practicanteElegido, primerMiembro, segundoMiembro, tercerMiembro)
                    listaTribunales.append(nuevoTribunal)
                    tribunalAfectado = nuevoTribunal
                    print("\n¡Tribunal asignado con éxito!")


                # PERSISTENCIA: Sobrescribimos el archivo de texto con la lista actualizada completa
                # PERSISTENCIA: Guardamos con cédula y nombre para mayor claridad visual
                try:
                    archivoTribunales = open("persistencia/tribunales.txt", "w")
                    for t in listaTribunales:
                        lineaTribunal = (
                                str(t.practicante.cedula) + " - " + str(t.practicante.nombre) + ", " +
                                str(t.primerMiembro.cedula) + " - " + str(t.primerMiembro.nombre) + ", " +
                                str(t.segundoMiembro.cedula) + " - " + str(t.segundoMiembro.nombre) + ", "
                        )


                        if t.tercerMiembro is not None:
                            lineaTribunal += str(t.tercerMiembro.cedula) + " - " + str(t.tercerMiembro.nombre) + "\n"
                        else:
                            lineaTribunal += "N/D - No asignado\n"


                        archivoTribunales.write(lineaTribunal)
                    archivoTribunales.close()
                except Exception as errorArchivo:
                    print("Error al guardar el tribunal en el archivo:", errorArchivo)


                # Mostramos cómo quedó conformado el tribunal finalmente
                print(str(tribunalAfectado))


        # Opción 9: Consultar/Listar el tribunal de un practicante buscando por cédula
        elif opcionSeleccionada == "9":
            print("\n[Consultar Tribunal de Practicante]")
            if not listaTribunales:
                print("Aún no hay tribunales asignados en el sistema.")
            else:
                cedulaBuscada = input("Ingrese la cédula del practicante a consultar: ").strip()
                tribunalEncontrado = None


                for t in listaTribunales:
                    if str(t.practicante.cedula).strip() == cedulaBuscada:
                        tribunalEncontrado = t
                        break


                if tribunalEncontrado:
                    print(str(tribunalEncontrado))
                else:
                    print("No se encontró un tribunal asignado para ese practicante.")


        elif opcionSeleccionada == "10":
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
    listaTribunales = []


    # 1. Carga automática de Centros desde la carpeta persistencia
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


    # 2. Carga automática de Adscriptores desde la carpeta persistencia (¡Corregido con la lista de grupos!)
    try:
        archivoAdscriptores = open("persistencia/adscriptores.txt", "r")
        for lineaActual in archivoAdscriptores:
            partesLinea = [parte.strip() for parte in lineaActual.strip().split(",")]
            if len(partesLinea) >= 6:
                cedula = partesLinea[0]
                nombre = partesLinea[1]
                mail = partesLinea[2]
                contacto = partesLinea[3]
                centroPractica = partesLinea[4]


                textoGrupos = partesLinea[5]
                listaGruposObj = []
                for g_str in textoGrupos.split(";"):
                    if g_str.strip():
                        datos_g = [d.strip() for d in g_str.split("|")]
                        if len(datos_g) >= 3:
                            listaGruposObj.append({
                                'grupo': datos_g[0],
                                'dias': datos_g[1],
                                'horario': datos_g[2]
                            })


                nuevoAdscriptor = Adscriptor(cedula, nombre, mail, contacto, centroPractica, listaGruposObj)
                listaAdscriptores.append(nuevoAdscriptor)
        archivoAdscriptores.close()
    except FileNotFoundError:
        pass


    # 3. Carga automática de Practicantes desde la carpeta persistencia
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


    # 4. Carga automática de Docentes de Didáctica desde la carpeta persistencia
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


    # 5. Carga automática de Visitas desde la carpeta persistencia (Actualizado para leer nombres con guión)
    try:
        archivoVisitas = open("persistencia/visitas.txt", "r")
        for lineaActual in archivoVisitas:
            partesLinea = [parte.strip() for parte in lineaActual.strip().split(",")]
            if len(partesLinea) >= 5:
                # Cortamos en el guión para quedarnos únicamente con la cédula limpia (ej: "12345678 - Juan" -> "12345678")
                cedDoc = partesLinea[0].split("-")[0].strip()
                cedPrac = partesLinea[1].split("-")[0].strip()


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


    # 6. Carga automática de Tribunales desde la carpeta persistencia (Versión con limpieza de guiones por seguridad)
    listaTribunales = []
    try:
        archivoTribunales = open("persistencia/tribunales.txt", "r")
        for lineaActual in archivoTribunales:
            partesLinea = [parte.strip() for parte in lineaActual.strip().split(",")]
            if len(partesLinea) >= 4:
                # Extraemos las cédulas limpias por si el archivo guarda nombres con guiones
                cedPrac = partesLinea[0].split("-")[0].strip()
                cedM1 = partesLinea[1].split("-")[0].strip()
                cedM2 = partesLinea[2].split("-")[0].strip()
                cedM3 = partesLinea[3].split("-")[0].strip()


                # Buscamos al practicante recorriendo la lista con un for básico
                pracObj = None
                for p in listaPracticantes:
                    if str(p.cedula).strip() == cedPrac:
                        pracObj = p
                        break  # Apenas lo encontramos, rompemos el ciclo para optimizar


                # Unimos temporalmente las listas de docentes y adscriptores para buscar a los miembros
                todosDocentesYAdscriptores = listaDocentes + listaAdscriptores


                # Buscamos al 1er miembro
                m1Obj = None
                for d in todosDocentesYAdscriptores:
                    if str(d.cedula).strip() == cedM1:
                        m1Obj = d
                        break


                # Buscamos al 2do miembro
                m2Obj = None
                for d in todosDocentesYAdscriptores:
                    if str(d.cedula).strip() == cedM2:
                        m2Obj = d
                        break


                # Buscamos al 3er miembro (solo si no es "N/D")
                m3Obj = None
                if cedM3 != "N/D":
                    for d in todosDocentesYAdscriptores:
                        if str(d.cedula).strip() == cedM3:
                            m3Obj = d
                            break


                # Si encontramos al practicante y a los dos primeros miembros obligatorios, creamos el tribunal
                if pracObj and m1Obj and m2Obj:
                    tCargado = TribunalFinal(pracObj, m1Obj, m2Obj, m3Obj)
                    listaTribunales.append(tCargado)


        archivoTribunales.close()
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
            menuDocenteDidactica(listaDocentes, listaAdscriptores, listaPracticantes, listaVisitas, listaTribunales)
        elif opcionSeleccionada == "5":
            print("\n¡Saliendo del sistema. Hasta luego!")
            break
        else:
            print("Opción incorrecta. Intentá otra vez.")


if __name__ == "__main__":
    main()
