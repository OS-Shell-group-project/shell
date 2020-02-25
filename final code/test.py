#!/usr/bin/env python3
import sys, os
from CommandHelper import CommandHelper

def getname(path):
    if os.path.isdir(path): 
        folder = os.path.basename(path) #+ ["    "] # use .listdir to list folder's name of current address
        print('Directory name : ' + folder)

    else:
        print("wrong path")
        exit()

# if __name__ == '__main__':
#      getname(path)

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

def pwd():
    print(path)

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

def cd():
        os.chdir('E:/study')
        path = os.getcwd()
        print(path)
        
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


ch = CommandHelper(ls,cat,head,rm,exit)

while 1: 
    command_input = input('% ')

    command = command_input.split()[0]

    cmd_params = command_input.split()[1:]

    # if command exists in our shell
    if ch.exists(command):
        ch.invoke(cmd=command, params=cmd_params, thread=False)
    else:
        print("Error: command %s doesn't exist." % (command))

    path = os.getcwd() # use .getcwd to get the path of current location