from app import index
import unittest


class HTestSuite(unittest.TestCase):

    test_load = unittest.TestLoader()

    test_classes_to_run = [
        index.TestUtils,
        index.TestReceiverFile,
        index.TestReceiverEmployee,
    ]

    suites_list = []
    for test_class in test_classes_to_run:
        suite = test_load.loadTestsFromTestCase(test_class)
        suites_list.append(suite)

    new_suite = unittest.TestSuite(suites_list)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(new_suite)
