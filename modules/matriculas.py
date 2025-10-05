import utils.io_jon as j

ARCHIVO_TRAINERS = "data/trainers.json"
ARCHIVO_RUTAS = "data/rutas.json"


def listar_matriculas():
    print("Busqueda de matrícula")
    opcion = input("¿Desea buscar por ruta (R) o por Trainer (T)? ").upper()

    if opcion == "T":
        t = input("Ingrese el ID del trainer encargado: ")

        data_trainers = j.read_json(ARCHIVO_TRAINERS).get("trainers", [])
        for trainer in data_trainers:
            if trainer["ID"] == t:
                print(f"ID: {trainer['ID']}\nNombre: {trainer['datos']['nombre']}\nRuta: {trainer['datos']['ruta']}")
                return
        print("Trainer no encontrado")

    elif opcion == "R":
        r = input("Ingrese el ID de la ruta: ")

        data_rutas = j.read_json(ARCHIVO_RUTAS).get("rutas", [])
        for ruta in data_rutas:
            if ruta["ID"] == r:
                print(f"Ruta: {ruta['ID']}\nArea: {ruta['data']['area']}\nCampers: {ruta['data']['campers']}")
                return
        print("Ruta no encontrada")

    else:
        print("❌ Opción inválida")
        
            
            
    


    

    
def actualizar_matricula():
    print("¿Qué desea actualizar?")
    print("1. Trainer")
    print("2. horario")
    print("3. aula")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        tr_id = input("Ingrese el ID del trainer que desea actualizar: ")
        tr_f= input("ingrese el nuevo trainer: ")
        trainers = j.read_json(ARCHIVO_TRAINERS)
        if trainers:
            for trainer in trainers:
                if trainer["ID"]== tr_id:
                    k=trainer.pop(trainer["datos"]["ruta"])
            for trainer in trainers:
                if trainer["ID"]== tr_f:
                    trainer["datos"]["ruta"].append(k)
                    j.write_json(ARCHIVO_TRAINERS, {"trainers": trainers})

        else:
            print("no hay trainers registrados")
            
    elif opcion == "2":

        i=input("ingrese el ID de la ruta: ")
        rutas = j.read_json(ARCHIVO_RUTAS)
        if rutas:
            for ruta in rutas:
                if ruta["ID"]== i:
                    print("ingrese el horario")
                    print("1. 7-11")
                    print("2. 11-15") 
                    print("3. 15-19")
                    hora= input("ingrese la hora inicio: ")
                    if hora == "1":
                        hora="7-11"       
                    elif hora == "2":
                        hora = "11-15"       
                    elif hora == "3":
                        hora = "11-15"
                    else:
                        print("opcion invalida")

                        ruta["data"]["area"]["hora"]=hora
                        j.write_json(ARCHIVO_RUTAS, rutas)
                        

        
                    
    elif opcion == "3":
        k=input("ingrese el ID de la ruta: ")
        rutas = j.read_json(ARCHIVO_RUTAS)
        if rutas:
            for ruta in rutas:
                if ruta["ID"]== k:
                        print("ingrese un salon")
                        print("1.Apolo")
                        print("2.Artemis")
                        print("3.Spuntnik")   
                        salon= input ("selecione una opcion: ")
                        if salon == "1":
                            salon="Apolo"       
                        elif salon == "2":
                            salon = "Artemis"       
                        elif salon == "3":
                            salon = "Spuntnik"
                        else:
                            print("opcion invalida")

                        ruta["data"]["area"]["salon"]=salon



    else:
        print("❌ Opción inválida")