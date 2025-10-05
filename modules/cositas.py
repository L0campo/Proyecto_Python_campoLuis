import modules.campers as c
import utils.io_jon as j
ARCHIVO_RUTAS = "data/rutas.json"
FILE = "data/campers.json"

j.initialize_json(FILE, {"campers": []})
data = j.read_json(FILE)
campers = data.get("campers", [])



def mostrar_camper():
    data = j.read_json(ARCHIVO_RUTAS)
    rutas = data.get("rutas", [])
    if rutas:
        ID=input ("ingrese el ID de la ruta asignada: ")
        for ruta in rutas:
            if ruta["ID"]== ID :
                print(f"camper:{ruta["data"]["campers"]["ID"]}\n:{ruta["data"]["campers"]["nombre"]}{ruta["data"]["campers"]["apellidos"]}")
                print("-"*60)
    else :
        print("no hay rutas registrados")            
    



def listar_campers_mo_estado():
    
    data = j.read_json(FILE)                
    campers = data.get("campers", [])  
    if campers:
        id=input ("ingrese su ID: ")
        
        for camper in campers:
            if camper ["ID"]== id :
                print(f"""ID: {camper["ID"]}\n
Nombre: {camper["datos"]["nombre"]}\n {camper["datos"]["apellidos"]}\n
Estado: {camper["datos"]["estado"]}""")

                
    else :
        print("no hay campers registrados")  

def listar_campers_mo_ru():
    
    

    data = j.read_json(ARCHIVO_RUTAS)
    rutas = data.get("rutas", [])
    if rutas:
        ID=input ("ingrese su ID: ")
        for ruta in rutas:
            if ruta["data"]["campers"]["ID"]== ID :
                print(f"camper:{ruta["data"]["campers"]["ID"]}\n:{ruta["data"]["campers"]["nombre"]}{ruta["data"]["campers"]["apellidos"]}\n{ruta["data"]["modulos"]}")
                
    else :
        print("no hay rutas registrados")       

def listar_campers_no():
    
    if campers:
        id=input ("ingrese su ID: ")
        
        for camper in campers:
            if camper ["ID"]== id :
                print(f"""ID: {camper["ID"]}\n
Nombre: {camper["datos"]["nombre"]}\n {camper["datos"]["apellidos"]}\n
{camper["datos"]["notas"]}""")
