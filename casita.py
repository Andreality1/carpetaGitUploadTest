import os

print('os.getcwd()')

os.chdir('d:\internet\wiki-andresito-01\\')
print(os.getcwd())

""" os.system('git commit -m "')

mensaje = 'Version 1.0.0'
os.system('git commit -m "'+ mensaje + "\"")
 """
print(os.listdir(os.getcwd()))


nameFileString = "version.txt"
f = open(nameFileString,"r+")

dataStringFile = f.readline()

stringDirectoryFile = os.getcwd() + '\\' + nameFileString

f.close()

os.remove(stringDirectoryFile)

print(os.listdir(os.getcwd()))