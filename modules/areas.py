import camperss as c
areas= []
def crear_area():
    
    salon= input ("ingrese el salon selecionado: ")
    hora= input("ingrese la hora inicio: ")
    hora1= input("ingrese la hora fin")

    area={
        "salon": salon,
        "detalles":{
            "hora":hora,
            "horaf":hora1,
            "campers": [],
            "capacidad": 33
            
        }
    }
    areas.append(area)



        


    

def asignar_camper_area():

    ID_camper=input("ingrese el ID del camper que dedea asignar a la ruta: ")
    ID_area= input("ingresar el nombre del salon: ")
    
    camper_encontrado= None
    area_encotrada= None
    
    for camper in c.campers :
        if camper["ID"]==  ID_camper:
            camper_encontrado= camper
            break
            
            
    if not camper_encontrado:
            print("error, ID inexistente") 
            return                  
            
    for area in areas:
        if area["salon"]==  ID_area:
            area_encotrada=area
            break
            

        else:
            print("error, ID de ruta inexistente")
                    
    if len(area_encotrada["detalles"]["campers"]) < area_encotrada["detalles"]["capacidad"]:
            area_encotrada["detalles"]["campers"].append(camper_encontrado)
            

            


            print("camper asignado con exito")
    else:
        print("capacidad maxima alcanzada")
            
    
    

def verificar_capacidad():
        if areas:
            nom =input ("ingrese el area que desea buscar: ")
            for area in areas :
                if area["salon"]== nom :
                    print(f"""salon: {area["salon"]}\n
hora de inicio: {area["detalles"]["hora"]}\n hora final: {area["detalles"]["horaf"]}\n
campers: {area["detalles"]["campers"]}""")
                    print("-"*60)
        else:
            print("no hay areas registradas")        
        
