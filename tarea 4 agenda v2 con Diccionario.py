import os
import json
import zipfile

v = 2.3
# print('Agenda v',v)

lista_contactos = []
fichero_datos = 'agenda_v2.json'
fichero = ''


def mostrar_contacto(contacto):
    for clave,valor in contacto.items():
        print(clave,valor)

def mostrarAmigos():
    global lista_contactos

    print('\n  **  Hay',len(lista_contactos),'contactos')
    print('------------------')
    for contacto in lista_contactos:
        mostrar_contacto(contacto)
        print('------------------')

    input('\n  **  pulse Enter para continuar  **')
    


def añadirAmigos():
    """ Añade amigos y sus datos al diccionario
        Pulsamos Enter '' para terminar
    """
    print('\n  **  Añadiendo amigos a la agenda:\n')

    global lista_contactos
    while True:
        nombre = input('Introduzca el contacto (Enter para terminar) ')
        if nombre == '':
            break
        if buscar_contacto(nombre) == True:
            continue
        
        contacto = {}
        contacto['nombre'] = nombre
        
        email = input('Introduzca el email de '+nombre+' (Enter para omitir) ')
        if email != '':
            contacto['email'] = email

        telefono = input('Introduzca el telefono de '+nombre+' (Enter para omitir) ')
        if telefono != '':
            contacto['telefono'] = telefono
            
        edad_cadena = input('Introduzca la edad de '+nombre+' (Enter para omitir) ')
        if edad_cadena != '':
            contacto['edad'] = int(edad_cadena)
        
        lista_contactos.append(contacto)
        print('  **  Añadido contacto '+nombre)
        print('-------------')
        mostrar_contacto(contacto)
        print('-------------')


def buscar_contacto(nombre):
    global lista_contactos
    for contacto in lista_contactos:
        if contacto['nombre'] == nombre:
            print('  **  El contacto '+nombre+' existe')
            mostrar_contacto(contacto)
            return True
    print('  **  No existe el contacto '+nombre)
    return False
              

def borrar_amigo():
    # Buscamos amigo en agenda y lo borramos

    global lista_contactos

    amigo = input("\n  **  Amigo a buscar y borrar, ojo con las mayusculas y acentos: ")

    for contacto in lista_contactos:
        if contacto['nombre'] == amigo:
            indice = lista_contactos.index(contacto)
            del lista_contactos[indice]
            print('\n  **  Borrado', amigo)
    
    input('\n  **  pulse Enter para continuar  **')


def carga_agenda(fich):

    if fich in os.listdir():
        f = open(fich,'rt',encoding='utf8')
        for linea in f.readlines():
            contacto = json.loads(linea)
            lista_contactos.append(contacto)
        f.close()
        print('  **  Se han recuperado',len(lista_contactos),'contactos')
    else:
        print('  **  No se ha encontrado el fichero', fichero_datos)


def guardarAgenda(fich):
    """ Guardamos la agenda de amigos
        en un fichero de texto en formato ,json
    """
    try:
        f = open(fich,'wt',encoding='utf8')
        for contacto in lista_contactos:
            linea = json.dumps(contacto)+'\n'
            f.write(linea)
        f.close()
        print('  **  Guardados '+str(len(lista_contactos))+' contactos')
    except Exception as e:
        print('  **  ERROR: no se ha podido guardar el fichero',e)

       
def pedir_fichero():
    import os.path
    global fichero
    es_nuevo = False
    
    fichero = input('Introduzca fichero con la agenda en formato JSON (Enter si el fichero es "agenda.json"): ')
    if fichero == '':
        fichero = 'agenda.json'
    
    try:
        f = open(fichero,'rt',encoding="utf8")
        f.close()
    except :
        print("  **  El fichero",fichero, "no existe.")
        crea = input("  **  ¿Desea crearlo? (s/n):")
        if crea.lower() == 's':
            es_nuevo = True 
        else:
            return 1

    nombre_archivo, extension = os.path.splitext(fichero)
    extension=extension.lower()    #la pongo en minusculas, por si...
    
    if extension != '.json':
        print('Extension incorrecta... debe ser .json')
        return 1
    else:   
        if es_nuevo == True :                 #Si es nuevo, solo lo creo, sin backup
            f = open(fichero,'w',encoding="utf8")
            f.close()
        else :                                #Si ya existía, creo backup de la agenda
            nombre2 = nombre_archivo + '_OLD'
            copia_fich = nombre2 + extension
            import shutil
            shutil.copy(fichero, copia_fich)
            print('  **  Creada copia de seguridad de la agenda:', copia_fich)
                

# PROGRAMA PRINCIPAL

if pedir_fichero() != 1 :    #Si devuelve 1 es que no existe o extension incorrecta
    carga_agenda(fichero)
    
    opcion=0
    while opcion != '5':
        print("\nOPCIONES:")
        print("---------")
        print("  1: Mostrar Agenda")
        print("  2: Añadir amigos a agenda")
        print("  3: Buscar un amigo en agenda")
        print("  4: Borrar un amigo de la agenda")
        print("  5: salir")
        opcion = input("Elija opción: ")

        if (opcion == '1'):
            mostrarAmigos()
        elif (opcion == '2'):
            añadirAmigos()
        elif (opcion == '3'):
            nombre = input('  **  Introduzca el contacto a buscar: ')
            buscar_contacto(nombre)
        elif (opcion == '4'):
            borrar_amigo()
        elif (opcion == '5'):             #se sale
            print('\n  ** Hasta luego Lucas  **  \n')
        else:
            print("\n  ** Opcion incorrecta, repita, please  ** ")

    guardarAgenda(fichero)
