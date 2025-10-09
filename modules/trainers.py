import modules.rutes as r
import utils.io_jon as j   

ARCHIVO_TRAINERS = "data/trainers.json"
ARCHIVO_RUTAS = "data/rutas.json"


j.initialize_json(ARCHIVO_TRAINERS, {"trainers": []})

def registrar_trainer():
        data = j.read_json(ARCHIVO_TRAINERS)
        trainers = data.get("trainers", [])
        
        print("------ Registro de Trainer ------")
        ID = input ("ingrese el ID del trainer: ")
    
        for trainer in trainers:
            if trainer["ID"]== ID:      
                print("ya existe ese ID")       
                return
       
                
            
            
        
    
        trainer1 = input ("ingrese el nombre del trainer que desea ingresar: ")
        apellidos = input ("ingrese los apellidos del trainer: ")
        
        print("ingrese un idioma de programacion en el cual se especializa")
        print("1.Java")
        print("2.JavaScript")
        print("3.C#")  
        opcion=input ("selecione una opcion: ")
        if opcion == "1":
            idioma="java"       
        elif opcion == "2":
            idioma = "javaScript"       
        elif opcion == "3":
            idioma = "c#"
        else:
            print("opcion invalida")
            return
            
        print("="*30)
        
 

        

        
        

        trainer ={
            "ID": ID,
            "datos": { 
            "nombre": trainer1,
            "apellidos" : apellidos,
            "idioma": idioma,
            "ruta":[]
        
        } }
        trainers.append(trainer)
        data["trainers"] = trainers
        j.write_json(ARCHIVO_TRAINERS, data)

        print ("el trainer fue registrado con exito")

def listar_trainers():

    data = j.read_json(ARCHIVO_TRAINERS)
    trainers = data.get("trainers", [])

    if trainers:
        for trainer in trainers:
            rutas = trainer["datos"].get("ruta", [])
            rutas_asignadas = ", ".join([ruta["ID"] for ruta in rutas]) if rutas else "Ninguna"

            print(f"""
ID: {trainer['ID']}
Nombre: {trainer['datos']['nombre']} {trainer['datos']['apellidos']}
Idioma que domina: {trainer['datos']['idioma']}
Ruta asignada: {rutas_asignadas}
""")
            print("-" * 60)
    else:
        print("❌ No hay trainers registrados")
        

def asignar_ruta_trainer():
    data = j.read_json(ARCHIVO_TRAINERS)
    trainers = data.get("trainers", [])
    data = j.read_json(ARCHIVO_RUTAS)
    rutas = data.get("rutas", [])
    if trainers:
        ID_trainer=input("ingrese el ID del trainer que deses asignarle una ruta: ")
        ID_ruta= input("ingresar el ID de la ruta: ")

        trainer_encontrado= None
        ruta_encotrada= None
        for ruta in rutas: 
            if ruta["ID"]==  ID_ruta:
                ruta_encotrada= ruta
                break
                
        if not ruta_encotrada:
            print("error, ID inexistente") 
            j.pasuar()
            return  

        for trainer in trainers:
            if trainer["ID"]==  ID_trainer:
                trainer_encontrado=trainer
                break
                

        if not trainer_encontrado:
            print ("error, ID inexistente")
                
                        
        
        trainer_encontrado["datos"]["ruta"].append(ruta_encotrada)
        j.write_json(ARCHIVO_TRAINERS, {"trainers": trainers})

    else:
        print("no hay trainers registrados")            

                


    