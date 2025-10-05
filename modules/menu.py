import modules.message as m 
import modules.campers as c
import modules.trainers as t
import modules.rutes as r


def menu():
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
                    opcionr=m.menu_regisCamper()
                    if opcionr== 1:
                        c.registrar_camper()
                    elif opcionr==2:
                        c.listar_campers_por_estado()
                    elif opcionr==3:
                        c.actualizar_estado_camper()
                    elif opcionr==4:
                        c.listar_campers_en_riesgo()
                    elif opcionr==5:
                        c.actualizar_riesgo_camper()
                    elif opcionr==0:
                        m.menu_admit()
                    else:
                        print("opcion invalida")

                    
                case 2:
                    opcionr=m.menu_registrainer()
                    if opcionr== 1:
                        t.registrar_trainer()
                    elif opcionr==2:
                        t.listar_trainers()
                    elif opcionr==3:
                        t.asignar_ruta_trainer()
                    
                    elif opcionr==0:
                        m.menu_admit()
                        
                    else:
                        print("opcion invalida")

                    
                case 3:
                    pass
                case 4:
                    r.crear_ruta()
                case 5:
                    pass
                case 6:
                    pass
                case 7:
                    pass

        elif opcion == 0:
            break

        else:
            print ("opcion invalida")

        
