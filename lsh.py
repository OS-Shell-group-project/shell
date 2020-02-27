
import Input, os

#
def ls(**kwargs):
    for items in os.listdir(os.getcwd()):
        size=os.path.getsize(items)    
        print (items)#type of paramater, doesn't work if print(items+size)
        print (size)