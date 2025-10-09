def logi ():
        print("====== CampusLands ======".center(50))
        print("1.camper")
        print("2.trainer")
        print("3.cordinacion")
        print("4.TES")
        print("0.salir")
        opcion=int(input("ingrese una opcion correspondiente del 0-3: "))
        return opcion

def menu_trainer ():
        print("\n--- MENÚ TRAINER ---")
        print("1. Ver campers asignados")
        print("2. Registrar notas de modulos")
        print("3. Calcular promedios")
        print("0. Cerrar sesión")
        opcion = int(input("👉 Seleccione una opción: "))
        return opcion

def menu_camper():
        print("\n--- MENÚ CAMPER ---")
        print("1. Ver ruta asignada")
        print("2. Ver notas")
        print("3. Consultar estado")
        print("0. Cerrar sesión")
        opcion = int(input("👉 Seleccione una opción: "))
        return opcion

def menu_admit():
        print("\n--- MENÚ COORDINADOR ---")
        print("1. Registrar camper")
        print("2. Registrar trainer")
        print("3. Crear rutas")
        print("4. Matricular camper")
        print("5. Generar reportes")
        print("0. Cerrar sesión")
        opcion = int(input("👉 Seleccione una opción: "))
        return opcion


def menu_regisCamper():
        print("--- Registro de camper ---")
        print("1. Registrar camper")
        print("2. lista de camper por estado")
        print("3. actulizar estado de camper")
        print("4. lista de estado por riesgo")
        print("5. actualizar riesgo del camper")
        print("0.salir")
        opcion = int(input("👉 Seleccione una opción: "))
        return opcion

def menu_registrainer():
        print("--- Registro de trainer ---")
        print("1.Registrar trainer")
        print("2.lista de trainer")
        print("3.asignar ruta a trainer")
        print("0.salir")
        opcion = int(input("👉 Seleccione una opción: "))
        return opcion
def menu_regisRuta():
        print("--- Registro de ruta ---")
        print("1.Registrar ruta")
        print("2.lista de ruta")
        print("0.salir")
        opcion = int(input("👉 Seleccione una opción: ") )
        return opcion
def menu_repot():
        print("--- Reportes ---")
        print("1. Campers inscritos y aprobados")
        print("2. Trainers activos")
        print("3. Campers bajo rendimiento")
        opcion = int(input("👉 Seleccione una opción: "))
        return opcion
def menu_matriculas():
        print("--- Matriculas ---")
        print("1. listar matriculas")
        print("2. actualizar matriculas")
        print("3. matricular camper")
        print("0.salir")
        opcion = int(input("👉 Seleccione una opción: " ))
        return opcion