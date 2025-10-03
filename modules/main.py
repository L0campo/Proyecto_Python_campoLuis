import modules.masseg as m
import modules.camperss as c
import modules.trainers as t
import modules.rutas as r
import modules.areas as a

while True:
    
    opcion=m.logi()

    if opcion == 1:
        opcion1=m.menu_camper()
        match opcion1:

            case 0:
                pass
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass

    elif opcion ==2:
        opcion2=m.menu_trainer()
        match opcion2:
            case 0:
                pass
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass

    elif opcion == 3:
        opcion3=m.menu_admit()
        match opcion3:
            case 0:
                pass
            case 1:
                c.registrar_camper()
                
            case 2:
                t.registrar_trainer()
            case 3:
                pass
            case 4:
                r.crear_ruta()
            case 5:
                a.crear_area()
            case 6:
                pass
            case 7:
                pass

    elif opcion == 0:
        break

    else:
        print ("opcion invalida")

    
