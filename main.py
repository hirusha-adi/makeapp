import sys, os
from termcolor import colored

def displayHelp():
    print(colored(text="Good Bye!", color='blue'))
    sys.exit(0)


class MakeApp:
    def __init__(self) -> None:
        self._args: dict = {}
        self._src_code: str = ""
    
    def green(self, text: str):
        print(
            colored(
                text="[", 
                color='green'
            ),
            end=""
        )
        print("+", end="")
        print(
            colored(
                text="]", 
                color='green'
            ),
            end=""
        )
        print(
            colored(
                text=" " + text, 
                color='green'
            ),
            end="\n"
        )
    
    def red(self, text: str):
        print(
            colored(
                text="[", 
                color='red'
            ),
            end=""
        )
        print("!!", end="")
        print(
            colored(
                text="]", 
                color='red'
            ),
            end=""
        )
        print(
            colored(
                text=" " + text, 
                color='red'
            ),
            end="\n"
        )
    
    def yellow(self, text: str):
        print(
            colored(
                text="[", 
                color='yellow'
            ),
            end=""
        )
        print("*", end="")
        print(
            colored(
                text="]", 
                color='yellow'
            ),
            end=""
        )
        print(
            colored(
                text=" " + text, 
                color='yellow'
            ),
            end="\n"
        )

    def processArgs(self) -> dict:
        sys_args = sys.argv[:]
        data = {}
        
        if ('h' in sys_args) or ('help' in sys_args) or ('-h' in sys_args) or ('--help' in sys_args):
            displayHelp()
        
        try:
            data['weburl'] = sys_args[1]
        except IndexError:
            displayHelp()
        
        try:
            data['title'] = ' '.join(sys_args[2:])
        except IndexError:
            displayHelp()
        
        try:
            if ('-s' in sys_args) or ('--source' in sys_args):
                data['source'] = True 
            else:
                data['source'] = False
        except:
            pass
        
        self._args = data
            
        return data

    def buildSourceCode(self) -> str:
        self._src_code = f"""import sys

from PySide6.QtCore import QUrl
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('{self._args["title"]}')
        self.webEngineView = QWebEngineView()
        self.setCentralWidget(self.webEngineView)
        initialUrl = '{self._args["weburl"]}'
        self.webEngineView.load(QUrl(initialUrl))

def startGUI():
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    availableGeometry = mainWin.screen().availableGeometry()
    mainWin.resize(availableGeometry.width() * 2 / 3, availableGeometry.height() * 2 / 3)
    mainWin.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    startGUI()""" 

        return self._src_code

    def run(self) -> None:
        self.processArgs()
        self.buildSourceCode()
    
        source_code_file: str = os.path.join(
            os.getcwd(),
            '_'.join(str(self._args["title"]).split(' ')) + '.py'
        )

        if os.path.isfile(source_code_file):
            os.remove(source_code_file)
            
        with open(source_code_file, "w", encoding="utf-8") as _make_file:
            _make_file.write(self._src_code)

        self.green('Created the source code file')


if __name__ == "__main__":
    obj = MakeApp()
    obj.run()