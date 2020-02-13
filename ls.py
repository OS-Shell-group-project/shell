#import sys
import os
path = os.getcwd() # use .getcwd to get the path of current location

def getname(path):
    if os.path.isdir(path): 
        filder = os.listdir(path) + ["    "] # use .listdir to list filder's name of current address
        return filder

    else:
        print("wrong path")
        exit()
