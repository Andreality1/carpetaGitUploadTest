import os

#Estamos sacando componente tras componente en forma de contenido divino.

def solution():

    booleanoGo_1 = True
    while(booleanoGo_1):
            #Que vamos a hacer?
            #que vamos a emprender
            #
            #
            #
        if(booleanoGo_1 == True):
            print('do yo want to ask to execute system commands from python running script')
            print('1 to write link:')
            print('0 to exit():')
            booleanoGo_2 = True
            booleanoData = False
            while(booleanoGo_2):
                try:
                    entrada = int(input())
                    if(entrada == 1):
                        booleanoData = True
                        booleanoGo_2 = False
                    elif(entrada == 0):
                        booleanoGo_2 = False
                        booleanoGo_1 = False
                except:
                    print('except booleanoGo_2')



            if(booleanoData == True):

                booleanoGo_3 = True

                while(booleanoGo_3):
                    try:
                        print('Write CMD COMMAND')
                        stringIn_1 = input()
                        os.system(stringIn_1)
                        booleanoGo_3 = False
                        
                    except:
                        print("except booleanoGo_3")
                    #A donde me mandas
                    #al siguiente concepto
                    #
                    #
                    #
                                
    return 0


variableDirectorio = 'D:\INTERNET\Wiki-Andresito-01\\'
os.chdir(variableDirectorio)
directoryCWD = os.getcwd()
print(directoryCWD)

listFilesGit = os.listdir(directoryCWD)

booleanoGo_1 = True
while(booleanoGo_1):
    
    try:

        indexVersion = listFilesGit.index('version.txt')
        nameFileString = "version.txt"
        f = open(nameFileString,"r+")

        dataStringFile = f.readline()

        stringDirectoryFile = variableDirectorio + '\\' + nameFileString

        os.remove(stringDirectoryFile)

        
        listastringVersion = dataStringFile.split(' ')
        #Esto es una string que tiene la forma numerica de la version separada por puntos he iniciando por uno
        versionNumerosPuntos = listastringVersion[1]
        listaversionNumeroPuntos = versionNumerosPuntos.split('.')
        lenlistaVersionNumeroPuntos = len(listaversionNumeroPuntos)
        numIncrement = int(listaversionNumeroPuntos[lenlistaVersionNumeroPuntos-1])
        if(numIncrement >= 150):
            numIncrement2 = int(listastringVersion[lenlistaVersionNumeroPuntos-2])
            numIncrement2 += 1 
            numIncrement = 0


        numIncrement += 1

        #Este comando actualiza, el tipo de data que posicion en la lista ocuapa

        listaversionNumeroPuntos[lenlistaVersionNumeroPuntos-1] = str(numIncrement)
        listToWord =  '.'.join(listaversionNumeroPuntos)
        
        #Este variable es una string con el numero de la versin
        
        stringVersion = listToWord
        stringOutCommit = listastringVersion[0] + stringVersion

        k = open('version.txt', 'w+') 
        
        os.system('git init')
        os.system('git add .')
        os.system('git commit -m "'+ stringOutCommit + "\"")
        os.system('git push -u origin main')


        print('HERE IN THE STRING YOU WANT TO SEE')

        print(stringOutCommit)
        print(listastringVersion[0] + stringVersion)
        k.write(listastringVersion[0] + stringVersion)

        k.close()

        #Por que no colocar el link del repositorio en el txt
        #porque esa es el puntero mio, esa es la forma de yo mirar en memoria que se ha creado
        #esa es la forma en que yo se que estoy trabajando sobre un contexto
        #Es la forma que me permite detallar las rutas en pro hacia el desarrollo del contexto
        #que yo estoy haciendo verdad
        #es el movimiento que define la accion de mi persona.
        #Es el punto donde el error se soluciona con el error
        #Es esa caracteristica que permite que el fallo no exista




    except:
        print('Estas en el except')
        f = open("version.txt","w+")
        f.write("Version 1.0.0")
        f.close()
        os.system('git init')
        stringIn = input()  
        os.system('git remote add origin '+ stringIn)
                    


