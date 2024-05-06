import os
import json
import funciones.globales as gf
import modulos.corefiles as cf
import ui.uicitas as uict
def newcita():
    title ="""
    **************************
    *     AGENDAR CITAS      *
    **************************
    """
    gf.borrar_pantalla()
    print(title)
    identificacion = input("ingrese la identificacion :" )
    nom_apell = input("ingrese nombre y apellidos : ")
    especialista = input("ingrese el especialista : ")
    correo = input("ingrese su correo eletronico : ")
    fecha = input(" ingrese el DD/MM/AAAA : ")

    cita = {
        'identificacion': identificacion,
        'nombre y apellido': nom_apell,
        'especialista': especialista,
        'correo': correo,
        'fecha': fecha
    }
    cf.AddData('data',identificacion,cita)
    gf.centromedico.get('data').update({identificacion:cita})
    if(bool(input("desea agendar otra cita s(si) enter ( no)"))):
        newcita()
    else:
        uict.menucitas(0)

def SearchData():
     input('Ingrese el Nro Identificacion del paciente: ')
     data=gf.centromedico.get('data')
     return data

def ModifyData():
    datacita=SearchData()
    identificacion,nom_apell,correo,fecha,especialista = datacita.values()
    for key in datacita.keys():
        if (key != 'identificacion' and key != 'notas'):
            if(bool(input(f'Desea modificar el {key} s(si) o Enter No'))):
                datacita[key] = input(f'Ingrese el nuevo valor para {key} :')
    gf.centromedico.get('data').update({identificacion:datacita})
    cf.UpdateFile(gf.centromedico)
    uict.menucitas(0) 