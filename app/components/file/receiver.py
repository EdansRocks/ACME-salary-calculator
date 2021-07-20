import os.path


class File:
    def file_exists(self, file_name):
        """
        FE - Check if a file exists on public/data (FILES_PATH) folder
        param fileName: String - Name of the txt file
        return: Boolean - True if file exists otherwise False
        """
        exists = os.path.isfile(file_name) or os.path.isfile(file_name + ".txt")
        return exists

    def read_users(self, file_path):
        """
        RU - Read specific file of employees and returns an array of them
        param filePath: String - Path where the txt file with the employee information is located
        return: Array - An array with the users list
                None if find an error format in file
        """
        try:
            file = open(file_path, "r")
            users = []
            for line in file:
                text = line.strip().split("=")
                name = text[0]
                days = self.__split_worked_days(text[1])
                user = [name, days]
                users.append(user)

            file.close()
            return users

        except:
            file.close()
            return

    def __split_worked_days(self, worked_days):
        """
        Split the worked days as an string into an array
        param workedDays: String - Worked days info
        return: Array - The days list where the first pos is the name of the day and the second one is the hours worked.
        """
        if worked_days == "":
            return []

        days = []
        for day_text in worked_days.split(","):
            day = [day_text[0:2], day_text[2 : len(day_text)]]
            days.append(day)

        return days
