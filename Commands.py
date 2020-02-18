import sys, os

def getname(path):
    if os.path.isdir(path): 
        folder = os.path.basename(path) #+ ["    "] # use .listdir to list folder's name of current address
        print('Directory name : ' + folder)

    else:
        print("wrong path")
        exit()

#get the fullname of the file (basically adds the extension to it)
def getFullFileName(file):
    for items in os.listdir(os.getcwd()):
        if file == items or file == items.split('.')[0]:
            ffn = [True,items]
            return ffn
        else:
            ffn = [False,'File(s) not found']
    return ffn

def isParamsListEmpty(paramsList):
    if paramsList == []:
        print('file name not provided.')
        return True

def ls(**kwargs):
    for items in os.listdir(os.getcwd()):
        print (items)

def pwd(**kwargs):
    print(os.getcwd())

def cat(**kwargs):
    fileList = []

    if isParamsListEmpty(kwargs['params']):
        return

    for file in kwargs['params']:
        file = getFullFileName(file)
        if file[0]:
            fileList.append(file)
        else:
            print(file[1])
            return

    for eachFile in fileList:
        if eachFile[0]:
            with open(eachFile[1], 'r') as _file:
                print(_file.read())
        else:
            print(file[1])

def head(**kwargs):
    if isParamsListEmpty(kwargs['params']):
        return

    file = getFullFileName(kwargs['params'][0])
    
    if len(kwargs['params']) > 1 and str(kwargs['params'][1]).isdigit():
        noLines = int(kwargs['params'][1])
        noLines = noLines if noLines >= 0 else 5
    else:
        noLines = 5

    if file[0]:
        with open(file[1], 'r') as _file:
            for x in range(noLines):
                print (_file.readline())
    else:
        print(file[1])

#not yet working
def cd(**kwargs):
    if len(kwargs['params']) == 0:
        print('Directory name not provided')
        return
    
    os.chdir(kwargs['params'])
    path = os.getcwd()
    print(path)

def mkdir(**kwargs):
    if len(kwargs['params']) == 0:
        print('Directory name not provided')
        return

    directory = ' '.join(kwargs['params'])

    directoryPath = os.path.join(os.getcwd(),directory)

    if os.path.isdir(directoryPath):
        print('Directory already exists')
        return
    else:
        os.mkdir(directoryPath)

    print('"' + directory + '" has been created.')
        
def rm(**kwargs):
    if isParamsListEmpty(kwargs['params']):
        return

    file = getFullFileName(kwargs['params'][0])

    if file[0]:
        filePath = os.getcwd() + '\\'+ file[1]
    else:
        print(file[1])
        return
    
    print('deleting file...........')
    os.remove(filePath)
    print(file[1] + ' successfully deleted!')

def exit(**kwargs):
    print('Exiting Shell!')
    sys.exit(0)