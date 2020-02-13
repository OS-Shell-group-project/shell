#import sys
import os
path = os.getcwd()

def getname(path):
    if os.path.isdir(path):
        filder = os.listdir(path) + ["    "]
        return filder

    else:
        print("wrong path")
        exit()
