from ...common.interface import Command


class ReadUsers(Command):
    def __init__(self, file_receiver):
        self._file_receiver = file_receiver

    def execute(self, file_path):
        return self._file_receiver.read_users(file_path)

    def redo(self, file_path):
        self.execute(file_path)


class FileExists(Command):
    def __init__(self, file_receiver):
        self._file_receiver = file_receiver

    def execute(self, file_name):
        return self._file_receiver.file_exists(file_name)

    def redo(self, file_name):
        self.execute(file_name)
