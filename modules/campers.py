campers= []


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
    estado = input("ingrese el estado del camper (En proceso de ingreso o Inscrito): ").lower()

    if estado == "en proceso de ingrso" and estado == "proceso de ingreso":
        estado = "en proceso"

    elif estado == "inscrito":
        estado = "inscrito"

    else:
        print("ingrese un estado valido")
    
    riesgo = "bajo"

    camper ={
        "ID": ID,
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

    }
    campers.append(camper)

    print ("el camper fue registrado con exito")



def listar_campers_por_estado():

    
    if campers:
        estado=input ("ingrese el estado de buqueda: ")
        for camper in campers:
            if camper["estado"]== estado :
                print(f"""ID:{camper["ID"]}\nnombre:{camper["nombre"]} {camper["apellidos"]}\nEstado: {camper["estado"]}""")
                print("-"*60)
    else :
        print("no hay campers registrados")            
    
    
        

    

def actualizar_estado_camper():
    estados=["En proceso de ingreso","proceso de ingreso", "Inscrito", "Aprobado","Cursando"," Graduado", "Expulsado"," Retirado"]
    if campers:
        ID=input ("ingrese el ID del camper que desea modificar su estado: ")
        
        for camper in campers:
            if camper["ID"]== ID :

                new_estado=input("ingrese el nuevo estado").lower()

                if new_estado in estados:
                    camper["estado"]= new_estado
                
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
            if camper["riesgo"]== riesgo :
                print(f"""ID:{camper["ID"]}\nnombre:{camper["nombre"]} {camper["apellidos"]}\nriesgo: {camper["riesgo"]}""")
                print("-"*60)
    else :
        print("no hay campers registrados")            

def actualizar_riesgo_camper():
    estados=["bajo","medio","alto"]
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
                    camper["riesgo"]= new_riesgo
                
                else:
                    print("estado no valido") 
            else:
                print("no exixten camper con ese ID")   