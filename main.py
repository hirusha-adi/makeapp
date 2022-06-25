import sys

def displayHelp():
    sys.exit(0)


class MakeApp:
    def __init__(self) -> None:
        self._args: dict = {}
        self._src_code: str = ""
    
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
