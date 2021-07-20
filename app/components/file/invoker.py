
class FileInvoker:

    def submit(self, command, filePath):
        return command.execute(filePath)