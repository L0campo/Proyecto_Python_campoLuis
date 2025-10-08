
import utils.io_jon as j
ARCHIVO_RUTAS = "data/rutas.json"
FILE = "data/campers.json"

j.initialize_json(FILE, {"campers": []})
data = j.read_json(FILE)
campers = data.get("campers", [])



j.initialize_json(ARCHIVO_RUTAS, {"rutas": []})

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
    Programacion=input ("selecione una opcion: ")
    if Programacion == "1":
        modulo_Programacion="java"       
    elif Programacion == "2":
        modulo_Programacion = "javaScript"       
    elif Programacion == "3":
        modulo_Programacion = "c#"
    else:
        print("opcion invalida")
        return
        
        
    print("="*30)


    print("ingrese dos bases de datos")
    print("1.Mysql")
    print("2.MongoDb")
    print("3.postgresql")
    BasesDeDatos= input("selecione una opcion: ") 
    BasesDeDatos2= input("selecione una opcion: ") 
    if BasesDeDatos == "1":
        modulo_BasesDeDatos="Mysql"       
    elif BasesDeDatos == "2":
        modulo_BasesDeDatos = "MongoDb"       
    elif Programacion == "3":
        modulo_BasesDeDatos = "postgresql"
    else:
        print("opcion invalida")
        return

    if BasesDeDatos2 == "1":
        modulo_BasesDeDatos2="Mysql"       
    elif BasesDeDatos2 == "2":
        modulo_BasesDeDatos2 = "MongoDb"       
    elif BasesDeDatos2 == "3":
        modulo_BasesDeDatos2 = "postgresql"
    else:
        print("opcion invalida")
        return
    
    print("="*30)
    
    print("ingrese un backend")
    print("1.Netcore")
    print("2.Spring Boot")
    print("3.NodeJS")
    print("4.Express")
    
    Backend=input ("selecione una opcion: ")
    if Backend == "1":
        modulo_Backend="Netcore"       
    elif Backend== "2":
        modulo_Backend = "Spring Boot"       
    elif Backend == "3":
        modulo_Backend = "NodeJS"
    elif Backend == "4":
        modulo_Backend = "Express"
    else:
        print("opcion invalida")
        return
    

    fundamentos=( "Introducción a la algoritmia" , "PSeInt" , "Python" )
    Web=( "HTML" , "CSS" , "Bootstrap" )
    modulos=[ fundamentos , Web , modulo_Programacion ,modulo_BasesDeDatos ,modulo_BasesDeDatos2 ,modulo_Backend ]
    
    j.clear_screen()
    
    print("="*30)
    print("ingrese un salon")
    print("1.Apolo")
    print("2.Artemis")
    print("3.Spuntnik")   
    salon1= input ("selecione una opcion: ")
    if salon1 == "1":
        salon="Apolo"       
    elif salon1 == "2":
        salon = "Artemis"       
    elif salon1 == "3":
        salon = "Spuntnik"
    else:
        print("opcion invalida")
        return
        
    print("="*30)  
    print("ingrese el horario")
    print("1. 7-11")
    print("2. 11-15") 
    print("3. 15-19")
    horat= input("ingrese una opcion: ")
    if horat == "1":
        hora="7-11"       
    elif horat == "2":
        hora = "11-15"       
    elif horat == "3":
        hora = "11-15"
    else:
        print("opcion invalida")
        return
        

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
    data["rutas"].append(ruta)
    j.write_json(ARCHIVO_RUTAS, data)
    print("Ruta creada ✅")
    



def listar_rutas():
    data = j.read_json(ARCHIVO_RUTAS)
    rutas = data.get("rutas", [])
    if rutas:
        
        for ruta in rutas:           
                print(f"""ID:{ruta["ID"]}\nmodulos:\n{ruta["data"]["modulos"]}""")
                print("---"*60)
    else :
        print("no hay rutas registrados")            
    

def asignar_camper_a_ruta():
    data = j.read_json(FILE)                
    campers = data.get("campers", [])     
    data = j.read_json(ARCHIVO_RUTAS)
    rutas = data.get("rutas", [])
    if rutas:
        ID_camper=input("ingrese el ID del camper que dedea asignar a la ruta: ")
        ID_ruta= input("ingresar el ID de la ruta: ")
        
        camper_encontrado= None
        ruta_encotrada= None
        
        for camper in campers :
            if camper["ID"]==  ID_camper:
                if camper["datos"]["estado"] == "aprobado":

                    camper_encontrado= camper
                    break
                    
                
        if not camper_encontrado:
                print("error, ID de camper inexistente o ninguno en estado de aprobado") 
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
                j.write_json(ARCHIVO_RUTAS, data) 
                

                


                print("camper asignado con exito")
        else:
            print("capacidad maxima alcanzada")

    else:
        print("no hay rutas registradas")            
