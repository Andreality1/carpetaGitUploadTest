x = 1.6
y = float(-0.32)
y2 = -6.645 
y3 = -14.22
y4 = -24.145
y5 = -37.12
y6 = -52.245
lista = []

listay = [-0.32,-6.645, -14.22,-24.145, -37.12, -52.245]
for i in range(6):

    lista.append(x)
    x += 0.5
    print(lista[i])
print(str(y))


numeroSalida = 0.0
for i in lista:
    numeroSalida += i
sumOfx = numeroSalida


sumOfy = 0.0
for i in listay:
    sumOfy += i


sumOfxpower = 0.0
for i in lista:
    sumOfxpower += (i**2)

print('X = ', sumOfx)
print('Y = ', sumOfy)
print('X^2 = ', sumOfxpower)

sumOfxy = 0.0
for i in range(len(lista)):
    sumOfxy +=  (lista[i] * listay[i])

print('XY = ', sumOfxy) 