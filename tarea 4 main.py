# PROGRAMA PRINCIPAL

import tarea_4_modulo

fichero = ''

fichero = input('Introduzca fichero con la agenda en formato JSON (si no existe, se creará) Enter para cargar "agenda.json": ')
if fichero == '':
    fichero = 'agenda.json'
    
if tarea_4_modulo.pedir_fichero(fichero) != 1 :    #Si devuelve 1 es que no existe o extension incorrecta
    tarea_4_modulo.carga_agenda(fichero)
    
    opcion=0
    while opcion != '8':
        print("\nOPCIONES:")
        print("---------")
        print("  1: Mostrar Agenda")
        print("  2: Añadir amigos a agenda")
        print("  3: Buscar un amigo en agenda")
        print("  4: Borrar un amigo de la agenda")
        print("  5: Obtener el tiempo de una ciudad")
        print("  6: Obtener el Pronostico del tiempo de una ciudad")
        print("  7: Crear Backup zip de", fichero)
        print("  8: salir")
        opcion = input("Elija opción: ")

        if (opcion == '1'):
            tarea_4_modulo.mostrarAmigos()
        elif (opcion == '2'):
            tarea_4_modulo.añadirAmigos()
        elif (opcion == '3'):
            nombre = input('  **  Introduzca el amigo a buscar: ')
            tarea_4_modulo.buscar_contacto(nombre)
        elif (opcion == '4'):
            tarea_4_modulo.borrar_amigo()
        elif (opcion == '5'):
            tarea_4_modulo.tiempo()
        elif (opcion == '6'):
            tarea_4_modulo.prevision()
        elif (opcion == '7'):
            tarea_4_modulo.copia_seguridad_zip(fichero)
        elif (opcion == '8'):             #se sale
            print('\n  ** Hasta luego Lucas  **  \n')
        else:
            print("\n  ** Opcion incorrecta, repita, please  ** ")

    tarea_4_modulo.guardarAgenda(fichero)
