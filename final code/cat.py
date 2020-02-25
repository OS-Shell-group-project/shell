import Input

#
def cat(**kwargs):
    if isParamsListEmpty(kwargs['params']):
        return

    fileList = []

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