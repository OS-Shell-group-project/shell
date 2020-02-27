import os
import shutil

def rmr(**kwargs):
    if os.path.isdir(kwargs['params']) :
        shutil.retree(kwargs['params'])# if it's a path
    elif os.path.isfile(kwargs['params']):
        os.remove(kwargs['params'])#if it's a file
    else:
        print("not avalable to remove")