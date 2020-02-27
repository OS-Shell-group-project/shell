import Input

#
def wc(**kwargs):
    validFlags = ['-l','-w','-m']
    flag = ' '

    if Input.isParamsListEmpty(kwargs['params']):
        return
    
    if not Input.isFlagsListEmpty(kwargs['flags']):
        flag = kwargs['flags'][0]
        if flag not in validFlags:
            print('Unrecognized flags\n')
            return

    lines = []
    words = []
    chars = []
    file = Input.getFullFileName(kwargs['params'][0])

    if file[0]:
        with open(file[1], 'r') as _file:
            for line in _file:
                if line.strip():
                    lines.append(line.strip())

            for line in lines:
                for wds in line.split():
                    words.append(wds)

            for wd in words:
                for ch in wd:
                    chars.append(ch)

    else:
        print(file[1])
        return

    if flag == validFlags[0]:     
        print(str(len(lines)) + ' line(s) in ' + file[1] + '\n')
    elif flag == validFlags[1]:
        print(str(len(words)) + ' words in ' + file[1] + '\n')
    elif flag == validFlags[2]:
        print(str(len(chars)) + ' characters in ' + file[1] + '\n')
    else:
        print(str(len(lines)) + ' ' + str(len(words)) + ' ' + str(len(chars)) + ' ' + '\n')