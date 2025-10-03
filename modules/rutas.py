import camperss as c


rutas=[]
def crear_ruta():
    programacion=["Java", "JavaScript", "C#"]
    base_de_datos=["Mysql", "MongoDb" , "Postgresql"]
    Backend=["NetCore", "Spring Boot", "NodeJS" , "Express"] 
    
    print("------ Registro de ruta ------")

    ID_ruta= input("ingrese el ID de la ruta: ")
    for ruta in rutas:
        if ruta["ID"]== ID_ruta:
            print("ID ya existente")
            return
    
    print("Java, JavaScript, C#")   
    modulo_Programacion=input ("ingrese un idioma de los presentados: ")
    

    print("Mysql, MongoDb ,Postgresql")
    modulo_BasesDeDatos= input("ingrese una base de datos de laa presentadas: ") 
    print("Mysql, MongoDb ,Postgresql")
    modulo_BasesDeDatos2= input("ingrese una base de datos de laa presentadas: ") 
    

    print("NetCore, Spring Boot, NodeJS , Express")
    modulo_Backend=input ("ingrese un baken de los mostrados: ")

    fundamentos=("Introducción a la algoritmia", "PSeInt" , "Python")
    Web=("HTML","CSS", "Bootstrap")
    modulos=[fundamentos,Web,modulo_Programacion,modulo_BasesDeDatos,modulo_BasesDeDatos2,modulo_Backend]

    ruta = {
        "ID": ID_ruta,
        "modulos" :modulos,
        "capacidad": 33,
        "camper": [],
        "trainers" : []
    }
    rutas.append(ruta)



def listar_rutas():
    if rutas:
        ID=input ("ingrese el ID de la ruta: ")
        for ruta in rutas:
            if ruta["ID"]== ID :
                print(f"""ID:{ruta["ID"]}\nmodulos:{ruta["modulos"]}""")
                print("-"*60)
    else :
        print("no hay rutas registrados")            
    

def asignar_camper_a_ruta():
    
    ID_camper=input("ingrese el ID del camper que dedea asignar a la ruta: ")
    ID_ruta= input("ingresar el ID de la ruta: ")
    
    camper_encontrado= None
    ruta_encotrada= None
    
    for camper in c.campers :
        if camper["ID"]==  ID_camper:
            camper_encontrado= camper
            break
            
            
    if not camper_encontrado:
            print("error, ID inexistente") 
            return                  
            
    for ruta in rutas:
        if ruta["ID"]==  ID_ruta:
            ruta_encotrada=ruta
            break
            

        else:
            print("error, ID de ruta inexistente")
                    
    if len(ruta_encotrada) < ruta_encotrada["capacidad"]:
            ruta_encotrada ["camper"].append(camper_encontrado)
            print("camper asignado con exito")
    else:
            print("capacidad maxima alcanzada")
            
