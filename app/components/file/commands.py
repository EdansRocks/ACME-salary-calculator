from ...common.interface import Command

class ReadUsers(Command):

    def __init__(self, fileReceiver):
        self._fileReceiver = fileReceiver

    def execute(self, filePath):
        return self._fileReceiver.readUsers(filePath)

    def redo(self, filePath):
        self.execute(filePath)


class FileExists(Command):

    def __init__(self, fileReceiver):
        self._fileReceiver = fileReceiver

    def execute(self, fileName):
        return self._fileReceiver.fileExists(fileName)

    def redo(self, fileName):
        self.execute(fileName)