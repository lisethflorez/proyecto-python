import modulos.corefiles as cf
import funciones.globales as gf
import funciones.pacientes as fp
import funciones.citas as fc
import funciones.medicos as fm
import ui.uicitas as uic
def menucitas(op : int):

    title = """
    ************************
    *   GESTION DE CITAS   *
    ************************
    """
    menucitasOP = '1.Buscar citas\n2.agendar citas \3.ediatar\4.eliminar citas\n5. salir'
    gf.borrar_pantalla
    if (op != 4):
        print(title)
        print(menucitasOP)
        try:
            op = int(input(":) "))
        except ValueError:
            print("Opcion no tiene formato adecuado")
            gf.pausar_pantalla()
            menucitasOP(0)
        else:
            match (op):
                case 1:
                    fc.SearchData()
                case 2:
                    fc.newcita()
                case 3:
                    fc.ModifyData()
                case 4:
                    pass
                case 5:
                    menucitas()
                case _:
                    print("La opcion ingresada no esta disponible en las opciones")
                    gf.pausar_pantalla()

