import sys

def displayHelp():
    sys.exit(0)

def processArgs():
    args = sys.argv[:]
    data = {}
    
    if ('h' in args) or ('help' in args) or ('-h' in args) or ('--help' in args):
        displayHelp()
    
    try:
        data['weburl'] = args[1]
    except IndexError:
        displayHelp()
    
    try:
        data['title'] = ' '.join(args[2:])
    except IndexError:
        displayHelp()
    
    try:
        if ('-s' in args) or ('--source' in args):
            data['source'] = True 
        else:
            data['source'] = False
    except:
        pass
    
    print(data)
        
    return data

processArgs()


