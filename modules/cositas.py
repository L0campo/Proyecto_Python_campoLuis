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
                for camper in ruta["data"]["campers"]:
                    print(f"Camper: {camper['ID']} - {camper['datos']['nombre']} {camper['datos']['apellidos']}")
                print("-" * 60)
                    
                    
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
            for camper in ruta["data"]["campers"]:
                if camper["ID"] == ID:
            
                    print(f"""
ID: {camper['ID']}
Nombre: {camper['datos']['nombre']} {camper['datos']['apellidos']}
Módulos: {ruta['data']['modulos']}
Ruta: {ruta['ID']} (Salón: {ruta['data']['area']['salon']}, Horario: {ruta['data']['area']['hora']})
""")
                    encontrado = True
        if not encontrado:
            print("❌ Ese camper no está asignado a ninguna ruta.")        
    else :
        print("no hay rutas registrados")       

def listar_campers_no():
    
    data = j.read_json(FILE)                
    campers = data.get("campers", [])  
    if campers:
        id=input ("ingrese su ID: ")
        
        for camper in campers:
            if camper ["ID"]== id :
                print(f"""ID: {camper["ID"]}\n
Nombre: {camper["datos"]["nombre"]}\n {camper["datos"]["apellidos"]}\n
{camper["datos"]["notas"]}""")
                
        
    else :
        print("no hay campers registrados")
