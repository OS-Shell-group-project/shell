
import sys, os


while 1: 
    command = input('% ')

    #print (sys.argv[1:])

    path = os.getcwd() # use .getcwd to get the path of current location

    def getname(path):
        if os.path.isdir(path): 
            folder = os.path.basename(path) #+ ["    "] # use .listdir to list folder's name of current address
            print('Directory name : ' + folder)

        else:
            print("wrong path")
            exit()

    # if __name__ == '__main__':
    #      getname(path)

    def ls():
        for items in os.listdir(path):
            print (items)

    def pwd():
        print(path)

    def cat():
        with open('ab.txt', 'r') as _file:
            _char = _file.read()

        print(_char)

    def head():
        with open('hehe.txt', 'r') as _file:
            for x in range(5):
                print (_file.readline())
                #break



    if command == 'x':
        print('Exiting Shell!')
        break
    elif  command == 'ls':
        ls()
    elif command == 'gn':
        getname(path)
    elif command == 'pwd':
        pwd()
    elif command == 'cat':
        cat()
    elif command == 'head':
        head()
    else:
        print('Invalid Command...try again')