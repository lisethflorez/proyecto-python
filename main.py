import ui.uipacientes as uipc
import funciones.globales as gf
import modulos.corefiles as cf
import ui.uimedico as uimc
import ui.uicitas as uic


def menuprincipal(op : int):
    title = """
    *******************************************
    *       CENTRO MEDICO CARLOS ARDILA LULLE  *
    *******************************************
    """
    menuStudentOp = '1.gestion medicos\n2.gestion pacientes\n3.gestion citas \n4. Salir'
    gf.borrar_pantalla()
    if (op != 4):
        print(title)
        print(menuStudentOp)
        try:
            op = int(input(":) "))
        except ValueError:
            print("Opcion no tiene formato adecuado")
            gf.pausar_pantalla()
            menuprincipal(0)
        else:
            match (op):
                case 1:
                    uimc.Menumedicos(0)
                case 2:
                    uipc.menupaciente(0)
                case 3:
                    uic.menucitas(0)
                case _:
                    print()
                    gf.pausar_pantalla()
                    menuprincipal
                    
                    
            
if __name__ == '__main__':
    cf.MY_DATABASE = 'data/medicos.json'
    cf.MY_DATABASE = 'data/pacientes.json'
    cf.checkFile(gf.centromedico)
    menuprincipal(0) 
