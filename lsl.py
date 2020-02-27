import Input, os

#
def ls(**kwargs):
    detal='---'
    for items in os.listdir(os.getcwd()):
            if os.R_OK == true and os.W_OK == true and os.X_OK == true:
                detal='rwx'
            elif os.R_OK != true and os.W_OK == true and os.X_OK == true:
                detal='-wx'
            elif os.R_OK == true and os.W_OK != true and os.X_OK == true:
                detal='r-x'
            elif os.R_OK == true and os.W_OK == true and os.X_OK != true:
                detal='rw-'
            elif os.R_OK != true and os.W_OK != true and os.X_OK == true:
                detal='--x'
            elif os.R_OK != true and os.W_OK == true and os.X_OK != true:
                detal='-w-'
            elif os.R_OK == true and os.W_OK != true and os.X_OK != true:
                detal='r--'

        print (items + detal )#type of paramater
        print (os.access(os.getcwd(),os.R_OK))
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
