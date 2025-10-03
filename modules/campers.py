import utils.io_jon as u

FILE = "data/campers.json"

u.initialize_json(FILE, {"campers": []})
data = u.read_json(FILE)
campers = data.get("campers", [])


def registrar_camper():
    print("------ Registro de campers ------")
    ID = input ("ingrese el ID del camper: ")
    
    for camper in campers:
        if camper["ID"]== ID:
            print("ID ya existente")
            return
    
    camper1 = input ("ingrese el nombre del camper que desea ingresar: ")
    apellidos = input ("ingrese los apellidos del camper: ")
    direcion = input ("ingrse la direccion del camper: ")
    acudiente = input("ingrese el nombre del acudiente del camper: ")
    telefono = input("ingrese el telefono del camper: ")
    figtelefono= input("ingrese el telefono fijo del camper: ")
    estado = ("proceso ")

    

    
    riesgo = "bajo"

    camper ={
        "ID": ID,
        "datos": {
        "nombre": camper1,
        "apellidos" : apellidos,
        "direcion": direcion,
        "acudiente": acudiente,
        "telefono" : {
            "celular": telefono,
            "fijo": figtelefono
        },
        "estado": estado,
        "riesgo":  riesgo

    } }
    campers.append(camper)
    u.rewrite_json(FILE, campers, path=["campers"])
    print("✅ El camper fue registrado con éxito")




def listar_campers_por_estado():

    
    if campers:
        estado=input ("ingrese el estado de buqueda: ")
        for camper in campers:
            if camper["datos"]["estado"]== estado :
                print(f"""ID:{camper["ID"]}\nnombre:{camper["nombre"]} {camper["apellidos"]}\nEstado: {camper["estado"]}""")
                print("-"*60)
            else:
                print("estado inexistente")
    else :
        print("no hay campers registrados")            
    
    
        

    

def actualizar_estado_camper():
    estados=["En proceso de ingreso","proceso de ingreso", "Inscrito", "Aprobado","Cursando"," Graduado", "Expulsado"," Retirado"]
    data = u.read_json(FILE)                
    campers = data.get("campers", [])       
    if campers:
        ID=input ("ingrese el ID del camper que desea modificar su estado: ")
        print(estados)
        for camper in campers:
            if camper["ID"]== ID :

                new_estado=input("ingrese el nuevo estado").lower()

                if new_estado in estados:
                    camper["datos"]["estado"] = new_estado
                    u.write_json(FILE, {"campers": campers})   
                    print("✅ Estado actualizado con éxito")
                    
                else:
                    print("estado no valido") 
            else:
                print("no exixten camper con ese ID")   



    else :
        print("no hay campers registrados")

def listar_campers_en_riesgo():
    
    if campers:
        riesgo=input ("ingrese el estado de buqueda: ")
        for camper in campers:
            if camper["datos"]["riesgo"]== riesgo :
                print(f"""ID: {camper["ID"]}\n
Nombre: {camper["datos"]["nombre"]}\n {camper["datos"]["apellidos"]}\n
Estado: {camper["datos"]["estado"]}""")

                print("-"*60)
    else :
        print("no hay campers registrados")            

def actualizar_riesgo_camper():
    estados=["bajo","medio","alto"]
    data = u.read_json(FILE)
    campers = data.get("campers", [])
    if campers:
        ID=input ("ingrese el ID del camper que desea modificar su nivel de riesgo: ")
        
        for camper in campers:
            if camper["ID"]== ID :
                
                print("niveles de riesgo")
                print("bajo")
                print("medio")
                print("alto")
                new_riesgo=input("ingrese el nuevo nivel de riesgo").lower()

                if new_riesgo in estados:
                    camper["datos"]["riesgo"]= new_riesgo
                    u.write_json(FILE, {"campers": campers}) 
                
                else:
                    print("estado no valido") 
            else:
                print("no exixten camper con ese ID")   