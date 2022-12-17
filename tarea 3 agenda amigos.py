# agenda v2
# guardar una lista de amigos y telefonos

#Parametros globales
lista_amigos = []
lista_telefonos = []
fichero = ''


def mostrarAmigosYtelefonos():
    """ Muestra todos los amigos y sus telefonos
        Utiliza las variables globales lista_telefonos etc
    """
    global lista_amigos, lista_telefonos
    print('\nLista de amigos y telefonos') # \n = salto de linea
    print('--------------------------')
    for i in range (len(lista_amigos)):
        print(lista_amigos[i],':',lista_telefonos[i])
    input('\n  **  pulse Enter para continuar  **')

def añadirAmigos():
    """ Añade amigos y sus telefonos a la lista
        Pulsamos Enter '' para terminar
    """
    print('\n  **  Añadiendo amigos a la agenda:\n')
    while True:
        amigo = input('Nombre del amigo: (Enter para terminar) ')
        if amigo == '':
            break  # salimos del bucle
        if amigo in lista_amigos:
            print('  **  ',amigo,'ya esta en la lista, repita.')
            continue # volvemos a empezar el bucle

        lista_amigos.append(amigo)
        telefono = int(input('Teléfono de ' + amigo+': '))
        lista_telefonos.append(telefono)
        print('  **  Ahora tienes', len(lista_amigos), 'amigos')


def guardarAgenda(fich):
    """ Guardamos la agenda de amigos y telefonos
        en un fichero de texto en formato CSV
        Cada linea tendra nombre;telefono
    """
    f = open(fich,'wt', encoding="utf8")
    
    for i in range (len(lista_amigos)): # range(0,len(..),1)
        linea = lista_amigos[i] + ';' + str(lista_telefonos[i]) + '\n'
        f.write(linea)
    
    f.close()


def buscar_amigo():
    # Buscamos amigo en agenda y devolvemos indice
    amigo = input("\n  **  Amigo a buscar, ojo con las mayusculas y acentos: ")
    if amigo in lista_amigos:
        indice = lista_amigos.index(amigo)
        print('  **  ',lista_amigos[indice], ':', lista_telefonos[indice], "  (está en la posición", indice, 'y aparece', lista_amigos.count(amigo), 'veces)')        
    else:
        print("  **  Este amigo aun no esta en la agenda")

    input('\n  **  pulse Enter para continuar  **')
              

def borrar_amigo():
    # Buscamos amigo en agenda y lo borramos
    amigo = input("\n  **  Amigo a buscar y borrar, ojo con las mayusculas y acentos: ")
    if amigo in lista_amigos:
        indice = lista_amigos.index(amigo)
        del lista_amigos[indice]
        del lista_telefonos[indice]
        print("  **  Eliminado",amigo, "de la agenda")

    else:
        print("  **  Este amigo aun no esta en la agenda")

    input('\n  **  pulse Enter para continuar  **')


def carga_agenda(fich):
    """ carga datos:
    """
    f = open(fich,'rt',encoding="utf8")
    numero_lineas = 0
    for linea in f.readlines():
        try:  # por si hay algun error en el formato
            valores=linea.split(';')  # divido la linea por ";"
            nombre= valores[0]        # 1º nombre
            telefono = int(valores[1])    # 2º telefono
            lista_amigos.append(nombre)
            lista_telefonos.append(telefono)
            numero_lineas += 1
        except:
            print('Error recuperando linea:',linea)
    f.close()
    print('\n  **  Actualmente tienes',numero_lineas,'amigos en tu agenda')

    
       
def pedir_fichero():
    import os.path
    global fichero
    
    fichero = input('Introduzca fichero con la agenda en formato CSV (Enter si el fichero es "agenda.csv"): ')
    if fichero == '':
        fichero = 'agenda.csv'
    
    try:
        f = open(fichero,'rt',encoding="utf8")
        f.close()
    except :
        print("  **  El fichero",fichero, "no existe.")
        crea = input("  **  ¿Desea crearlo? (s/n):")
        if crea.lower() == 's':
            f = open(fichero,'w',encoding="utf8")
            f.close()
        else:
            return 1

    nombre_archivo, extension = os.path.splitext(fichero)
    extension=extension.lower()    #la pongo en minusculas, por si...
    
    if extension != '.csv':
        print('Extension incorrecta... debe ser .csv')
        return 1
    else:   #Creo backup de la agenda
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
            mostrarAmigosYtelefonos()
        elif (opcion == '2'):
            añadirAmigos()
        elif (opcion == '3'):
            buscar_amigo()
        elif (opcion == '4'):
            borrar_amigo()
        elif (opcion == '5'):             #se sale
            print('\n  ** Hasta luego Lucas  **  \n')
        else:
            print("\n  ** Opcion incorrecta, repita, please  ** ")

    guardarAgenda(fichero)
