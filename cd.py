import Input, os

#not yet working
def cd(**kwargs):
    cwd = os.getcwd()
    directoryList = cwd.split('\\')


    if not kwargs['params'] or kwargs['params'][0] == '~':
        directoryList = directoryList[:5]
        cwd = '\\'.join(directoryList)
        os.chdir(cwd)
        return

    if not os.path.exists(cwd + '\\' + kwargs['params'][0]):
        print('directory doesn''t exist\n')
        return

    if kwargs['params'][0] == '..':
        directoryList = directoryList[:-1]
        cwd = '\\'.join(directoryList)
        os.chdir(cwd)
        return
    
    os.chdir(kwargs['params'][0])