trainers=[]
def registrar_trainer():
        programacion=["Java", "JavaScript", "C#"]
        print("------ Registro de Trainer ------")
        ID = input ("ingrese el ID del trainer: ")
    
        for trainer in trainers:
            if trainer["ID"]== ID:
                print("ID ya existente")
                return
    
        trainer1 = input ("ingrese el nombre del trainer que desea ingresar: ")
        apellidos = input ("ingrese los apellidos del camper: ")
        print(programacion)
        idioma= input("ingrese el idioma que domina el trainer: ").lower()
        
        if idioma in programacion:
            idioma= idioma
        else:
            print("ingrese un idioma valido")

        

        
        

        trainer ={
            "ID": ID,
            "datos": { 
            "nombre": trainer1,
            "apellidos" : apellidos,
            "idioma que domina": idioma,
            "ruta":[]
        
        } }
        trainers.append(trainer)

        print ("el trainer fue registrado con exito")

def listar_trainers():
    if trainers:
        for trainer in trainers:
            print(f"""
ID: {trainer["ID"]}\n
Nombre: {trainer["datos"]["nombre"]} {trainer["datos"]["apellidos"]}\n
Idioma que domina: {trainer["datos"]["idioma"] }\n Ruta asignada: {trainer["datos"]["ruta"]}
""")
            
            print("-"*60)

def asignar_ruta_trainer():
    
    ID_trainer=input("ingrese el ID del trainer que deses asignarle una ruta: ")
    ID_ruta= input("ingresar el ID de la ruta: ")

    trainer_encontrado= None
    ruta_encotrada= None