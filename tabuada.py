def tabuada(x):
    tabuada =[]
    for i in range(1, 11):
        tabuada.append(str(x) + ' x ' + str(i) + ' = ' +str(x*i))
    return tabuada

for x in tabuada(2):
    print(x)