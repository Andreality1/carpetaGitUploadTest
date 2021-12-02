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



solution()