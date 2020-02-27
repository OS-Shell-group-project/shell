import os
def cd(**kwargs):
    path = os.getcwd()
    parent_path = os.path.dirname(path)
    print (parent_path)