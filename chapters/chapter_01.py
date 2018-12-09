input('Please enter your name: ')

my_name = input('Please enter your name: ')

file = open('file.txt', mode='w')
file.write(my_name)
file.close()

file = open('file.txt', mode='r')
file.read()
file.close()