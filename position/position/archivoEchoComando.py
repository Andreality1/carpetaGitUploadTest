 #texto escribiendose en este archivo 
import pyautogui
import sys
 #Estamos detallando una idea la cual poder usar en el contexto que se nos presenta en el momento presente
print(pyautogui.size())



print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')

