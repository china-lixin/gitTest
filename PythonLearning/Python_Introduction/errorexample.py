'''

def spm():
    bacon()


def bacon():
    raise Exception('This is a error message!')


# spm()
'''
import traceback
try:
    raise Exception('This is the error message.')
except:
    errorFile = open('errorInfo.txt', 'w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written to errorInfo.txt.')
