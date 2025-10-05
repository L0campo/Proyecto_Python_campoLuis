import modules.campers as c
import utils.io_jon as j
ARCHIVO_RUTAS = "rutas.json"


j.initialize_json(ARCHIVO_RUTAS, {"rutas": []})
data = j.read_json(ARCHIVO_RUTAS)
rutas = data.get("rutas", [])






rutas=[]

def crear_ruta():
    
    print("------ Registro de ruta ------")
    data = j.read_json(ARCHIVO_RUTAS)
    rutas = data.get("rutas", [])

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
    modulo_BasesDeDatos= input("selecione una opcion: ") 
    modulo_BasesDeDatos2= input("selecione una opcion: ") 
    if modulo_BasesDeDatos == "1":
        modulo_BasesDeDatos="Mysql"       
    elif modulo_BasesDeDatos == "2":
        modulo_BasesDeDatos = "MongoDb"       
    elif modulo_Programacion == "3":
        modulo_BasesDeDatos = "postgresql"
    else:
        print("opcion invalida")

    if modulo_BasesDeDatos2 == "1":
        modulo_BasesDeDatos2="Mysql"       
    elif modulo_BasesDeDatos2 == "2":
        modulo_BasesDeDatos2 = "MongoDb"       
    elif modulo_BasesDeDatos2 == "3":
        modulo_BasesDeDatos2 = "postgresql"
    else:
        print("opcion invalida")
    
    print("="*30)
    
    print("ingrese un backend")
    print("1.Netcore")
    print("2.Spring Boot")
    print("3.NodeJS")
    print("4.Express")
    
    modulo_Backend=input ("selecione una opcion: ")
    if modulo_Backend == "1":
        modulo_Backend="Netcore"       
    elif modulo_Backend== "2":
        modulo_Backend = "Spring Boot"       
    elif modulo_Backend == "3":
        modulo_Backend = "NodeJS"
    elif modulo_Backend == "4":
        modulo_Backend = "Express"
    else:
        print("opcion invalida")
    

    fundamentos=("Introducción a la algoritmia", "PSeInt" , "Python")
    Web=("HTML","CSS", "Bootstrap")
    modulos=[fundamentos,Web,modulo_Programacion,modulo_BasesDeDatos,modulo_BasesDeDatos2,modulo_Backend]
    
    print("="*30)
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
    print("="*30)  
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
        

    area={
        "salon": salon,
        "hora":hora,
        }
    
        

    ruta = {
        "ID": ID_ruta,
        "data":{        
        "modulos" :modulos,
        "capacidad": 33,
        "area": area,
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
    data = j.read_json(ARCHIVO_RUTAS)
    rutas = data.get("rutas", [])
    if rutas:
        ID_camper=input("ingrese el ID del camper que dedea asignar a la ruta: ")
        ID_ruta= input("ingresar el ID de la ruta: ")
        
        camper_encontrado= None
        ruta_encotrada= None
        
        for camper in c.campers :
            if camper["ID"]==  ID_camper:
                if camper["datos"]["estado"] == "aprodado":

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

    else:
        print("no hay rutas registradas")            
