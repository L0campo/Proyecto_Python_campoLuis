rutas=[]
def crear_ruta(nombre, modulos, sgdb_principal, sgdb_alternativo):
    programacion=["Java", "JavaScript", "C#"]
    base_de_datos=["Mysql", "MongoDb" , "Postgresql"]
    Backend=["NetCore", "Spring Boot", "NodeJS" , "Express"] 
    
    print("------ Registro de campers ------")

    ID_ruta= input("ingrese el ID de la ruta: ")
    for ruta in rutas:
        if ruta["ID"]== ID_ruta:
            print("ID ya existente")
            return
    
    print("Java, JavaScript, C#")   
    modulo_Programación= ("ingrese un idioma de los presentados")

    print("Mysql, MongoDb ,Postgresql")
    modulo_BasesDeDatos= ("ingrese una base de datos de laa presentadas") 
    

    print("NetCore, Spring Boot, NodeJS , Express")
    modulo_Backend= ("ingrese un baken de los mostrados")

    fundamentos=("Introducción a la algoritmia", "PSeInt" , "Python")
    Web=("HTML","CSS", "Bootstrap")
    modulos=[fundamentos,Web,modulo_Programación,modulo_BasesDeDatos,modulo_Backend]

    ruta = {
        "ID": ID_ruta,
        "modulos" :modulos
    }
        



def listar_rutas():
    pass

def asignar_camper_a_ruta(id_camper, ruta):
    pass