import modulos.corefiles as cf
import funciones.globales as gf
import funciones.pacientes as fp
import funciones.medicos as fm
import main

def Menumedicos(op : int):
    title = """
    *******************************************
    *           CENTRO DE MEDICOS       *
    *******************************************
    """
    menumedicosOp = '1.buscar medico\n2.agregar medico \n3.Editar medico\n4. Eliminar\n5. Salir'
    gf.borrar_pantalla()
    if (op != 4):
        print(title)
        print(menumedicosOp)
        try:
            op = int(input(":) "))
        except ValueError:
            print("Opcion no tiene formato adecuado")
            gf.pausar_pantalla()
            menumedicosOp(0)
        else:
            match (op):
                case 1:
                    fm.SearchData()
                case 2:
                    fm.newmedico()
                case 3:
                    fm.ModifyData()
                case 4:
                    Menumedicos(0)
                case _:
                    print("La opcion ingresada no esta disponible en las opciones")
                    gf.pausar_pantalla()

