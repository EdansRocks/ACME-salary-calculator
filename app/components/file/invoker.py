class FileInvoker:
    def submit(self, command, file_path):
        return command.execute(file_path)
