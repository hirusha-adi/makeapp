
import sys

from PySide6.QtCore import QUrl
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Scammer.info')
        self.webEngineView = QWebEngineView()
        self.setCentralWidget(self.webEngineView)
        initialUrl = 'http://scammer.info'
        self.webEngineView.load(QUrl(initialUrl))

def startGUI():
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    availableGeometry = mainWin.screen().availableGeometry()
    mainWin.resize(availableGeometry.width() * 2 / 3, availableGeometry.height() * 2 / 3)
    mainWin.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    startGUI()
