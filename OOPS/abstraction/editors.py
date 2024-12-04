from abc import ABC,abstractmethod

class Editor(ABC):

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def write(self):
        pass

    @abstractmethod
    def debug(self):
        pass

    @abstractmethod
    def execute(self):
        pass

class Vscode(Editor):
    def open(self):
        print("vscode open method")

    def write(self):
        print("write")

    def debug(self):
        print("debug")

    def execute(self):
        print("execute")

Vscode_inst=Vscode()
Vscode_inst.open()
Vscode_inst.write()
Vscode_inst.debug()
Vscode_inst.execute()
