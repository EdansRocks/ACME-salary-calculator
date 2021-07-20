from ..common.utils import *
from ..payment_config import *
from datetime import datetime
import unittest

class TestUtils(unittest.TestCase):

    def setUp(self):
        self.start = datetime.strptime('00:01', '%H:%M')
        self.end = datetime.strptime('09:00', '%H:%M')
        self.startWorked = datetime.strptime('04:00', '%H:%M')
        self.endWorked = datetime.strptime('08:00', '%H:%M')
        self.outOfSchedule = datetime.strptime('18:00', '%H:%M')
        self.pathFile = './public/data/archivo_test'
        self.pathResult = self.pathFile + '.txt'

    def testCBDThreeDatesTrue(self):
        """ - Test Check Between Dates: Three Dates True """
        """ Expect True if datetime is between start - end """
        self.assertTrue(checkBetweenDates(self.start, self.end, self.startWorked))

    def testCBDFourDatesTrue(self):
        """ - Test Check Between Dates: Four Dates True """
        """ Expect True if two datetimes are between start - end """
        self.assertTrue(checkBetweenDates(self.start, self.end, self.startWorked, self.endWorked))

    def testCBDThreeDatesFalse(self):
        """ - Test Check Between Dates: Three Dates False """
        """ Expect False if datetime is not between start - end """
        self.assertFalse(checkBetweenDates(self.end, self.start, self.startWorked))

    def testCDSTrue(self):
        """ - Test Check Date String: True """
        """ Expect True if the string complies with the format 'xx:xx' """
        self.assertTrue(checkDateString('19:00'))

    def testCDSFalse(self):
        """ - Test Check Date String: False """
        """ Expect False if the string not complies with the format 'xx:xx' """
        self.assertFalse(checkDateString('119:00'))

    def testCSIn(self):
        """ - Test Check Schedule: Exists """
        """ Expect a key of an schedule that exist in SCHEDULES """
        self.assertIn(checkSchedule(self.startWorked, self.endWorked), SCHEDULES.keys())

    def testCSNotIn(self):
        """ - Test Check Schedule: Not Exists """
        """ Expect a key of an schedule that not exist in SCHEDULES """
        self.assertNotIn(checkSchedule(self.startWorked, self.outOfSchedule), SCHEDULES.keys())

    def testCTDIsDatetime(self):
        """ - Test Convert To Dates: Datetime """
        """ Expect datetime from a string with format 'xx:xx' """
        self.assertIsInstance(convertToDates('00:00', '23:59')[0], datetime)

    def testGHWEqual(self):
        """ - Test Get Hours Worked: Integer """
        """ Expect integer with the value of hours worked  """
        self.assertEqual(getHoursWorked(self.startWorked, self.endWorked), 4)

    def testGSDIsDatetime(self):
        """ - Test Get Schedule Dates: Datetime """
        """ Expect start and end datetime from an schedule in SCHEDULES """
        self.assertIsInstance(getScheduleDates(0)[0], datetime)

    def testSTEFEqual(self):
        """ - Test Set Txt Extension File: String"""
        """ Expect a string with the correct path of file with .txt extension  """
        self.assertEqual(setTxtExtensionFile(self.pathFile), self.pathResult)