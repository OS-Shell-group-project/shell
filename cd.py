import os

def cd(**kwargs):
    #path = os.getcwd()
    #print (path)
    #os.chdir('E:\study')
    #print (kwargs['params'])
    os.chdir(kwargs['params'][0])#type of paramater （E:\study）


    path = os.getcwd()
    print(path)