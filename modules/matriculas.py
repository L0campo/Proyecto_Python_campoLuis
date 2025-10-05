import trainers as ti
import rutes as rt

def listar_matriculas():
    print("busqueda de matricula de ")
    opcion = input("¿Desea buscar por ruta (R) o por Trainer (T)? ").upper()

    if opcion == "T":

        t= input("ingrese el ID del trainer encargado: ")
                
        if ti.trainers:
            for trainer in ti.trainers:
                if trainer["ID"]== t:
                    print (f"ID: {trainer['ID']}\nNombre: {trainer['datos']['nombre']}\nRuta: {trainer['datos']['ruta']}\n"
)
        else:
            print("no hay trainers registrados")
    
    
    elif opcion == "R":
        r= input("ingrese el ID de la ruta: ")
        if rt.rutas:
            for trainer in ti.trainers:
                if trainer["datos"]["ruta"]["ID"]== t:
                    print(f"ID: {trainer["datos"]["ruta"]["ID"]}\n Trainer: {trainer["datos"]["nombre"]}\n Ruta: {trainer["datos"]["ruta"]} ")
        else:
            print("no hay rutas registradas")
    else:
        print("opcion invalida")
            
            
    


    

    
def actualizar_matricula(matricula_id, nuevos_datos):
    pass