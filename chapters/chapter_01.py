# ESCRITURA Y LECTURA DE DATOS EN FICHEROS
input('Please enter your name: ')

myName = input('Please enter your name: ')
print(myName)

file = open('file.txt', mode='w')
file.write(myName)
file.close()

file = open('file.txt', mode='r')
file.read()
file.close()

# LISTAS DE DATOS
myList0 = ['Dennis', 'Ken', 'Richard']
myList1 = [3, 5, 27]
myList2 = ['Hola', 3.14, True, ['Otra lista!', False, 3]]
