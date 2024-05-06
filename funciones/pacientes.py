import os
import json
import funciones.globales as gf
import modulos.corefiles as cf
import ui.uipacientes as uipc
def newpacientes():
    title = """"
    ************************
    * REGISTRO DE PACIENTES *
    ************************
    """
    print(title)
    idpaciente = int(input("ingrese el nro de identificacion:"))
    nombrepaciente = str(input("ingrese  el nombre del aciente: "))
    apellidopaciente =  str (input("ingrese el apellido del paciente:"))
    nrotelefono = int("ingrese el nro de telefono:")
    nrocelular = int("ingrese el nuro de celular:")
    fechadenacimiento = int("ingrese fecha de nacimiento (dd/mm/aa)")
    edad = int("ingrse la edad")
    genero = str(input("ingrese su genero F o M"))
    pacientes ={
        "idpaciente": idpaciente,
        "nombrepaciente": nombrepaciente,
        "apellidopaciente": apellidopaciente,
        "nrotelefono": nrotelefono,
        "nrocelular": nrocelular,
        "fechadenacimiento":fechadenacimiento,
        "edad": edad,
        "genero": genero 

    }

    cf.AddData('data',idpaciente,pacientes)
    gf.centromedico.get('data').update({idpaciente:pacientes})
    if(bool(input('Desea registrar otro pasiente S(Si) o Enter(No)'))):
        newpacientes()
    else:
       uipc.Menupaciente(0)
       