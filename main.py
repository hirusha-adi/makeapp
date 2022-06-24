import sys

def displayHelp():
    pass

def processArgs():
    args = sys.argv[:]
    data = {}
    try:
        weburl = args[1]
    except IndexError:
        displayHelp()
    title = ' '.join(args[2:])
    print(weburl)
    print(title)

processArgs()