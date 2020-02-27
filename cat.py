import Input

#
def cat(prnt=True,**kwargs):
    if Input.isParamsListEmpty(kwargs['params']):
        return

    redirectFile = False
    fileList = []
    catFile = ''

    if '>' in kwargs['params'] or '>>' in kwargs['params']:
        redirectFile = Input.getRedirectFile(kwargs['params'])
        indexOfRedirect = kwargs['params'].index(redirectFile[2])
        kwargs['params'] = kwargs['params'][:indexOfRedirect]

    for file in kwargs['params']:
        file = Input.getFullFileName(file)
        if file[0]:
            fileList.append(file)
        else:
            print(file[1])
            return

    # for eachFile in fileList:
    #     if eachFile[0]:
    #         with open(eachFile[1], 'r') as _file:
    #             if prnt:
    #                 print(_file.read())
    #             else:
    #                 return _file.read()
    #     else:
    #         print(eachFile[1])

    for eachFile in fileList:
        with open(eachFile[1], 'r') as _file:
            catFile += _file.read() + '\n'

    if redirectFile:
        newFile = open(redirectFile[0],redirectFile[1])
        newFile.write(catFile)
        newFile.close()
    elif prnt:
        print(catFile)
    else:
        return catFile