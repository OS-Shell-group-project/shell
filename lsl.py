import Input, os

#
def ls(**kwargs):
    detal='---'
    for items in os.listdir(os.getcwd()):
        size=os.path.getsize(items)
        if os.R_OK == True and os.W_OK == True and os.X_OK == True:
            detal='rwx'
        elif os.R_OK != True and os.W_OK == True and os.X_OK == True:
            detal='-wx'
        elif os.R_OK == True and os.W_OK != True and os.X_OK == True:
            detal='r-x'
        elif os.R_OK == True and os.W_OK == True and os.X_OK != True:
            detal='rw-'
        elif os.R_OK != True and os.W_OK != True and os.X_OK == True:
            detal='--x'
        elif os.R_OK != True and os.W_OK == True and os.X_OK != True:
            detal='-w-'
        elif os.R_OK == True and os.W_OK != True and os.X_OK != True:
            detal='r--'

        print (items + "    "+ str(detal) +"    "+ str(size) )#type of paramater
#future implementation
# def ls(**kwargs):
#     directoryItems = []
#     directoryItemsFormatted = ''
#     for items in os.listdir(os.getcwd()):
#         directoryItems.append(items)
        
#     directoryItems.sort(key = len,reverse = True)

#     for items in directoryItems:
#         directoryItemsFormatted += items + '\t'

    #for x in range(5):
    #print(tabulate([['Alice', 24], ['Bob', 19]], headers=['Name', 'Age']))
    #print (directoryItemsFormatted)
