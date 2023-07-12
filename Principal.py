import os 
import json
import pacientes

if __name__ == "__main__":
    isActive = True
    opcion = 0

    while isActive:
        os.system("clear")
        print("\n--- ADMINISTRACIÓN DEL CENTRO VETERINARIO ---")
        print("1. Gestión de pacientes: ")
        print("2. Gestion de veterinarios:  ")
        print("3. Gestión de citas médicas: ")
        print("4. Salir: ")
        opcion = int(input(":<"))
        if (opcion == 1):
            pacientes.LoadInfoPaciente()
            pacientes.mainMenu()
        elif (opcion == 2):
            pass
        elif (opcion == 3):
            pass
        elif (opcion == 4):
            pass
        elif (opcion == 5):
            pass
        elif (opcion == 6):
            isActive = False
        else:
            print("Opcion no valida....")
            os.system("pause")