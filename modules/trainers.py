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
            "nombre": trainer1,
            "apellidos" : apellidos,
            "idioma que domina": idioma,
        
        }
        trainers.append(trainer)

        print ("el trainer fue registrado con exito")

def listar_trainers():
    if trainers:
        for trainser in trainers:
            print(f"""ID:{trainser["ID"]}\nnombre:{trainser["nombre"]} {trainser["apellidos"]}\nidioma que domina: {trainser["idioma que domina"]}""")
            print("-"*60)

def asignar_ruta_trainer(id_trainer, ruta):
    pass