#Como se pueden encaminar las cualidades de la mente con tal de producir acciones de caracter mayor, con tal de sintetizar 
#Los aplicativos que mejoran como el componente intelectual se produce, como el comportamiento interno se conduce.
#Como las experiencias de mi saber determinan como yo puedo entender, las realidades que yo quiero vivir.
#Como aprendo a ser mas magico, como yo aprendo a ser mas alto, como yo puedo entender, las verdades que construyen el 
#El proceso que se mueve en mi, el proceso que produce mente, las cualidades que mejoran como mi realidad se 
#conduce a si misma, como el saber promueve como el comportamiento se analiza.



#Como yo puedo conducir mi mente hacia el trabajo del saber.

#Entendiendo como yo puedo hacer para construir el proceso que produce el codigo que yo quiero entender.


#Installa OpenCV

#Comienza una cosa y completala
#Vamos a comenzar

# pip install numpy
# pip install opencv-python




#Comparame dos imagenes y dime si son iguales
#Describe el proceso de como hiciste el objetivo en un articulo.

#El repositorio con el articulo y el programa, el programa corre cuando instales, y lees el articulo.


#Puedo comparar imagenes, y decir si son iguales

#Yo uso los scripts de python para mandar comandos al terminal.
#Esos scripts ejecutan comandos de git.
#Y esos comandos de git, me actualizan la nubecita.
#Me dan la fuerza.
#Fuerza a GitHub, que cualquier archivo que yo actualize en mi repositorio siempre se sube.
#Yo puedo validar si el comando de git se ejecuto de manera correcta.
#Lo siguiente seria que.
#
 
#import pyscreenshot


#Esto lo ejecuto si quiero subirlo a github


import os
import numpy as np

os.system('dir')
pathTesting = os.getcwd()


#os.system('cd d:\\ \ndir')
os.system('dir')




print()
print()
print()

os.chdir('d:\\')
pathTesting = os.getcwd()
print(pathTesting)

#Este comando me manda hacia el directorio Internet
os.chdir('D:\INTERNET\\')

#Este comando me entrega el directorio en el que estoy trabajando
pathDirectory = os.getcwd()
print(pathDirectory)

#Este for me lista todos los subdirectorios del directorio en el que estoy trabajando.
#En forma de string
for i in os.listdir(pathDirectory):
    
    #Este comando me posiciona en el directorio que yo quiero actualizar
    os.chdir(pathDirectory + '\\' + i)
    stringDirectory = os.getcwd()
    print(stringDirectory)

    #Este comando me entrega la lista de los files dentro del directorio que quiero actualizar
    listfileVersion = os.listdir(os.getcwd())

    #Esto me sirve 
    indexFileVersion = 0
    try:
        print("Estas aqui in the try")
        #Este comando sirve para determinar si es error si el archivo no esta
        #Y si si esta se ejucutan los siguientes comandosl.
        #Esto me verifica si el archivo existe
        indexFileVersion = listfileVersion.index('version.txt')
        #Esto abre para sacar data.
    
        f = open("version.txt","r+")
        #Sacas data en forma de string
        stringVersion = f.readline()
        print(stringVersion)


        nameFile = 'version.txt'

        stringDirectoryFile = os.getcwd() + '\\'+ nameFile
        os.remove(stringDirectoryFile)


        #Esto es puro parseo de que?, esto es puro parseo de texto
        #Como yo puedo componer las funciones que nos hacen mas divino.
        #Mero deporte, de golpes al cuerpo.

        listastringVersion = stringVersion.split(' ')
        #Esto es una string que tiene la forma numerica de la version separada por puntos he iniciando por uno
        versionNumerosPuntos = listastringVersion[1]
        listaversionNumeroPuntos = versionNumerosPuntos.split('.')
        lenlistaVersionNumeroPuntos = len(listaversionNumeroPuntos)
        numIncrement = int(listaversionNumeroPuntos[lenlistaVersionNumeroPuntos-1])
        if(numIncrement >= 10000):
            numIncrement2 = int(listastringVersion[lenlistaVersionNumeroPuntos-2])
            numIncrement2 += 1 
            numIncrement = 0


        numIncrement += 1

        #Este comando actualiza, el tipo de data que posicion en la lista ocuapa

        listaversionNumeroPuntos[lenlistaVersionNumeroPuntos-1] = str(numIncrement)
        listToWord =  '.'.join(listaversionNumeroPuntos)
        k = open('version.txt', 'w+')
        logString = os.system('git log -n 1')
        #Este es el mensaje que me permite unir el parseo con la lista que escribe.
        stringVersion = listToWord

        print('HERE IN THE STRING YOU WANT TO SEE')
        print(listastringVersion[0] + stringVersion)
        k.write(listastringVersion[0] + stringVersion)
        k.close()

        #Poner esa palabra en 

    except:
        print('Estas en el except')
        f = open("version.txt","w+")
        f.write("v 1.0.0")
        f.close()
        





    # for i in listfileVersion:
    #     print(i)
    # print(os.getcwd())

    # print(i)
#esto es el directorio
#
stringDirectory = os.getcwd()
print(stringDirectory)
logString = os.system('git log -n 1')
print(logString)


#los parametros que construyen el fundamento que yo quiero promover, la direccion de la mente que me ayuda 
#El tiempo le va da valor.
#Que muchas personas lo sepan manejar
#