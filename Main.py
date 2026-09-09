# ==========================================
# SUBMENÚ 1: LICEOS
# ==========================================
def menuLiceos(gestion, repositorio):
    while True:
        print("\n--- (1) MENÚ LICEOS ---")
        print("1. Registrar")
        print("2. Modificar")
        print("3. Borrar")
        print("4. Listar")
        print("5. Salir")
        opcion = input("Elegir opción: ").strip()

        if opcion == "1":
            print("\n[Registrar Liceo]")
            # Lógica para registrar liceo...
        elif opcion == "2":
            print("\n[Modificar Liceo]")
            # Lógica para modificar liceo...
        elif opcion == "3":
            print("\n[Borrar Liceo]")
            # Lógica para borrar liceo...
        elif opcion == "4":
            print("\n[Listar Liceos]")
            # Lógica para listar liceos...
        elif opcion == "5":
            break  # Vuelve al Menú Principal
        else:
            print("Opción no válida.")


# ==========================================
# SUBMENÚ 2: ADSCRIPTORES
# ==========================================
def menuAdscriptores(gestion, repositorio):
    while True:
        print("\n--- (2) MENÚ ADSCRIPTORES ---")
        print("1. Registrar")
        print("2. Modificar")
        print("3. Borrar")
        print("4. Listar")
        print("5. Salir")
        opcion = input("Elegir opción: ").strip()

        if opcion == "1":
            print("\n[Registrar Adscriptor]")
        elif opcion == "2":
            print("\n[Modificar Adscriptor]")
        elif opcion == "3":
            print("\n[Borrar Adscriptor]")
        elif opcion == "4":
            print("\n[Listar Adscriptores]")
        elif opcion == "5":
            break
        else:
            print("Opción no válida.")


# ==========================================
# SUBMENÚ 3: PRACTICANTES
# ==========================================
def menuPracticantes(gestion, repositorio):
    while True:
        print("\n--- (3) MENÚ PRACTICANTES ---")
        print("1. Registrar")
        print("2. Modificar")
        print("3. Borrar")
        print("4. Listar")
        print("5. Salir")
        opcion = input("Elegir opción: ").strip()

        if opcion == "1":
            print("\n[Registrar Practicante]")
        elif opcion == "2":
            print("\n[Modificar Practicante]")
        elif opcion == "3":
            print("\n[Borrar Practicante]")
        elif opcion == "4":
            print("\n[Listar Practicantes]")
        elif opcion == "5":
            break
        else:
            print("Opción no válida.")


# ==========================================
# SUBMENÚ 4: DOCENTE DIDÁCTICA
# ==========================================
def menuDocenteDidactica(gestion, repositorio):
    while True:
        print("\n--- (4) MENÚ DOCENTE DIDÁCTICA ---")
        print("1. Registrar")
        print("2. Modificar")
        print("3. Listar")
        print("4. Tribunal Final")
        print("5. Salir")
        opcion = input("Elegir opción: ").strip()

        if opcion == "1":
            print("\n[Registrar Docente Didáctica]")
        elif opcion == "2":
            print("\n[Modificar Docente Didáctica]")
        elif opcion == "3":
            print("\n[Listar Docentes Didáctica]")
        elif opcion == "4":
            print("\n[Gestión de Tribunal Final]")
        elif opcion == "5":
            break
        else:
            print("Opción no válida.")


# ==========================================
# MENÚ PRINCIPAL Y PUNTO DE ENTRADA
# ==========================================
def main():
    # Aquí puedes instanciar tus clases de lógica y persistencia
    gestion = None
    repositorio = None

    while True:
        print("\n==========================================")
        print("            MENÚ PRINCIPAL               ")
        print("==========================================")
        print("1. Liceos")
        print("2. Adscriptores")
        print("3. Practicantes")
        print("4. Docente Didáctica")
        print("5. Salir")

        opcion = input("Elegir opción: ").strip()

        if opcion == "1":
            menuLiceos(gestion, repositorio)
        elif opcion == "2":
            menuAdscriptores(gestion, repositorio)
        elif opcion == "3":
            menuPracticantes(gestion, repositorio)
        elif opcion == "4":
            menuDocenteDidactica(gestion, repositorio)
        elif opcion == "5":
            print("\n¡Gracias por usar el sistema! Saliendo...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()