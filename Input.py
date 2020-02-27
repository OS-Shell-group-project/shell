import sys, os
#from tabulate import tabulate

def getname(path):
    if os.path.isdir(path): 
        folder = os.path.basename(path) #+ ["    "] # use .listdir to list folder's name of current address
        print('Directory name : ' + folder)

    else:
        print("wrong path")
        exit()

#get the fullname of the file (basically adds the extension to it)
def getFullFileName(file):
    cwd = getCwd(file)
    
    if '/' in file:
        fileName = file.split('/')[-1]
    else:
        fileName = file

    if not os.path.exists(cwd):
        ffn = [False,'Path not found\n']
        return ffn
        
    for items in os.listdir(cwd):
        if (fileName == items.lower() or fileName == items.split('.')[0].lower()) and items.split('.')[1] != 'pyc':
            ffn = [True,cwd + '/' + items]
            return ffn
        else:
            ffn = [False,'File(s) not found\n']
    return ffn

def getCwd(dr):
    cwd = os.getcwd()

    if '/' in dr:
        wd = dr.split('/')
        del wd[-1]

        cwd = './'
        for d in wd:
            cwd += d +'/'
    return cwd

def isParamsListEmpty(paramsList,minNumParams=1):
    if paramsList == [] or len(paramsList) < minNumParams:
        print('file name not provided.')
        return True

def isFlagsListEmpty(flagsList):
    if flagsList == []:
        print('flag(s) not provided.')
        return True
    else:
        return False


def recordHistory(command):
    if not os.path.isfile('historyList.txt'):
        with open("historyList.txt",'w') as createHistoryFile:
            createHistoryFile.writelines('0:Command History File\n')
            createHistoryFile.writelines('1:' + command + '\n')
    else:
        with open("historyList.txt") as readHistory:
            cmdHistory = readHistory.readlines()
        lastCommand = cmdHistory[-1]

        lastCommandNumber = int(lastCommand.split(':')[0])
        lastCommandNumber += 1

        writeToHistory = open("historyList.txt","a")
        writeToHistory.writelines(str(lastCommandNumber) + ':' + command + '\n')
        writeToHistory.close()

def getRedirectFile(params):
    if '>' in params:
        mode = 'w'
        modeDirection = '>'
    if '>>' in params:
        mode = 'a'
        modeDirection = '>>'
    return [params[-1],mode,modeDirection]