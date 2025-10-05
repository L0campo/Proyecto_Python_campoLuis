import modules.message as m 
import modules.campers as c
import modules.trainers as t
import modules.rutes as r
import modules.matriculas as mat
import modules.repot as rep
import utils.io_jon as u
import modules.cositas as co



def menu():
    while True:
        opcion=m.logi()
        u.clear_screen()
        try: 

            if opcion == 1:
                opcion1=m.menu_camper()
                u.clear_screen()
                match opcion1:

                    case 0:
                        u.clear_screen()
                        m.logi()
                        
                    case 1:
                        co.listar_campers_mo_ru
                        u.pasuar()
                        u.clear_screen()
                        m.menu_camper()
                    case 2:
                        co.listar_campers_no()
                        u.pasuar()
                        u.clear_screen()
                        m.menu_camper()
                    case 3:
                        co.listar_campers_mo_estado
                        u.pasuar()
                        u.clear_screen()
                        m.menu_camper()
                    case _:
                        print("opcion invalida")


            elif opcion ==2:
                opcion2=m.menu_trainer()
                u.clear_screen()
                match opcion2:
                    case 0:
                        m.logi()
                        u.clear_screen()
                    case 1:
                        co.mostrar_camper()
                        u.pasuar()
                        u.clear_screen()
                    case 2:
                        c.actualizar_notas_camper()
                        u.pasuar()
                        u.clear_screen()
                    case 3:
                        c.calcular_promedio_notas()
                        u.pasuar()
                        u.clear_screen()
                    case _:
                        print("opcion invalida")



            elif opcion == 3:
                opcion3=m.menu_admit()
                u.clear_screen()
                match opcion3:

                    case 1:
                        opcionr=m.menu_regisCamper()
                        u.clear_screen()
                        
                        
                        if opcionr== 1:
                            c.registrar_camper()
                            u.pasuar()
                            u.clear_screen()
                            m.menu_admit()
                        elif opcionr==2:
                            c.listar_campers_por_estado()
                            u.pasuar()
                            u.clear_screen()
                        elif opcionr==3:
                            c.actualizar_estado_camper()
                            u.pasuar()
                            u.clear_screen()
                        elif opcionr==4:
                            c.listar_campers_en_riesgo()
                            u.pasuar()
                            u.clear_screen()
                        elif opcionr==5:
                            c.actualizar_riesgo_camper()
                            u.pasuar()
                            u.clear_screen()
                        elif opcionr==0:
                            m.menu_admit()
                            u.clear_screen()
                        else:
                            print("opcion invalida")

                        
                    case 2:
                        opcionr=m.menu_registrainer()
                        u.clear_screen()
                        if opcionr== 1:
                            t.registrar_trainer()
                            u.pasuar()
                            u.clear_screen()
                        elif opcionr==2:
                            t.listar_trainers()
                            u.pasuar()
                            u.clear_screen()
                        elif opcionr==3:
                            t.asignar_ruta_trainer()
                            u.pasuar()
                            u.clear_screen()
                        
                        elif opcionr==0:
                            m.menu_admit()
                            u.clear_screen()
                            
                        else:
                            print("opcion invalida")

                    case 3:
                        opciont=m.menu_regisRuta()
                        u.clear_screen()
                        if opciont== 1:
                            r.crear_ruta()
                            u.pasuar()
                            u.clear_screen()
                        elif opciont==2:
                            r.listar_rutas()
                            u.pasuar()
                            u.clear_screen()
                        elif opciont==0:
                            m.menu_admit()
                            u.pasuar()
                            u.clear_screen()
                        else:
                            print("opcion invalida")

                            
                    case 4:                   
                        opcion0=m.menu_matriculas()
                        u.clear_screen()
                        if opcion0== 1:
                            mat.listar_matriculas()
                            u.pasuar()
                            u.clear_screen()
                        elif opcion0==2:
                            mat.actualizar_matricula()
                            u.pasuar()
                            u.clear_screen()
                        elif opcion0==3:
                            r.asignar_camper_a_ruta()
                            u.pasuar()
                            u.clear_screen()
                        elif opcion0==0:
                            m.menu_admit()
                            u.clear_screen()
                        else:
                            print("opcion invalida")

                        
                    case 5:
                        opcion4=m.menu_repot()
                        u.clear_screen()
                        if opcion4== 1:
                            rep.campers_inscritos_aprobados()
                            u.clear_screen()
                            u.clear_screen()
                        elif opcion4==2:
                            rep.trainers_activos()
                            u.clear_screen()
                            u.clear_screen()
                        elif opcion4==3:
                            rep.campers_bajo_rendimiento()
                            u.clear_screen()
                            u.clear_screen()
                        elif opcion4==0:
                            m.menu_admit()
                            u.clear_screen()
                            u.clear_screen()
                        else:
                            print("opcion invalida")


                            
                    case 0:
                        m.logi()
                        u.clear_screen()

                    case _:
                        print("opcion invalida")




            elif opcion == 0:
                break

            else:
                print ("opcion invalida")
        
        except ValueError: 
            print("erro")
        
