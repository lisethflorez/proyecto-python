import os
import json
import funciones.globales as gf
import modulos.corefiles as cf
import ui.uipacientes as uip
import ui.uimedico as uim

def newmedico():
    title = """"
    ************************
    * REGISTRO DE MEDICOS *
    ************************
    """
    gf.borrar_pantalla()
    print(title)
    identificacion = input ("ingrese el nro de identificacion:")
    nombresmedicos = input("ingrese  el nombre del medico: ")
    apellidomedicos = input("ingrese el apellido del medico:")
    nroconsultorio = input("ingrese el nro del consultorio:")
    correo = input("ingrse su correo:")
    horarioAtecion = input("ingrse la hora:") 
    especialidad= input("ingrse el especialista:")

    medicos = {
        "identificacion": identificacion,
        "nombresmedicos": nombresmedicos,
        "apellidomedicos": apellidomedicos,
        "nroconsultorio": nroconsultorio,
        "correo": correo,
        "horarioAtencion": horarioAtecion,
        "especialidad": especialidad 
    }
    
    cf.AddData('data',identificacion,medicos)
    gf.centromedico.get('data').update({identificacion:medicos})
    if(bool(input('Desea registrar otro medico S(Si) o Enter(No)'))):
        newmedico()
    else:
       uim.Menumedicos(0)
    
def SearchData():
     input('Ingrese el Nro Identificacion del medico: ')
     data=gf.centromedico.get('data')
     return data
    

def ModifyData():
    datamedico=SearchData()
    datamedico= ()
    identificacion,nombremedicos,apellidomedicos,correo,nroconsultorio = datamedico.values()
    for key in datamedico.keys():
        if (key != 'identificacion' and key != 'notas'):
            if(bool(input(f'Desea modificar el {key} s(si) o Enter No'))):
                datamedico[key] = input(f'Ingrese el nuevo valor para {key} :')
    gf.centromedico.get('data').update({identificacion:datamedico})
    cf.UpdateFile(gf.centromedico)
    uim.Menumedicos(0) 

    

        

    
















    