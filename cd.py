import os

def cd(**kwargs):
    #path = os.getcwd()
    #print (path)
    #os.chdir('E:\study')
    os.chdir(kwargs['params'])#type of paramater

    path = os.getcwd()
    print(path)