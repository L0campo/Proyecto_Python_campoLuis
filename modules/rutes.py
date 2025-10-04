import modules.campers as c







rutas=[]

def crear_ruta():
    
    print("------ Registro de ruta ------")

    ID_ruta= input("ingrese el ID de la ruta: ")
    for ruta in rutas:
        if ruta["ID"]== ID_ruta:
            print("ID ya existente")
            return
    print("ingrese un idioma de programacion")
    print("1.Java")
    print("2.JavaScript")
    print("3.C#")  
    modulo_Programacion=input ("selecione una opcion: ")
    if modulo_Programacion == "1":
        modulo_Programacion="java"       
    elif modulo_Programacion == "2":
        modulo_Programacion = "javaScript"       
    elif modulo_Programacion == "3":
        modulo_Programacion = "c#"
    else:
        print("opcion invalida")
        
    print("="*30)


    print("ingrese dos bases de datos")
    print("1.Mysql")
    print("2.MongoDb")
    print("3.postgresql")
    modulo_BasesDeDatos= input("ingrese una base de datos de laa presentadas: ") 
    modulo_BasesDeDatos2= input("ingrese una base de datos de laa presentadas: ") 
    if modulo_Programodulo_BasesDeDatosmacion == "1":
        modulo_Programacion="java"       
    elif modulo_Programacion == "2":
        modulo_Programacion = "javaScript"       
    elif modulo_Programacion == "3":
        modulo_Programacion = "c#"
    else:
        print("opcion invalida")
    
    

    print("NetCore, Spring Boot, NodeJS , Express")
    modulo_Backend=input ("ingrese un baken de los mostrados: ")

    fundamentos=("Introducción a la algoritmia", "PSeInt" , "Python")
    Web=("HTML","CSS", "Bootstrap")
    modulos=[fundamentos,Web,modulo_Programacion,modulo_BasesDeDatos,modulo_BasesDeDatos2,modulo_Backend]

    ruta = {
        "ID": ID_ruta,
        "data":{        
        "modulos" :modulos,
        "capacidad": 33,
        "area": [],
        "campers": []
    }  }
    rutas.append(ruta)



def listar_rutas():
    if rutas:
        ID=input ("ingrese el ID de la ruta: ")
        for ruta in rutas:
            if ruta["ID"]== ID :
                print(f"""ID:{ruta["ID"]}\nmodulos:{ruta["data"]["modulos"]}""")
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
            

    if not ruta_encotrada:
        print("error, ID de ruta inexistente")
        return
                    
    if len(ruta_encotrada["data"]["campers"]) < ruta_encotrada["data"]["capacidad"]:
            ruta_encotrada["data"]["campers"].append(camper_encontrado)
            

            


            print("camper asignado con exito")
    else:
        print("capacidad maxima alcanzada")
            
def asignar_area_ruta():
        salon= input ("ingrese el salon selecionado: ")
        hora= input("ingrese la hora inicio: ")
        hora1= input("ingrese la hora fin")

        area={
            "salon": salon,
            "detalles":{
                "hora":hora,
                "horaf":hora1,               
                
            }
        }
        return area