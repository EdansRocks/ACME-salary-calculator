from ..components import file, employee
import unittest

"""
TestReceiverFile needs a file in public/data folder called test_example.txt  with this data:
RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00
ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00
"""
class TestReceiverFile(unittest.TestCase):

    def setUp(self):
        self.receiver =file.File()
        self.commandFileExists = file.FileExists(self.receiver)
        self.commandReadUsers = file.ReadUsers(self.receiver)
        self.invoker = file.FileInvoker()
        self.pathFile = './public/data/test_example.txt'

    def testFETrue(self):
        """ - Test File Exists: True """
        """ Expect True if the file exists in specific path """
        self.assertTrue(self.invoker.submit(self.commandFileExists, self.pathFile))

    def testFEFalse(self):
        """ - Test File Exists: False """
        """ Expect False if the file not exists in specific path """
        self.assertFalse(self.invoker.submit(self.commandFileExists, self.pathFile + 'Non-Existin-File'))

    def testRUIsList(self):
        """ - Test Read Users: list """
        """ Expect a list of all the users information """
        self.assertIsInstance(self.invoker.submit(self.commandReadUsers, self.pathFile), list)

    def testRUIsNotNone(self):
        """ - Test Read Users: Not None """
        """ Expect an not None return from method """
        self.assertIsNotNone(self.invoker.submit(self.commandReadUsers, self.pathFile))

    def testRUIsIn(self):
        """ - Test Read Users: User Exist"""
        """ Expect a list with the specific user information """
        self.assertIn('RENE', self.invoker.submit(self.commandReadUsers, self.pathFile)[0])


class TestReceiverEmployee(unittest.TestCase):

    def setUp(self):
        self.receiver =employee.Employee()
        self.command = employee.CalculateSalary(self.receiver)
        self.invoker = employee.EmployeeInvoker()

        self.daysWorked = [['MO', '10:00-12:00'], ['TU', '10:00-12:00'], ['TH', '01:00-03:00'], ['SA', '14:00-18:00'], ['SU', '20:00-21:00']]

    def testCSEqual(self):
        """ - Test Calculate Salary: Integer """
        """ Expect an integer with the value of an user payment amount """
        self.assertEqual(self.invoker.submit(self.command, self.daysWorked), 215)
