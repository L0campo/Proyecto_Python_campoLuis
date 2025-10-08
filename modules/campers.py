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
    estado = ("proceso")

    

    
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
        "riesgo":  riesgo,
        "notas" : {
            "nota 0": None,
            "modulo.1": None,
            "modulo.2": None,
            "modulo.3": None,
            "modulo.4": None,
            "modulo.5": None
            
            
        }

    } }
    campers.append(camper)
    u.rewrite_json(FILE, campers, path=["campers"])
    print("✅ El camper fue registrado con éxito")
    




def listar_campers_por_estado():

    data = u.read_json(FILE)                
    campers = data.get("campers", [])  
    if campers:
        for camper in campers:
            
            print("estados")
            print("1.En proceso de ingreso") 
            print("2.inscrito")           
            print("3.aprobado")
            print("4.cursando")
            print("5.graduado")
            print("6.expulsado")
            print("7.retirado")
            estado1=input ("ingrese el estado de buqueda: ")
            if estado1 == "1":
                    estado="proceso"

            elif estado1 == "2":
                    estado="inscrito"
                    
            elif estado1 == "3":
                    estado="aprobado"
                    
            elif estado1 == "4":
                    estado="cursando"
                    
            elif estado1 == "5":
                    estado="graduado"
                    
            elif estado1 == "6":
                    estado="expulsado"
                    
            elif estado1 == "7":
                    estado="retirado"

            else:
                    print("opcion no valido")
                    return


            if camper["datos"]["estado"]== estado :
                u.clear_screen()
                print(f"""ID: {camper["ID"]}\n
Nombre: {camper["datos"]["nombre"]}\n {camper["datos"]["apellidos"]}\n
Estado: {camper["datos"]["estado"]}""")

                print("---"*60)
        
    if not campers:
        print("no hay campers registrados")

                
         
    
    
        

    

def actualizar_estado_camper():
    
    data = u.read_json(FILE)                
    campers = data.get("campers", [])       
    if campers:
        ID=input ("ingrese el ID del camper que desea modificar su estado: ")

        for camper in campers:
            if camper["ID"]== ID :
                print("estados")
                print("1.En proceso de ingreso") 
                print("2.inscrito")           
                print("3.aprobado")
                print("4.cursando")
                print("5.graduado")
                print("6.expulsado")
                print("7.retirado")

    

                new_estado=input("ingrese el nuevo estado")
                if new_estado == "1":
                    estado="proceso"

                elif new_estado == "2":
                    estado="inscrito"
                    
                elif new_estado == "3":
                    estado="aprobado"
                    
                elif new_estado == "4":
                    estado="cursando"
                    
                elif new_estado == "5":
                    estado="graduado"
                    
                elif new_estado == "6":
                    estado="expulsado"
                    
                elif new_estado == "7":
                    estado="retirado"

                else:
                    print("opcion no valido")
                    return
                

                
                camper["datos"]["estado"] = estado
                u.write_json(FILE, {"campers": campers})   
                print("✅ Estado actualizado con éxito")
                    

            else:
                print("no exixten camper con ese ID")   



    else :
        print("no hay campers registrados")

def listar_campers_en_riesgo():
    data = u.read_json(FILE)                
    campers = data.get("campers", [])      
    if campers:
        for camper in campers:
            print("niveles de riesgo")
            print("1.bajo")
            print("2.medio")
            print("3.alto")
            opcion=input("seleccione una opcion: ")
            if opcion == "1":
                riesgo="bajo"
            elif opcion == "2":
                riesgo="medio"
            elif opcion == "3":
                riesgo="alto"
            else:
                print("opcion no valida")

            if camper["datos"]["riesgo"]== riesgo :
                print(f"""\nID: {camper["ID"]}\n
Nombre: {camper["datos"]["nombre"]}\n {camper["datos"]["apellidos"]}\n
riesgo: {camper["datos"]["riesgo"]}""")

                print("---"*60)
    else :
        print("no hay campers registrados")            

def actualizar_riesgo_camper():
    
    data = u.read_json(FILE)
    campers = data.get("campers", [])
    if campers:
        ID=input ("ingrese el ID del camper que desea modificar su nivel de riesgo: ")
        
        for camper in campers:
            if camper["ID"]== ID :
                
                print("niveles de riesgo")
                print("1.bajo")
                print("2.medio")
                print("3.alto")
                opcion=input("seleccione una opcion: ")
                if opcion == "1":
                    new_riesgo="bajo"
                elif opcion == "2":
                    new_riesgo="medio"
                elif opcion == "3":
                    new_riesgo="alto"
                else:
                    print("opcion no valida")
                    return


                
                camper["datos"]["riesgo"]= new_riesgo
                u.write_json(FILE, {"campers": campers}) 
                
                
            else:
                print("no exixten camper con ese ID")   


def actualizar_notas_camper():
    
    data = u.read_json(FILE)                
    campers = data.get("campers", [])       
    if campers:
        ID=input ("ingrese el ID del camper que desea modificar su estado: ")

        for camper in campers:
            if camper["ID"]== ID :
                print("que nota desea modificar?")
                print("1.nota 0")
                print("2.modulo.1")
                print("3.modulo.2")
                print("4.modulo.3")
                print("5.modulo.4")
                print("6.modulo.5")
                opcion=input("seleccione una opcion: ")

                if opcion == "1":
                    nota= float(input("ingrese nota: "))
                    camper["datos"]["notas"]["nota 0" ] = nota
                    u.write_json(FILE, {"campers": campers})   
                    print("✅ nota ingresada con éxito")
                
                elif opcion == "2":
                    nota= float(input("ingrese nota: "))
                    camper["datos"]["notas"]["modulo.1" ] = nota
                    u.write_json(FILE, {"campers": campers})
                    print("✅ nota ingresada con éxito")
                
                elif opcion == "3":
                    nota= float(input("ingrese nota: "))
                    camper["datos"]["notas"]["modulo.2" ] = nota
                    u.write_json(FILE, {"campers": campers})
                    print("✅ nota ingresada con éxito")
                
                elif opcion == "4":
                    nota= float(input("ingrese nota: "))
                    camper["datos"]["notas"]["modulo.3" ] = nota
                    u.write_json(FILE, {"campers": campers})
                    print("✅ nota ingresada con éxito")
                
                elif opcion == "5":
                    nota= float(input("ingrese nota: "))
                    camper["datos"]["notas"]["modulo.4" ] = nota
                    u.write_json(FILE, {"campers": campers})
                    print("✅ nota ingresada con éxito")

                elif opcion == "6":
                    nota= float(input("ingrese nota: "))
                    camper["datos"]["notas"]["modulo.5" ] = nota
                    camper["datos"]["notas"]["modulo.4" ] = nota
                    u.write_json(FILE, {"campers": campers})
                    print("✅ nota ingresada con éxito")
                    
                else:
                    print("opcion no valida")
                    return

                

        if not campers:
            print("no hay campers registrados")

                

def calcular_promedio_notas():

    data = u.read_json(FILE)
    campers = data.get("campers", [])

    for camper in campers:
        notas = camper["datos"].get("notas", [])

        
        notas = [float(n) for n in notas if n != ""]

        if notas:
            promedio = sum(notas) / len(notas)
            camper["datos"]["promedio"] = round(promedio, 2)
        else:
            camper["datos"]["promedio"] = None

    data["campers"] = campers
    u.write_json(FILE, data)
    print("✅ Promedios calculados y guardados en campers.json")