import modules.rutes as r
import utils.io_jon as j   

ARCHIVO_TRAINERS = "data/trainers.json"


j.initialize_json(ARCHIVO_TRAINERS, {"trainers": []})

def registrar_trainer():
        data = j.read_json(ARCHIVO_TRAINERS)
        trainers = data.get("trainers", [])
        
        print("------ Registro de Trainer ------")
        ID = input ("ingrese el ID del trainer: ")
    
        for trainer in trainers:
            if trainer["ID"]== ID:
                print("ID ya existente")
                return
    
        trainer1 = input ("ingrese el nombre del trainer que desea ingresar: ")
        apellidos = input ("ingrese los apellidos del camper: ")
        
        print("ingrese un idioma de programacion")
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
            print(f"""
ID: {trainer["ID"]}\n
Nombre: {trainer["datos"]["nombre"]} apellido: {trainer["datos"]["apellidos"]}\n
Idioma que domina: {trainer["datos"]["idioma"] }\n Ruta asignada: {trainer["datos"]["ruta"]}
""")
            
            print("-"*60)

def asignar_ruta_trainer():
    data = j.read_json(ARCHIVO_TRAINERS)
    trainers = data.get("trainers", [])
    if trainers:
        ID_trainer=input("ingrese el ID del trainer que deses asignarle una ruta: ")
        ID_ruta= input("ingresar el ID de la ruta: ")

        trainer_encontrado= None
        ruta_encotrada= None
        for ruta in r.rutas: 
            if ruta["ID"]==  ID_ruta:
                ruta_encotrada= ruta
                break
                
        if not ruta_encotrada:
            print("error, ID inexistente") 
            return  

        for trainer in trainers:
            if trainer["ID"]==  ID_trainer:
                trainer_encontrado=trainer
                break
                

            else:
                print("error, ID de ruta inexistente")
                        
        
        trainer_encontrado["datos"]["ruta"].append(ruta_encotrada)
        j.write_json(ARCHIVO_TRAINERS, data)

    else:
        print("no hay trainers registrados")            

                


    