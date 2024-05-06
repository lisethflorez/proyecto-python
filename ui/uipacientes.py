import funciones.medicos as fm
import modulos.corefiles as cf
import funciones.globales as gf
import funciones.pacientes as fp

 
def menupaciente(op):
    title = """
    
    *********************************
    *    GESTION   DE  PACIENTES    *
    *********************************
    """
    menupacienteOp = '1. buscar pacientes\n2. agregar paciente\n3.editar paciente\n4.eliminar paciente\n5. salir'
    gf.borrar_pantalla()
    if (op !=5):
        print(title)
        print(menupacienteOp)
        try:
           op = int(input(",)") )
        except ValueError:
            print("opcion no tiene formato adecuado")
            gf.pausar_pantalla()
            menupaciente(0)
    match op:
        case 1:
            fp.searchdata
        case 2:
            fp.newpaciente(0)
        case 2:
            fp.modifydata(0)
        case 3:
            pass
        case 4:
            menupacienteOp
        case _:
            print("la opcion no es valida") 
            gf.pausar_pantalla