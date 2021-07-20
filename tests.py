from app import index
import unittest

class HTestSuite(unittest.TestCase):
   
    testLoad = unittest.TestLoader()

    testClassesToRun =[index.TestUtils, index.TestReceiverFile, index.TestReceiverEmployee]

    suitesList = []
    for testClass in testClassesToRun:
        suite = testLoad.loadTestsFromTestCase(testClass)
        suitesList.append(suite)
   
    newSuite = unittest.TestSuite(suitesList)
    
    runner = unittest.TextTestRunner(verbosity=2)
    
    runner.run(newSuite)

