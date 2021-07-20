import os.path

class File:

    '''
    FE - Check if a file exists on public/data (FILES_PATH) folder
    param fileName: String - Name of the txt file
    return: Boolean - True if file exists otherwise False
    '''
    def fileExists(self, fileName):
        exists = os.path.isfile(fileName) or os.path.isfile(fileName+'.txt')
        return exists
        
    '''
    RU - Read specific file of employees and returns an array of them
    param filePath: String - Path where the txt file with the employee information is located
    return: Array - An array with the users list 
            None if find an error format in file
    '''
    def readUsers(self, filePath):

        try:
            file = open(filePath, 'r')
            users = []

            for line in file:
                text = line.strip().split('=')

                name = text[0]
                days = self.__splitWorkedDays(text[1])
                user = [name, days]

                users.append(user)

            file.close()

            return users

        except:
            file.close()

            return

    '''
    Split the worked days as an string into an array
    param workedDays: String - Worked days info
    return: Array - The days list where the first pos is the name of the day and the second one is the hours worked.
    '''
    def __splitWorkedDays(self, workedDays):
        
        if(workedDays == ''):
            return []

        days = []

        for dayText in workedDays.split(','):
            
            day = [ dayText[0:2], dayText[2:len(dayText)] ]

            days.append(day)
        
        return days