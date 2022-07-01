import sys
import os
import shutil
from termcolor import colored


def displayHelp():
    print(colored(text="Good Bye!", color='magenta'))
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

    def blue(self, text: str):
        print(
            colored(
                text="[",
                color='cyan'
            ),
            end=""
        )
        print("-", end="")
        print(
            colored(
                text="]",
                color='cyan'
            ),
            end=""
        )
        print(
            colored(
                text=" " + text,
                color='cyan'
            ),
            end="\n"
        )

    def magenta(self, text: str):
        print(
            colored(
                text="[",
                color='magenta'
            ),
            end=""
        )
        print("-", end="")
        print(
            colored(
                text="]",
                color='magenta'
            ),
            end=""
        )
        print(
            colored(
                text=" " + text,
                color='magenta'
            ),
            end="\n"
        )

    def processArgs(self) -> dict:
        sys_args = sys.argv[:]
        data = {}

        if ('h' in sys_args) or ('help' in sys_args) or ('-h' in sys_args) or ('--help' in sys_args):
            displayHelp()

        try:
            if ('-s' in sys_args) or ('--source' in sys_args):
                data['source'] = True
            else:
                data['source'] = False
        except:
            pass

        try:
            data['weburl'] = sys_args[1]
        except IndexError:
            displayHelp()

        try:
            data['title'] = ""
            for arg in sys_args[2:]:
                if not(arg in ('help', 'h', '-h', '--help', '-s', '--source')):
                    data['title'] += f"{arg} "
        except IndexError:
            displayHelp()

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

        filename = ""
        if len(str(self._args["title"]).split(' ')) > 1:
            filename = str(self._args["title"]).strip() + '.py'
        else:
            filename = '_'.join(
                str(self._args["title"]).split(' ')).strip() + '.py'

        base_path = os.getcwd()
        source_code_file = os.path.join(base_path, filename)

        self.blue(f'Using filename: {source_code_file}')

        try:
            if os.path.isfile(source_code_file):
                os.remove(source_code_file)
                self.green(f'Removed existing file at {source_code_file}')
        except:
            self.red(f'Unable to remove the existing file {source_code_file}')

        try:
            with open(source_code_file, "w", encoding="utf-8") as _make_file:
                _make_file.write(self._src_code)
                self.green(
                    f'Created the file with source code at {source_code_file}')
        except:
            self.red(
                f'Unable to create the file with source code at {source_code_file}')

        if self._args['source']:
            print(colored(text="Good Bye!", color='magenta'))
            sys.exit(0)

        self.blue('Checking for dependencies')
        try:
            from PySide6.QtCore import QUrl
            from PySide6.QtWebEngineWidgets import QWebEngineView
            from PySide6.QtWidgets import QApplication, QMainWindow
            self.green('Dependencies are installed!')
        except:
            self.blue('Installing required dependencies to coompile')
            os.system('py -m pip install PySide6 PyInstaller -U' if os.name ==
                      'nt' else 'python3 -m pip install PySide6 PyInstaller -U')
            self.green('Installed dependencies')

        compile_folder = os.path.join(base_path, 'compile')
        self.blue(f'Using folder: {compile_folder} to compile')
        if not(os.path.isdir(compile_folder)):
            os.makedirs(compile_folder)
            self.green('Created folder')
        dst = os.path.join(compile_folder, filename)
        if os.path.isfile(dst):
            os.remove(dst)
            self.green(f'Removed existing file at {source_code_file}')
        shutil.copy(src=source_code_file, dst=dst)
        self.green(f'Copied file from {source_code_file} to {dst}')
        os.chdir(compile_folder)
        self.green(f"Changed current working directory to {compile_folder}")
        self.blue(
            f'Starting to compile {filename} with filename of "{filename[:-3]}"')
        command = "py -m " if os.name == 'nt' else 'python3 -m '
        command += 'PyInstaller '
        command += ''


if __name__ == "__main__":
    obj = MakeApp()
    obj.run()
