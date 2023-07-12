import os
import core
import random
diccpacient = {"datos":[]}

def LoadInfoPaciente():
    global diccpacient
    if (core.checkFile("pacientes.json")):
        diccpacient = core.LoadInfo("pacientes.json")
    else:
        core.crearInfo("pacientes.json",diccpacient)    

def mainMenu():
    os.system("clear")
    print("\n--- GESTIÓN DE PACIENTES ---")
    print("1. Agregar paciente: ")
    print("2. Buscar paciente: ")    
    print("3. Mostrar información de un paciente: ")
    print("4. Volver al menú principal: ")    
    opcion = int(input(":<"))

    if (opcion == 1):
        Block = False
        for i in diccpacient["datos"]:
            Block = True
            consecutivo = i["id"]
        if Block == True:    
            idactual = int(consecutivo)+1
            idAgregar = str(idactual).zfill(3)
        if Block  == False:
            idAgregar="001"    
            print(idAgregar)
        datos = {
            "id": idAgregar,
            "Nombre": input("Ingrese el nombre Paciente: "),
            "Tipo": "",
            "Edad": int(input("Ingrese la edad del paciente: ")),
            "Nombre_propietario": input("Ingrese el nombre del propietario: "),
            "raza": ""
        }
        diccpacient["datos"].append(datos)
        core.crearInfo("pacientes.json",datos)
    elif (opcion == 2):
        print('+','-'*55,'+')
        print("|{:^16}{}{:^15}|".format(' ','BUSCADOR DE PACIENTE',' '))
        print('+','-'*55,'+')
            
    elif (opcion == 3):
        pass
    elif (opcion == 4):
        pass    