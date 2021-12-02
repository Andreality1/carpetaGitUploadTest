#Lanzar un executable.
#Because and exe file, allow me to define a keyboard shortcut that i can use in order to execute a python program
import pyautogui
#Autogui para tirar clicks
#run the click that enable me to generate a file in the folder im working on 

print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')
print(pyautogui.size())
print(pyautogui.position())

#esto me permite generar executables los cuales transformar en instaladores los cuales correr en la maquina que yo
#Quiera.
#Un instalador es un traductor de las neuronas hacia el cuerpo hacia el materia hacia los transistores hacia las puertas logicas, hacia 
#los circuitos, desde los circuitos, hacia los algoritmos, desde los algoritmos hacia los computadores hacia la entrada y salida, de los pensamientos
#Que quiero hacer materia, de las ideas que yo quiero construir, todos esos proyectos que yo quiero alcanzar, como ser capaz de alcanzar
#El deseo que yo quiero ver hecho realidad.
#Los instaladores son una serie de pasos que buscan reducir las instrucciones de lenguage de alto nivel a un lenguage de bajo de nivel
#Es decir lenguage binario, el cual habilite la serie de reglas que definen en teoria una maquina turing, que corra cualquier programa en el universo

pyautogui.moveTo(100, 200)   # moves mouse to X of 100, Y of 200.
pyautogui.moveTo(None, 500)  # moves mouse to X of 100, Y of 500.
pyautogui.moveTo(600, None)

#
# que yo estoy ejecutando 
#Como yo puedo estar mas concentrado.ay
 

